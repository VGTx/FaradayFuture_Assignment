This problem has been solved by the use of 3 classes - 

1. Model - This class loads the data from the JSON file and stores it in a Dictionary in the appropriate format.The Keys for this Dictionary are the City Names and the Data Values are a Tuple made up of the required data fields for the GUI

2. View - This class defines the GUI elements for the program using wxPython. This is the only external requirement for the program to run.

3. Controller - This class controls the overall interaction between the Model and the View components of the program.

The Launcher file is used to Launch the GUI for the program with all the background functionality in place.

##########################################################################################################################################################

Instructions to run the program - 

 - Run the Launcher.py file
 - Start entering the characters of the desired City's name
 - Press the button for the drop down list or the down arrow for the suggested values corresponding to the input provided so far
 - For Cities with null data fields for County name, Latitude or Longitude, a warning message shows up to highlight the missing data field

##########################################################################################################################################################

External Requirements - 

 - wxPython version 4.01

