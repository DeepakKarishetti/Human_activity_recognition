import sys
import matplotlib.pyplot as plt

a = sys.argv[1]
def plot_bar(a,b):
    plt.bar(a,b)
    plt.show()
    
if(int(a) == 1):
    a = (3,4,5,6,7)
    b = (27.5,15,62.5,17.5,20)
    plot_bar(a,b)

if(int(a) == 2):
    a = (4,5,6,7,9)
    b = (75,67.5,70,70,72.5)
    plot_bar(a,b)
