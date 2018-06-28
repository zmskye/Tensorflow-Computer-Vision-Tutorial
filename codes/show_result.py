import matplotlib.pyplot as plt
from PIL import Image


def deep_dream():
    contents = ['morvan1', 'sky']
    channels = [60, 61, 62, 121, 122, 123]
    plt.figure(1, figsize=(4, 12))
    plt.suptitle('mixed4d_3x3_bottleneck_pre_relu')
    for i in range(6):
        for j in range(2):
            plt.subplot(6, 2, 2*i+j+1)
            path = '../results/%s_mixed4d_3x3_bottleneck_pre_relu_%i.jpeg' % (contents[j], channels[i])
            image = Image.open(path)
            plt.imshow(image)
            if j == 0:
                plt.ylabel('channel %i' % channels[i])
            plt.xticks(())
            plt.yticks(())
    plt.savefig('../results/sum_deepdream.png', dpi=500)


def style_transfer():
    # plotting
    content = Image.open('../example_images/morvan2.jpg').resize((400, 400))
    plt.figure(1, figsize=(4, 7))
    for i in range(5):
        for j in range(3):
            plt.subplot(5, 3, 3*i+j+1)
            if j == 0:
                plt.imshow(content)
                if i == 0:
                    plt.title('Content')
            elif j == 1:
                style = Image.open('../example_images/style%i.jpg' % (i+1)).resize((400, 400))
                plt.imshow(style)
                if i == 0:
                    plt.title('Style')
            else:
                styled = Image.open('../results/morvan2_style%i.jpeg' % (i+1)).resize((400, 400))
                plt.imshow(styled)
                if i == 0:
                    plt.title('Styled')
            plt.xticks(());plt.yticks(())
    plt.tight_layout()
    plt.savefig('../results/sum_style_transfer.png', dpi=500)
    # plt.show()


if __name__ == '__main__':
    # deep_dream()
    style_transfer()