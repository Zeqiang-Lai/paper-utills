from addbox import select_roi, addbox_with_diff
import os


def test_addbox_diff():
    root = 'real4'
    fns = ['ref', 'gt', 'lr', 'integrated', 'optimized', 'ours', 'biqrnn3d', 'mcnet', 'optimized', 'sspsr']
    fns.append('nssr')

    output_path = root + '_out'
    os.makedirs(output_path, exist_ok=True)

    from functools import partial
    pt = select_roi('real4/lr.png', size=100,
                    preview=partial(addbox_with_diff, gt='real4/gt.png'))
    for fn in fns:
        print(fn)
        addbox_with_diff(os.path.join(root, fn+'.png'),
                         pt,
                         os.path.join(root, 'gt.png'),
                         save=os.path.join(output_path, fn+'.png'))


if __name__ == '__main__':
    test_addbox_diff()
