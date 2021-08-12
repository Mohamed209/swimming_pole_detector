import os
import random
import shutil
TEST_SIZE = 0.25
TRAIN_IMAGES_DIR = 'yolo_data/train/images/'
TRAIN_LBL_DIR = 'yolo_data/train/labels/'
VAL_IMAGES_DIR = 'yolo_data/val/images/'
VAL_LBL_DIR = 'yolo_data/val/labels/'
total_images = len(os.listdir(TRAIN_IMAGES_DIR))
sample_images = random.sample(os.listdir(
    TRAIN_IMAGES_DIR), int(total_images*TEST_SIZE))
for sample_image in sample_images:
    sample_image_name = sample_image.split('.')[0]
    shutil.move(src=TRAIN_IMAGES_DIR+sample_image,
                dst=VAL_IMAGES_DIR+sample_image)
    shutil.move(src=TRAIN_LBL_DIR+sample_image_name+'.txt',
                dst=VAL_LBL_DIR+sample_image_name+'.txt')
