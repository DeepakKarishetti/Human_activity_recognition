**README FILE**

````````````````````````````
Deepak Rajasekhar Karishetti

````````````````````````````

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
