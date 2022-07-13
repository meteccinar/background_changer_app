import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import cv2
import time
import glob
from PIL import Image

ROOT_DIR = os.path.abspath("../")

import warnings
warnings.filterwarnings("ignore")
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  # To find local version
from samples.coco import coco

MODEL_DIR = os.path.join(ROOT_DIR, "logs")


COCO_MODEL_PATH = os.path.join('', "mask_rcnn_coco.h5")


if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

IMAGE_DIR = os.path.join(ROOT_DIR, "images")

class InferenceConfig(coco.CocoConfig):

     GPU_COUNT = 1
     IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

model = modellib.MaskRCNN(mode="inference", model_dir='mask_rcnn_coco.hy', config=config)

    # Load weights trained on MS-COCO
model.load_weights('mask_rcnn_coco.h5', by_name=True)

class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
                   'bus', 'train', 'truck', 'boat', 'traffic light',
                   'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                   'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
                   'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
                   'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
                   'kite', 'baseball bat', 'baseball glove', 'skateboard',
                   'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
                   'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                   'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
                   'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
                   'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
                   'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
                   'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
                   'teddy bear', 'hair drier', 'toothbrush']


    


def dice_coef(y_true, y_pred):
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = np.sum(y_true_f * y_pred_f)
    dice_score = (2. * intersection + 1) / (np.sum(y_true_f) + np.sum(y_pred_f) + 1)
    print("Dice Similarity: {}".format(dice_score))
    return dice_score



def applyBackground(originalImage,bgImage):

    dir_path = r'C:/Users/Metcnr/Desktop/bitirme_temp/human_images/'
    dice_path = ""
    image = skimage.io.imread(originalImage)
    newBg = skimage.io.imread(bgImage)


    x = image.shape[0]
    y = image.shape[1]

    resized_image = skimage.transform.resize(newBg, (x, y))
    rescaled_image = 255 * resized_image
    final_image = rescaled_image.astype(np.uint8)

    print("x :",x)
    print("y :",y)



    start = time.time()
    results = model.detect([image], verbose=1)
    end = time.time()
    print(end-start)

    r = results[0]
    res = visualize.display_newBG(image,final_image ,r['rois'], r['masks'],r['class_ids'],class_names, r['scores'],name="save.jpg")



    dice_path = "C:/Users/Metcnr/Desktop/bitirme_temp/dice/"+originalImage[50:-4]+".png"
    filepath = glob.glob("dice/"+originalImage[50:-4]+".png", recursive=True)

    if originalImage[50:-4] in str(filepath):
        true = cv2.imread(dice_path)
        dice_coef(true,image)
    else:
        print("Dice Mask is not found")



    return res[0]
