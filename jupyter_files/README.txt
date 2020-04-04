CSCI_573
Project-2 (Deliverable-1)

``````````````````````````````

Deepak Rajasekhar Karishetti
10846936

``````````````````````````````
Programming language: Python 3

``````````````````````````````

Running the code:

	(i) Open the Linux terminal at the destination of the file.
	(ii) Run the following command on the Linux terminal:
		For Relative Angles and Distances (RAD):
			>> python3 rad.py 
		
		For Histogram of Joint Posiion Differences (HJPD):
			>> python3 hjpd.py

		For Histogram of Oriented Displacements (HOD):
			>> python3 hod.py


		Running the respective file, with the respective dataset produces an output file containing the skeletal-based representation data.

``````````````````````````````
	(iii) Implementation:

		(a) RAD:
			-File destination is defined and the training datasets are opened to get all the required information from the dataset.

			-Joints used are: 1, 4, 8, 12, 16, 20, and 5 bins used.

			-All the joints used have their information stored in a dictionary and is appended it to a full_frame_list list, where the (x,y,z) values are stored after checking for all the possible NAN values.

			-All the distances between the joint 1 and other joints are calculated taking joint 1 as the reference joint. 
			 Similarly, all the angles between the adjacent body extremeties are calculated with joint 1 as the reference and taking the difference btween the vectors from this point to find the angle.
			
			-After the joint distances and the adjacent angles are calculated, then histograms are computed with a defined bin size (N for distances and M for angles) and then normalized to compensate for the different number of frames in any data instance.

			-Later, all the histograms are concatenated into a one-dimensional vector of length 5(M+N).
	
			-The computed 1-D vector is then written to a file to store the information extracted from the above analysis.

			-The output for the train dataset is 'rad_dl' and for the test dataset is 'rad_dl.t'.


		The process remains the same for RAD, HJPD and HOD.




		(b) HJPD:
			-Joints used are: All the 20 joints, and 5 bins used.
	
			-Here the basic process remains the same, except that only the displacements between the joint 1 and all other joints are computed.

			-All the joint distances are computed and stored for computing histogram as explained for RAD.

			-The output for the train dataset is 'hjpd_dl' and foe the test dataset is 'hjpd_dl.t'.




		(c) HOD:
			-Joints used are: All the 20 joints, and 8 bins used.

			-In this case, all the (x,y,z) values for each joint is extraced from the input dataset and then used to compute the following:

			-The projection of the joints are estimated from the x,y and z axis, so as to find the possible trajectories for each of the joints for all the respective frames.
	
			-Then with the projection on the 2D plane, the slope is calculated for the respective joints for each of xy, yz and zx planes with the respective axis.

			-Then these slopes are used to compute histograms for each of the frame for the respective frames. Here the bins are selected to be 8 having each bin to be 45 when the angles are computed in degrees. The joint projection or the trajectory can be seen from the histogram that gives us the frequency or the occurence with respect to the angles.

			-This is then written to an output file. The output for the train dataset is 'hod_dl' and for the test dataset is 'hod_dl.t'.


