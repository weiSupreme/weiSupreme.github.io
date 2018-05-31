import matplotlib.pyplot as plt  
import numpy as np  
  
  
# draw the picture  
def draw(Curve_one, Curve_two, Curve_three, Curve_four):  
  
    plt.figure()  
      
    plot1, = plt.plot(Curve_one[0], Curve_one[1],     'bo-', linewidth=1.0, markersize=5.0)  
    plot2, = plt.plot(Curve_two[0], Curve_two[1],     'rx-', linewidth=1.0, markersize=5.0)  
    #plot3, = plt.plot(Curve_three[0], Curve_three[1], 'rh-', linewidth=1.0, markersize=5.0)  
    #plot4, = plt.plot(Curve_four[0], Curve_four[1],   'k^-', linewidth=2.0, markersize=10.0)  
      
    # set X axis  
    plt.xlim( [0, 1.05] )  
    plt.xticks( np.linspace(0, 1.0, 11) )  
    plt.xlabel("Recall", fontsize="x-large")  
      
    # set Y axis  
    plt.ylim( [0, 1.05] )  
    plt.yticks( np.linspace(0, 1.0, 11) )  
    plt.ylabel("Precision",    fontsize="x-large")  
      
    # set figure information  
    plt.title("SSD400", fontsize="x-large")  
    plt.legend([plot1, plot2], ("OriginalSSD", "OurSSD"), loc="lower left", numpoints=1)  
    plt.grid(True)  
  
    # draw the chart  
    plt.show()  
  
  
# main function  
def main():  
    # Curve one  
    Curve_one = [ (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),   
                  (1, 0.995, 0.995, 0.993, 0.989, 0.982, 0.967, 0.952, 0.922, 0.847, 0.0) ]  
  
    # Curve two  
    Curve_two  = [ (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),   
                   (1, 1, 1, 1, 1, 0.998, 0.987, 0.977, 0.963, 0.896, 0) ]  
  
    # Curve three  
    Curve_three = [ (0.997050, 0.992867, 0.987220, 0.977600, 0.957650, 0.912350, 0.833100, 0.743753, 0.664700, 0.598011, 0.542317),  
                    (0.103480, 0.239338, 0.411086, 0.578412, 0.734205, 0.858531, 0.928235, 0.956837, 0.979437, 0.984903, 0.997224) ]  
  
    # Curve four  
    Curve_four = [ (0.995750, 0.982433, 0.960270, 0.928964, 0.887517, 0.835059, 0.775115, 0.713273, 0.652159, 0.594189, 0.541702),  
                   (0.107366, 0.258592, 0.421263, 0.570542, 0.700825, 0.805936, 0.884097, 0.938723, 0.972731, 0.990533, 0.998092) ]  
  
    # Call the draw function  
    draw(Curve_one, Curve_two, Curve_three, Curve_four)  
  
  
# function entrance  
if __name__ == "__main__":  
    main()
