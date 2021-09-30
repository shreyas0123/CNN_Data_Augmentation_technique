########################### Problem1 #############################################
# Importing necessary functions
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        width_shift_range=0.2, # horizontal shift
        height_shift_range=0.2, # vertical shift
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 
img = load_img('E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/images/000001.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 
   
# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
                          save_to_dir ='E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/Aug image', 
                          save_prefix ='image', save_format ='jpeg'):
    i += 1
    if i > 5:
        break

################################## Problem2 ######################################
# Importing necessary functions
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        width_shift_range=0.2, # horizontal shift
        height_shift_range=0.2, # vertical shift
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 
img = load_img('E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/images/000067.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 
   
# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
                          save_to_dir ='E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/Aug image', 
                          save_prefix ='image', save_format ='jpeg'):
    i += 1
    if i > 5:
        break


################################# Problem3 ##################################################
# Importing necessary functions
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        width_shift_range=0.2, # horizontal shift
        height_shift_range=0.2, # vertical shift
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 
img = load_img('E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/images/000456.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 
   
# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
                          save_to_dir ='E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/Aug image', 
                          save_prefix ='image', save_format ='jpeg'):
    i += 1
    if i > 5:
        break


############################################### Problem4 ##################################
# Importing necessary functions
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        width_shift_range=0.2, # horizontal shift
        height_shift_range=0.2, # vertical shift
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 
img = load_img('E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/images/000542.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 
   
# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
                          save_to_dir ='E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/Aug image', 
                          save_prefix ='image', save_format ='jpeg'):
    i += 1
    if i > 5:
        break
########################################### Problem5 ############################## Importing necessary functions
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        width_shift_range=0.2, # horizontal shift
        height_shift_range=0.2, # vertical shift
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 
img = load_img('E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/images/001150.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 
   
# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
                          save_to_dir ='E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/Aug image', 
                          save_prefix ='image', save_format ='jpeg'):
    i += 1
    if i > 5:
        break
######################################### Problem6 ################################
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        width_shift_range=0.2, # horizontal shift
        height_shift_range=0.2, # vertical shift
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 
img = load_img('E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/images/001763.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 
   
# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
                          save_to_dir ='E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/Aug image', 
                          save_prefix ='image', save_format ='jpeg'):
    i += 1
    if i > 5:
        break
    
######################################Problem7 #####################################
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        width_shift_range=0.2, # horizontal shift
        height_shift_range=0.2, # vertical shift
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 
img = load_img('E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/images/004545.jpg') 
# Converting the input sample image to an array
x = img_to_array(img)
# Reshaping the input image
x = x.reshape((1, ) + x.shape) 
   
# Generating and saving 5 augmented samples 
# using the above defined parameters. 
i = 0
for batch in datagen.flow(x, batch_size = 1,
                          save_to_dir ='E:/ARTIFICIAL INTELIGENCE/Assignment/Convolution Neural Network/Aug image', 
                          save_prefix ='image', save_format ='jpeg'):
    i += 1
    if i > 5:
        break
    
###################################### END #################################################    