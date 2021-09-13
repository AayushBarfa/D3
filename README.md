# Driver Drowsiness Detection
<h2>About</h2>
Various studies have suggested that around 20% of all road accident are fatigue-related. This usually happens when a driver has not slept enough, but it can also happen because of untreated sleep disorders, medications, drinking alcohol, or shift work. Makes you less able to pay attention to the road. Slows reaction time if you have to brake or steer suddenly. 
       The main aim of this is to develop a drowsiness detection system by monitoring the facial expression; it is believed that the symptoms of driver fatigue can be detected early enough to avoid a car accident. Detection of fatigue involves the observation of eye movements and blink patterns. 

</br>

<h2>Approach</h2>

This section details the proposed approach to detect driver’s drowsiness. First, we’ll set up a camera that monitors a stream for faces. The process starts with capturing of live images from camera and search for face. If a face is found Face Recognition Library is employed to detect facial landmarks and a threshold value is used to detect whether driver is drowsy or not. These facial landmarks are then used to compute the EAR (Eye Aspect Ratio) and Yawn Ration the both the computed value be compared with the threshold value taken as 0.25 for EAR and 25 Yawn Ration. If the EAR value is less than the threshold value and if yawn ration is more than threshold limit then any of this would indicate a state of fatigue. In case of Drowsiness, the driver and the passengers would be alerted by an alarm. The subsequent section details the working of each module. After that alarm will be automatically stops when driver gets out of that situation. 

</br>

<h2>Implementation</h2>

<h3>Facial Landmark Marking</h3>
To extract the facial landmarks of drivers, Face Recognition library was imported which is Built using dilb’s state-of-the-art face recognition built with deep learning. The library uses a pre-trained face detector, which is based on a modification to the histogram of oriented gradients and uses linear SVM (support vector machine) method for object detection. The model has an accuracy of 99.38%. Actual facial landmark predictor was then initialized and facial landmarks captured by the application were used to calculate distance between points.

![FaceLandmark](https://github.com/AayushBarfa/D3/blob/master/images/figure_68_markup.jpg )


<h3>Ration Computation</h3>
The distance I calculated using facial landmark points is used to compute EAR value and Yawn ration.

![EyeMarks](https://github.com/AayushBarfa/D3/blob/master/images/481585_1_En_30_Fig7_HTML.png)

Using these points as shown in image ,I compute Euclidean distance between 𝑝2 and 𝑝6 store in A, 𝑝3 and 𝑝5 store in B, 𝑝1 and 𝑝4 store in C.
So EAR = (A + B) / (2.0 * C) Or in other words EAR = (|𝑝2 – 𝑝6| + |𝑝3 – 𝑝5|)/ (2 ∗ |𝑝1−𝑝4|).

![MouthMarks](https://github.com/AayushBarfa/D3/blob/master/images/images.jpg)

Using these points as shown in image we can compute the Euclidean distance between mean of the upper lip and lower lip points which is used for comparison with threshold limit. 
</br>


<h2>Result</h2>

![RunningEyesCheck](https://github.com/AayushBarfa/D3/blob/master/images/Screenshot%20(86).png)

As we can see in image Eyes are closed and thus EAR is decreased which is less then threshold limit so it is showing “Alert!” to notify the driver. This alert is not for Yawn Detection as mouth is not wide opened thus yawn ration is calculated is less then threshold limit.

![RunningMouthCheck](https://github.com/AayushBarfa/D3/blob/master/images/Screenshot%20(85).png)

Now in this image it is showing yawn alert as yawn ration is exceeded by threshold limit and in above image we can notice EAR is more than Ear threshold as eyes are open.



