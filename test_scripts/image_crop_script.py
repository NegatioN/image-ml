import matplotlib.image as mpimg
import sys
import os
import argparse
import imageio
import scipy.ndimage as ndi
from skimage.color import rgb2gray

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=".", help="Folder path of images")
parser.add_argument("-r", "--radius", type=int,  default=300, help="Radius from image weight to crop picture to.")
options = parser.parse_args()

img_radius = options.radius

def main():
    if not os.path.isdir('test_output'):
        os.mkdir('test_output')
    path = options.path
    file_names = os.listdir(path)
    for file_name in file_names:
        try:
            img = mpimg.imread('{}/{}'.format(path, file_name))
            cropperino_saverino(img, 'test_output/{}'.format(file_name))
        except:
            pass


def bounded_pixel(pix, _max):
    if pix > _max:
        return int(_max)
    elif pix < 0:
        return 0
    return int(pix)


def cropperino_saverino(img, uri):
    gray_img = rgb2gray(img)
    image_size_x = gray_img.shape[1]
    image_size_y = gray_img.shape[0]
    cy, cx = ndi.center_of_mass(gray_img)
    min_y = bounded_pixel(cy - img_radius, image_size_y)
    max_y = bounded_pixel(cy + img_radius, image_size_y)
    min_x = bounded_pixel(cx - img_radius, image_size_x)
    max_x = bounded_pixel(cx + img_radius, image_size_x)
    print('y min={} max={} x min={} max={}'.format(min_y,max_y,min_x,max_x))
    imageio.imwrite(uri, img[min_y:max_y, min_x:max_x])


if __name__ == "__main__":
    sys.exit(main())
