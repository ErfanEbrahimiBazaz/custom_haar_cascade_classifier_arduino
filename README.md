# custom_haar_cascade_classifier_arduino

Training a custom haar cascade classifier by following [Muraza's code](https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects). 

The steps are as follows:

1. Create your dataset by putting a number of images of the object you want to detect in a folder called "p" and at least 1.5 times more negative samples in a folder called "n".
2. Install the cascade trainer at [link](https://amin-ahmadi.com/cascade-trainer-gui/). Enter the number of negatives and tune other parameters. For this trainer I used 169 positives and 369 negatives. Some of the samples I used are available in the repo as samples.
3. Rename your haar cascade and saved it to your preferred directory. 
4. Apply the code detector_on_cam.py and tune the parameters until it worked properly.
