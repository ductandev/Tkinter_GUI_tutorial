from PIL import Image
import numpy
im = Image.open("sample2.png")
np_im = numpy.array(im)
print (np_im.shape)
np_im = np_im - 18
#print(np_im)
new_im = Image.fromarray(np_im)
print (new_im)
new_im.save("numpy_altered_sample2.png")
