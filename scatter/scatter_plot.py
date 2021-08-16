import matplotlib.pyplot as plt

gaussian = [
    (38.45, 154, 'BM4D', 20, 0.1),
    (41.48, 1755, 'KBR', -350, -0.7),
    (42.62, 1600, 'WLRTR', -600, 0.3),
    (42.99, 166, 'NGmeet',-50, -0.7),
    (38.70, 3, 'HSCNN', 0.5, 0.1),
    (42.22, 0.8, 'QRNN3D', -0.1, -0.6),
    (43.06, 1, 'Ours', 0.2, 0),
]

complex = [
    (32.80, 6, 'LRMR', 1, 0.1),
    (33.62, 88, 'LRTV', 15, 0),
    (34.51, 170, 'NMoG', 25, 0.1),
    (38.14, 231, 'TDTV', 45, -0.2),
    (38.40, 3, 'HSCNN', 0.5, -0.2),
    (42.79, 0.8, 'QRNN3D', 0.1, -0.5),
    (42.89, 1, 'Ours', 0.1, -0.2)
]

inpainting = [
    (41.90, 500, 'WLRTR', -300, -0.5),
    (39.10, 40, 'FastHy', 5, 0),
    (42.43, 100, 'Ours', 10, 0),
]

sr = [
    (39.8, 0.7, '3D-FCNN', 0.1, 0),
    (47.5, 4.4, 'SSPSR', 0.5, 0),
    (41.1, 0.3, 'IFN', 0.1, 0),
    (42.5, 1.8, 'Bi-3DQRNN', 0.1, 0),
    (48.8, 25, 'Ours', -13, 0)
]

def denoise():
    fig, ax = plt.subplots()

    psnr, time, name, xt, yt = zip(*gaussian)
    x, y = time, psnr
    ax.scatter(x, y, color='red', alpha=0.6, label='Gaussian')
    for i in range(len(x)):
        plt.annotate(name[i], xy = (x[i], y[i]), xytext = (x[i]+xt[i], y[i]+yt[i]))
        
    psnr, time, name, xt, yt = zip(*complex)
    x, y = time, psnr
    ax.scatter(x, y, color='blue', alpha=0.6, label='Complex')
    for i in range(len(x)):
        plt.annotate(name[i], xy = (x[i], y[i]), xytext = (x[i]+xt[i], y[i]+yt[i]))
        
    ax.legend()
    # ax.grid(True)
    
    plt.title('Denoising Task')
    plt.xlabel('Running Time (sec)')
    plt.ylabel('PSNR (dB)')
    plt.xscale('symlog')
    plt.savefig('denoise.pdf')
    plt.show()

def sr_inpainting():
    fig, ax = plt.subplots()

    psnr, time, name, xt, yt = zip(*sr)
    x, y = time, psnr
    ax.scatter(x, y, color='red', alpha=0.6, label='Super Resolution')
    for i in range(len(x)):
        plt.annotate(name[i], xy = (x[i], y[i]), xytext = (x[i]+xt[i], y[i]+yt[i]))
        
    psnr, time, name, xt, yt = zip(*inpainting)
    x, y = time, psnr
    ax.scatter(x, y, color='blue', alpha=0.6, label='Inpainting')
    for i in range(len(x)):
        plt.annotate(name[i], xy = (x[i], y[i]), xytext = (x[i]+xt[i], y[i]+yt[i]))
        
    ax.legend()
    # ax.grid(True)
    
    plt.title('Super Resolution & Inpainting Tasks')
    plt.xlabel('Running Time (sec)')
    plt.ylabel('PSNR (dB)')
    plt.xscale('symlog')
    plt.savefig('sr_inpaint.pdf')
    plt.show()

# denoise()
sr_inpainting()