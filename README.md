# Plot Digitizer


SIMPLE plot digitizer.

I wrote this code when working on a project where I had to extract quite a bit of data points from literature. I did not want to upload every time a picture into a plot digitizer, so I included an image **crop** tool option into the code in order to take a picture of the **desktop** and crop the image where the **graph is located**.

No need to copy picture from PDF, since it has a selecting tool in order for you to select the image and start extracting those points! And save them as well into an xlsx sheet. 

* What can this thing do:
   * Manually crop images from pdfs, and manually mark the points you want to extract out of them
   * Save the extracted points into an **`xlsx`** sheet or look at them directly in the command window
   
* What you **CAN'T** do:
   * Automatically detect points (nice feature to work in the near future)
   * Upload images of your own (Meaning that it only works with the cropped images from your desktop screen, which I believe is nicer)



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This code was written on `python==3.6.6`, but it should work on all python versions which have the following dependencies covered:

**Dependencies**:

```
numpy==1.15.1
matplotlib==3.0.0
pyexcel==0.5.9.1 and pyexcel-xlsx
Pillow==5.3.0
pyscreenshot==0.4.2
XlsxWriter==1.1.2
opencv_python==3.4.4.19
PyQt5==5.11.3
```

### Installing
__1.-__ First, install all dependencies if needed. 

>**Note:** You can probably create a virtual environment that includes all the following packages

In ubuntu:

```
pip install numpy==1.15.1 matplotlib==3.0.0 pyexcel==0.5.9.1 Pillow==5.3.0 pyscreenshot==0.4.2 XlsxWriter==1.1.2 opencv_python==3.4.4.19 PyQt5==5.11.3 pyexcel-xlsx
```
__2.-__ After finishing the installation of all dependencies, copy or clone all of the included files in this repository into one folder, `check_dict.py, excel.py, input_dialog2.py` and `Plot_digitizer.py`. The latter will be the one which you will be executing as *`python Plot_digitizer.py`* on your command window. 

__3.-__ Run the code as shown bellow and start extracting those points!

```
python ~/Desktop/Folder_with_files/Plot_digitizer.py
```

> **Note:** You have to change `Folder_with_files` to the path where you saved the codes.

If everything has worked out fine, a window of the program should pop up on your screen and should look something like the image bellow

![alt text](https://raw.githubusercontent.com/edghyhdz/plot_digitizer/master/window.jpg)


### The buttons are quite self explanatory, 

* **Create Excel**: this button will, ... well, create an excel where all your extracted points will be saved. This button should be pressed first in order to not have any errors in while using the plot digitizer. You should give the name of the excel, if you press cancel, the code will create a "change_me.xlsx" file.



* **Input Data**, when pressing this button, a window will pop up and 3 input values should be given:
  * **Data points** where you indicate the number of data points to extract (The maximum number able to be introduced is 1000, but this can be changed on the `input_dialog2.py` file.)
  * **Top Value**, which is where you indicate the **`y`** axis top value and finally 
  * **Value** window, where you indicate the top **`x`** value axis.

  > **Note:**  **Top value**, and **Value** windows, assume that you start with a 0 value in both axis.


![alt text](https://raw.githubusercontent.com/edghyhdz/plot_digitizer/master/input_data_points.jpg)
  
* **Crop image**: this button will pop up a picture of your **desktop**, from which you will be able to select the image you want, and then press **`c`** two times in order to crop it and start working with it. If you would like to reselect the image, you should press **`r`** to restart selection of the cropped image.

  * ![alt text](https://raw.githubusercontent.com/edghyhdz/plot_digitizer/master/selection_image.jpg)

    > **Note:** Don't forget to press **"c"** or **"r"** twice to crop or do a reselection respectively of the cropped image!
  
  * Once `c` was pressed, a second window of the cropped image will pop up, where you will first indicate the **`Y`** axis poin (from zero to your top value) followed by indicating your **`X`** points (from zero to your top value). Afterwards, you can start manually marking your points. As seen bellow, were the x and y points are indicated by a white x and the extracted points are marked in red.
  
  
    ![alt text](https://github.com/edghyhdz/plot_digitizer/blob/master/point_selections.jpg)
  
  * Once you have marked the points, close the cropped window followed by the desktop picture. You can check your data either on the created excel file or by pressing the button **Check Dictionary**.


* **Check Dictionary**: When pressing this button, you will be able to select from a list of extracted graphs, the data that you would like to see on your command windows. 
    
    Example:
  
    ```
    
    ****************************************************************************
    ****************************************************************************
    Graph Number: 2

    X value:     [5.769230769230765, 21.978021978021975, 39.560439560439555, 55.769230769230774]
    Y Value:     [0.8636363636363638, 0.8496503496503497, 0.7692307692307694, 0.6328671328671329]


    ****************************************************************************
    ****************************************************************************

    ```
    
* **Check Input Data**:  Will print the current input data that was given.
    
    Example:
  
    ```

    ****************************************************************************
    ****************************************************************************


    Current top Y value:             1.0
    Current top X value :            1000.0
    Current number of data inputs:   4
    Current excel sheet:             test_excel.xlsx


    ****************************************************************************
    ****************************************************************************


    ```


## Authors

* **Edgar Hernandez** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Part of this code were gotten from  [Adrian Rosebrock's](https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/) tutorial, in order to do the cropping of the images.
