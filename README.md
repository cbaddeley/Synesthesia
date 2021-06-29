<img src="https://github.com/cbaddeley/Synesthesia/blob/main/src/synesthesia/images/git_main_logo.png" width="500"/>
Synesthesia is a lightweight audio visualization tool. Simply select an MP3 or WAV file, modify any parameters, and Synesthesia will create an image based on the mood, rhythm, and melody of your audio file.

## Instructions ##
1. Once running the application, use the file picker ("Choose..." button) or enter a file path to a MP3 or WAV audio file. 
2. Choose the desired algorithm from the algorithm combo box.
    - <ins>Shape of You</ins>: Draw a collection of shapes based on notes and octaves.
    - <ins>Line Rider</ins>: Draws a collection of lines based on notes and octaves.
    - <ins>Curvy</ins>: Draws a collection of arcs based on notes and octaves.
3. Use the sliders to adjust the parameters of the processed audio file.
    - <ins>Sample Rate</ins>: Determines the number of samples taken per second of audio.
      - Higher SR = more notes, longer processing.
    - <ins>Frequency</ins>: Increases or decreases the frequency by a given percentage leading to a alteration of the shapes, line, etc. depending on the chosen algorithm.
    - <ins>Octave</ins>: Changes the octaves by the selected amount which impact the size of the shapes, lines, etc. in the resulting image.
4. Select the "Process" button to digest the audio file apply any adjustments and create the artistic rendering of the audio.

## pip Installation ## 
_Note: The pip package may not be as current as the code on Github._

To install Synesthesia, enter an Ubuntu based terminal and run the command `pip install synesthesia-uf` or `pip3 install synesthesia-uf` depending on your python instillation.

## Local build/installation
If you want to build it locally, simply extract the tar and enter the "src" folder. From that folder, run command "make build" in the terminal to install and then


## Dependencies ## 
_Note: All dependencies are included in the "install_requires" part of the setup.py file and should be installed when you run the application._

Dependencies include: PyQt5, librosa, essentia, and musicnn.

## Program Execution ##
To run Synesthesia after installing, enter an Ubuntu based terminal and run the command `syne`. After installing any dependencies, the application will be launched.

## Github Repository ##
https://github.com/cbaddeley/Synesthesia

## Trello ##
https://trello.com/b/VGXHTDLq/synesthesia


## Team Members ##
Cory Baddeley, Scott Engelhardt, Drew Garmon, George Kolasa, Zack Simmons

