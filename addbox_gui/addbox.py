from os import PathLike
import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_img(img):
    if isinstance(img, PathLike):
        return cv2.imread(str(img))
    if isinstance(img, str):
        return cv2.imread(img)
    return img


def get_border_box_pt(h, w, size, thickness, pos):
    if pos == 'br':
        return (w-size-thickness, h-size-thickness)
    if pos == 'ur':
        return (w-size-thickness, 0)
    if pos == 'ul':
        return (0, 0)
    if pos == 'bl':
        return (0, h-size-thickness)


def addbox(img, pt, size=100, save=None,
           bbsize=200, bbpos='br',
           color=(0, 0, 255),
           thickness=1,
           bbthickness=2):
    img = get_img(img)
    H, W = img.shape[0], img.shape[1]

    ptb = get_border_box_pt(H, W, bbsize, bbthickness, pos=bbpos)
    crop_img = img[pt[1]:pt[1]+size, pt[0]:pt[0]+size]
    crop_img = cv2.resize(crop_img, (bbsize, bbsize))
    img[ptb[1]:ptb[1]+bbsize, ptb[0]:ptb[0]+bbsize] = crop_img

    # big box
    pt1 = ptb
    pt2 = (pt1[0]+bbsize, pt1[1]+bbsize)
    cv2.rectangle(img, pt1, pt2, color, bbthickness)

    # small box
    pt1 = pt
    pt2 = (pt1[0]+size, pt1[1]+size)
    cv2.rectangle(img, pt1, pt2, color, thickness)

    if save:
        cv2.imwrite(save, img)

    return img

def convert_color(arr, cmap=None, vmin=None, vmax=None):
    import matplotlib.cm as cm
    sm = cm.ScalarMappable(cmap=cmap)
    sm.set_clim(vmin, vmax)
    rgba = sm.to_rgba(arr, alpha=1, bytes=True)
    return rgba
    
def addbox_with_diff(input, pt, gt, size=100,
                     save=None,
                     color=(0, 0, 255),
                     thickness=1,
                     bbthickness=2):
    input = get_img(input)
    gt = get_img(gt)

    H, W, C = input.shape

    out = np.zeros((H, W+H//2, C))
    out[:, :W] = input

    # small box.
    pt1 = pt
    pt2 = (pt1[0]+size, pt1[1]+size)
    cv2.rectangle(out, pt1, pt2, color, thickness)

    # crop.
    bbsize = H//2
    crop_img = input[pt[1]:pt[1]+size, pt[0]:pt[0]+size]
    crop_img = cv2.resize(crop_img, (bbsize, bbsize))

    # diff
    input = input.astype('float') / 255
    gt = gt.astype('float') / 255
    # diff = convert_color(np.abs(input-gt)[:,:,1], vmin=0, vmax=0.2)
    # diff = (diff*255).astype('uint8')
    # diff = cv2.cvtColor(diff, cv2.COLOR_BGRA2BGR)
    plt.imsave('_tmp.png', np.abs(input-gt)[:,:,1], vmin=0, vmax=0.2)
    diff = cv2.imread('_tmp.png')
    
    crop_img_diff = diff[pt[1]:pt[1]+size, pt[0]:pt[0]+size]
    crop_img_diff = cv2.resize(crop_img_diff, (bbsize, bbsize))
    
    out[:H//2, W:W+H//2, :] = crop_img
    out[H//2:, W:W+H//2, :] = crop_img_diff
    
    out = out.astype('uint8') 
    
    if save:
        cv2.imwrite(save, out)
        
    return out

def select_roi(img, size=100, preview=None):
    if isinstance(img, str):
        img = cv2.imread(img)
    clean_img = np.array(img)

    sx, sy = None, None

    def mouse_drawing(event, x, y, flags, params):
        nonlocal sx, sy, img
        if event == cv2.EVENT_LBUTTONDOWN and sx is None:
            print(x, y)
            sx, sy = x, y
            # preview
            if preview:
                img = preview(img, (sx, sy))

    cv2.namedWindow("SelectROI")
    cv2.setMouseCallback("SelectROI", mouse_drawing)

    confirm_key = 32  # space
    clear_key = 98  # b

    while True:
        cv2.imshow("SelectROI", img)
        key = cv2.waitKey(1)
        if key == confirm_key:
            print('select', sx, sy)
            break
        if key == clear_key:
            print('clear')
            sx, sy = None, None
            img = np.array(clean_img)

    return sx, sy


