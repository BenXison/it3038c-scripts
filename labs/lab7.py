from PIL import Image
import os
import PIL

size_300 = (300,300)

#for f in os.listdir('.'):
#    if f.endswith('.jpg'):
#        i = Image.open(f)
#        fn, fext = os.path.splitext(f)
#        i.convert(mode='L')
#        i.thumbnail(size_300)
#        i.save('Lab7-output/{}.png'.format(fn))



img = Image.open('flag2.jpg')
img = img.rotate(90, PIL.Image.NEAREST, expand = 1)
img.thumbnail(size_300)
img.convert(mode='L').save('flag2.png')
