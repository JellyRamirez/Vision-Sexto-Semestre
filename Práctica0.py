from skimage import color
from skimage import io
from skimage.color import rgb2gray


img_2 = io.imread('ImagenRGB.jpg')
imgGray_2 = color.rgb2gray(img_2)
io.imsave('ImagenGray3.jpg',imgGray_2)