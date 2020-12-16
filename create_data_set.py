import numpy as np
import os


if __name__ == "__main__":
    path_src = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_S6__HW\OpenCV-Python-Tutorials-and-Projects\HW\flowers - Google Search'
    path_target = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_S6__HW\OpenCV-Python-Tutorials-and-Projects\HW\n'
    # path_src = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_S6__HW\OpenCV-Python-Tutorials-and-Projects\HW\ariana'
    # list all images
    # for file in os.listdir(path_src):
    #     print(file)

    ## rename and move images
    # for root, dirs, files in os.walk(path_src):
    #     i = 0
    #     for file in files:
    #         file = os.path.join(root, file)
    #         os.rename(file, "negative" + '\\' + "arianaa" + str(i) + ".jpg")
    #         i += 1

    print('Number of negatives {}'.format(len([ file for file in os.listdir(path_target)
                                                if file.endswith(('jpg', 'JPEG', 'png', 'bmp'))])))

    path_positives = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_S6__HW\OpenCV-Python-Tutorials-and-Projects\HW\p'
    print('Number of positives {}'.format(len([ file for file in os.listdir(path_positives)
                                                if file.endswith(('jpg', 'JPEG', 'png', 'bmp'))])))


    # for file os.listdir(path_target):

