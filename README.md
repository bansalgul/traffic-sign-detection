# Traffic Sign Detection Project

## Overview
This repository contains code and resources for a traffic sign detection project aimed at enhancing road safety through computer vision technology. The project focuses on detecting and classifying various types of traffic signs using deep learning techniques, including the YOLOv8 (You Only Look Once version 8) object detection algorithm.

## YOLOv8
YOLOv8 is a state-of-the-art object detection algorithm that belongs to the YOLO family of models. It is characterized by the following key aspects:

- **Architecture**: YOLOv8 is built upon a deep convolutional neural network architecture, allowing it to predict multiple bounding boxes and their corresponding class probabilities within a single inference pass.
- **Backbone**: YOLOv8 typically uses a backbone network, such as Darknet, as its base feature extractor, enabling it to extract high-level features from input images.
- **Feature Pyramid Network (FPN)**: YOLOv8 may incorporate a Feature Pyramid Network (FPN) into its architecture to improve the detection of objects at different scales, enhancing its robustness to scale variations.
- **Training Techniques**: YOLOv8 utilizes advanced training techniques, including data augmentation, focal loss, and label smoothing, to improve model performance and convergence speed.
- **Post-processing**: After prediction, YOLOv8 applies post-processing techniques such as non-maximum suppression (NMS) to refine predictions and remove redundant detections.

## Dataset
The dataset used in this project consists of images captured manually along a route spanning approximately 240km from Mohali to Meerut. The images were annotated manually and divided into five categories based on the type of traffic sign:
- Warning
- Mandatory
- Regulatory
- General
- Informatory

## Training Process
The training process involves training the YOLOv8 model on the custom dataset. Data augmentation techniques such as histogram equalization are applied to enhance the training dataset and improve model robustness.

## Model Evaluation
Trained models are evaluated based on performance metrics such as precision, recall, and mean average precision (mAP). The best-performing model is selected based on evaluation results and further validated on a test dataset containing unseen images. Additionally, the model's performance is tested on random videos collected from nearby areas to assess its real-world applicability.


## Results
The results obtained from model predictions are analyzed and compared, highlighting improvements achieved through data augmentation and model training. Visualizations of model predictions on test data and videos are provided to demonstrate the model's effectiveness in detecting traffic signs.

![image](https://github.com/bansalgul/traffic-sign-detection/assets/146025595/8c68374e-c94b-4c3d-b2c8-78c882c67bcb)

![image0](https://github.com/bansalgul/traffic-sign-detection/assets/146025595/4d6c9d85-d773-4f00-ac51-283309f139d2)

## Future Enhancements
Suggestions for further improving accuracy and model performance include:
- Integration of additional data augmentation techniques
- Exploration of advanced model architectures such as Feature Pyramid Networks (FPN)
- Implementation of ensemble learning for improved generalization
- Continuous monitoring and fine-tuning of the model based on real-world feedback

## Contact
For any questions, suggestions, or inquiries related to the project, please contact @bansalgul @rastogi17
