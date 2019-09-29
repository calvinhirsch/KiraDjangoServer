import math
import numpy as np
#from keras.models import Model, load_model
from imageio import imread
import cv2
import base64
from io import BytesIO

"""
image is a matrix with a depth 
"""
def blur_metric(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

"""
image is a tensor of shape
[299, 299, 3]
"""
#def get_preds(image):
#    image = np.expand_dims(image, axis=0)
#    InceptionModel = load_model('iv3_v1.h5')
#    prediction = InceptionModel.predict(image)
#    return prediction

def cv_crop(image):
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours.sort(key = cv2.contourArea, reverse=True)
    contours = contours[:10]
    c = contours[1]
    #circularity = 0
    #for cont in contours:
    #    circ = circularity_measure(cv2.moments(cont))
    #    if circ > circularity:
    #        c = cont
    #        circularity = circ
    x,y,w,h = cv2.boundingRect(c)
    im_rect = cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imwrite('fTesting.jpg', im_rect)
    crop_img = image[y-100:y+h+100, x-100:x+w+100]
    return crop_img

def circularity_measure(M):
    return M['m00']**2 / ((M['m20'] + M['m02']) * 2*math.pi)

def square_crop(image):
    height, width, _ = image.shape
    t = image[int((height-width)/2):int((height+width)/2), :, :]
    return cv2.resize(t, (299, 299))

def readb64(base64_string):
    img = base64.b64decode(base64_string)
    img = BytesIO(img)
    img = imread(img)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def pipeline(b64_string):
    # Decodes image
    img = b64_string

    # Crops the image to correct dimensions
    img = square_crop(img)

    # Preliminary blur checkin
    blur = blur_metric(img)
    if blur < 100:
        return (None, img)

    # Finds correct contour
    crop = cv_crop(img.copy())

    # Analyzes quality of features extracted
    feature_extraction_metric = get_preds(img)
    if np.std(feature_extraction_metric) < 0.05 or max(feature_extraction_metric) < 0.5:
        return (None, img)

    return (crop, img)
    



    
