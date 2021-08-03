# Mask_Detection_and_Social_Distance


---------------------------------------------------------------------------------------------------

  
[ Detect Model ]


We will use Yolov5 to train an object detect model.

Please refer to https://github.com/ultralytics/yolov5.

The sources of datasets and classes are show below. 

<Data source>


-facemask

https://www.kaggle.com/aditya276/face-mask-dataset-yolo-format
  
https://www.kaggle.com/aditya276/face-mask-dataset-yolo-format

-person

https://www.kaggle.com/karthika95/pedestrian-detection

<classes>
( 0 no_mask, 1 with_mask, 2 person )

---------------------------------------------------------------------------------------------------

  
[Social Distance]

We use the above trained model, and then refer to the practice on github to calculate the social distance. 
Please refer to https://github.com/lucasresck/deep-learning-and-applications.git
Use the center point of the bounding box as the calculation basis, and then use the transfer matrix to adjust the calculation of the distance.

