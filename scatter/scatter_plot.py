import matplotlib.pyplot as plt


def plot_scatter(ax, data, **kwargs):
    """ plot scatter graph with annoation for each point

        Usage:
        ```
        fig, ax = plt.subplots()
        gaussian = [
            (154, 38.45, 'BM4D', 20, 0.1),
            (1755, 41.48, 'KBR', -350, -0.7),
        ]
        plot_scatter(ax, gaussian, color='red', alpha=0.6, label='Gaussian')    
        ```
    Args:
        ax: matplotlib axes object
        data: list of description for each point in the format of (x, y, name, xtext, ytext) 
        kwargs: you can pass any args of plt.scatter to this function.
    """
    
    x, y, name, xt, yt = zip(*data)
    ax.scatter(x, y, **kwargs)
    for i in range(len(x)):
        plt.annotate(name[i], xy=(x[i], y[i]), xytext=(x[i]+xt[i], y[i]+yt[i]))


## Exampel usages

def denoise():
    gaussian = [
        (154, 38.45, 'BM4D', 20, 0.1),
        (1755, 41.48, 'KBR', -350, -0.7),
        (1600, 42.62,  'WLRTR', -600, 0.3),
        (166, 42.99,  'NGmeet', -50, -0.7),
        (3, 38.70, 'HSID-CNN', 0.5, 0.1),
        (0.8, 42.22,  'QRNN3D', -0.1, -0.6),
        (1, 43.06,  'Ours', 0.2, 0),
    ]

    complex = [
        (6, 32.80, 'LRMR', 1, 0.1),
        (88, 33.62,  'LRTV', 15, 0),
        (170, 34.51,  'NMoG', 25, 0.1),
        (231, 38.14, 'TDTV', 45, -0.2),
        (3, 38.40,  'HSID-CNN', 0.5, -0.2),
        (0.8, 42.79,  'QRNN3D', 0.1, -0.5),
        (1, 42.89,  'Ours', 0.1, -0.2)
    ]
    
    fig, ax = plt.subplots()

    plot_scatter(ax, gaussian, color='red', alpha=0.6, label='Gaussian')
    plot_scatter(ax, complex, color='blue', alpha=0.6, label='Complex')

    ax.legend()

    plt.title('Denoising Task')
    plt.xlabel('Running Time (sec)')
    plt.ylabel('PSNR (dB)')
    plt.xscale('symlog')
    plt.savefig('denoise.pdf')
    plt.show()


def sr_inpainting():
    inpainting = [
        (500, 41.90, 'WLRTR', -300, -0.5),
        (40, 39.10,  'FastHyIn', 5, 0),
        (100, 42.43,  'Ours', 10, 0),
    ]

    sr = [
        (0.7, 39.8, '3D-FCNN', 0.1, 0),
        (4.4, 47.5,  'SSPSR', 0.5, 0),
        (0.3, 41.1, 'IFN', 0.1, 0),
        (1.8, 42.5, 'Bi-3DQRNN', 0.1, 0),
        (25, 48.8,  'Ours', -13, 0)
    ]

    fig, ax = plt.subplots()

    plot_scatter(ax, sr, color='red', alpha=0.6, label='Super Resolution')
    plot_scatter(ax, inpainting, color='blue', alpha=0.6, label='Inpainting')

    ax.legend()

    plt.title('Super Resolution & Inpainting Tasks')
    plt.xlabel('Running Time (sec)')
    plt.ylabel('PSNR (dB)')
    plt.xscale('symlog')
    plt.savefig('sr_inpaint.pdf')
    plt.show()


if __name__ == '__main__':
    # denoise()
    sr_inpainting()