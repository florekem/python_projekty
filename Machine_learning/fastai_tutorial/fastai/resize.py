import cv2
import os

path = 'train/'
path2 = 'train_resized/'

for file in os.listdir(path):
    bgr_img = cv2.imread(os.path.join(path, file))
    b,g,r = cv2.split(bgr_img)
    rgb_img = cv2.merge([r,g,b])
    
    ORIGINAL_SIZE = 96
    CROP_SIZE = 48
    
    start_crop = (ORIGINAL_SIZE - CROP_SIZE) // 2
    end_crop = start_crop + CROP_SIZE
    rgb_img = rgb_img[start_crop:end_crop, start_crop:end_crop]
    
    cv2.imwrite(os.path.join(path2, file), rgb_img)