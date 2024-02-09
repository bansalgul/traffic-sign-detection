import cv2
import os
import shutil

def histogram_equalization(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting to gray scale
    equalized = cv2.equalizeHist(gray) #applying histogram equalization
    equalized_bgr = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR) #converting back to BGR
    return equalized_bgr #returning histogram equalized image

def preprocessing_dataset(image_dir, label_dir, output_image_dir, output_label_dir):

    #creating output directories, if they dont exist
    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)
    if not os.path.exists(output_label_dir):
        os.makedirs(output_label_dir)
    
    #for each image in the training image directory
    for filename in os.listdir(image_dir):
        if filename.lower().endswith((".jpeg", ".jpg")):

            image_path = os.path.join(image_dir, filename)
            image = cv2.imread(image_path) #read image
            
            #calling histogram equalization function
            equalized_image = histogram_equalization(image)
            
            #saving the equalized image to the output directory with _he added to its name
            if filename.endswith(".jpeg"):
                he_filename = filename.split('.')[0] +'_he' +'.jpeg'
            elif filename.endswith(".jpg"):
                he_filename = filename.split('.')[0] +'_he' +'.jpg'
            else:
                he_filename = filename.split('.')[0] +'_he' +'.JPG'

            output_image_path = os.path.join(output_image_dir, he_filename)
            cv2.imwrite(output_image_path, equalized_image)
            
            #copying the corresponding label file to the output label directory as no resizing is done, the same label file will work
            label_filename = filename.split('.')[0] +'.txt'
            label_path = os.path.join(label_dir, label_filename)
            
            out_lab_filename = filename.split('.')[0] +'_he' +'.JPG' 
            output_label_path = os.path.join(output_label_dir, out_lab_filename)
            shutil.copy(label_path, output_label_path)
    print('Done.')