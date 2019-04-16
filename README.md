ROS package for MASHI platform
================================
This is a python ROS package that performs a pre-processing of the images captured by the MASHI robot webcam. The video without fisheye effect and with an image enhancement application is taken by the ros_face_recognition package to execute face detection and recognition. An id for each user is stored and then given the name. This name is reproduced by a simple html page that connects to the rosbridge server

Dependencies on Python 2.7
-----------------------------
- OpenCV v3.4
- Numpy
- Dlib v19.6

Installation
---------------
- Clone [usb_cam ros node](http://wiki.ros.org/usb_cam) for interfacing with USB camera
- Clone [vision_opencv](https://github.com/ros-perception/vision_opencv) repository to your catkin_ws src folder and ```cd .. && catkin_make --pkg cv_bridge```.
- Clone [ros_face_recognition](https://github.com/bryandario8/ros_face_recognition) package to your catkin_ws src folder and ```cd .. && catkin_make --pkg ros_face_recognition```.
- Execute the bash file located in ros_face_recognition scripts data folder to download the models, so ```./models.sh```.
- Install rosbridge package, depending on your distribution of ros ```sudo apt-get install ros-<rosdistro>-rosbridge-server```.

Running
----------

- Open a terminal
  ```
  source ~/catkin_ws/devel/setup.bash
  roslaunch mashi_ros webcam_face_recognition.launch
  ```

- In other terminal
  ``` 
  source ~/catkin_ws/devel/setup.bash
  roslaunch rosbridge_server rosbridge_websocket.launch
  ```

Training
--------
To save the characteristics of the detected users press CTRL-C on the first terminal. Then the faces.json file will be created with data such as id, name and gender, located in the ros_face_recognition scripts faces folder. There you can edit the username instead of its corresponding id.

Final test
----------
Finally, run the launch file of mashi_ros again and in the mozilla browser open the create_audio.html file that is located in mashi_ros web folder. Remember that rosbridge server must also be running. Then, the first time the system recognizes a new face, it will emit a greeting with the respective user's name.
