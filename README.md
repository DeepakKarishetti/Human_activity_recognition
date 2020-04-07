**README FILE**

````````````````````````````
Deepak Rajasekhar Karishetti

````````````````````````````
**Abstract:**
 - In this project work, several star skeletal based representations are implemented, namely, Relative Angles and
Distances (RAD), Histogram of Joint Position Differences (HJPD) and Histograms of Oriented Displacements (HOD).
 - These representations are then classified based on the human behaviours with the use of Support Vector Machines (SVMs),
using a public activity dataset collected from a Kinect V1 sensor. 
 - The dataset used in this project is one of the most widely applied benchmark dataset in human behaviour understanding tasks. The dataset used in this project is a subset of the original dataset, which only uses six(6) activity categories.     
 - Initially, the datasets are used to implement three specific star skeletal based representations to convert all the data instances from the Train and Test folders into a single training file and a testing file respectively, each line corresponding to the representation data instance. 
 - The training and testing files of all the representations are then converted into a format that can be used by LIBSVM. LIBSVM is applied to the output files, using its APIs provided, to learn a C-SVM model with the RBF kernel from the training data, and then the learned model is used to predict the behaviour labels of the testing data, which will generate a result file for all the representations. 
 - This project is programmed using Python on a Linux system which reads the data from the training and testing directories and creates a given representation, performs robot learning, and outputs all the information of accuracy and confusion matrix to the user when run on a Linux terminal. 
 - The accuracy obtained for each of the representations are then analyzed for different number of bins. and are tuned accordingly to obtain the required accuracy.



(1) The graphs for all the representations are put into the main folder           

(2) The best values for different representations are as follows:

	(i) **RAD representation:**

		C value = 1.0
		Gamma value = 1.0
		Accuracy = 62.5%

	(ii) **HJPD representation:**

		C value = 2.0
		Gamma value = 0.0625
		Accuracy = 75%


	(iii) **HOD representation:**

		C value = 2.0
		Gamma value = 0.5 
		Accuracy = 87.5%


(3) All the covered representation files and the output files are saved in the main folder

	Running for accuracy:

		(i) **RAD** >>python3 combined_accuracy_code.py [args]

			[args]  => 1 for RAD
				   2 for HJPD
				   3 for HOD

(4) The figures showing the variations between the accuracy and the number of bins are saved in the bar_plots folder


(5) **Dependencies:**

		numpy
		scipy
		os
		sys
		glob
		matplotlib

(6) Confusion matrix is obtained when run for the representation accuracy by varying the input arguments.
