import matplotlib.pyplot as pyplot
import numpy as np
import cv2
from PIL import Image
from django.core.files.storage import FileSystemStorage
from sitebetaver.settings import MEDIA_ROOT, MEDIA_URL
import os

def ImageEqualizer (img_path):
    #i = Image(imgDefault=myfile)
    #i.save()
    img_path2 = os.path.join(MEDIA_ROOT, img_path)
    print("media path : "+MEDIA_ROOT)
    print("img path path : "+img_path)
    print("image path : "+img_path2)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img = cv2.imread(img_path2)
    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]

    clB = clahe.apply(B)
    clG = clahe.apply(G)
    clR = clahe.apply(R)
    
    imgnoDef = Image.fromarray(np.dstack((clR, clG, clB)).astype(np.uint8),'RGB')
    uploaded_file_path = os.path.join(MEDIA_ROOT,'out.jpg')
    imgnoDef.save(uploaded_file_path)
    uploaded_file_path = os.path.join(MEDIA_URL,'out.jpg')
    # fs = FileSystemStorage()
    # filename = fs.open('out.jpg')
    # uploaded_file_url = fs.url(filename)

    return uploaded_file_path