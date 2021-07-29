<img src="https://github.com/cbaddeley/Synesthesia/blob/main/src/synesthesia/images/git_main_logo.png" width="500"/>
Synesthesia is a lightweight audio visualization tool. Simply select an MP3 or WAV file, modify any parameters, and Synesthesia will create an image based on the mood, rhythm, and melody of your audio file.

## Instructions ##
1. Once running the application, use the file picker ("Choose..." button) or enter a file path to a MP3 or WAV audio file. Or use the Sample dropdown to choose an existing processed song along with it's specifications.
2. Choose the desired algorithm from the algorithm combo box.
    - <ins>Shape of You</ins>: Draw a collection of shapes based on notes and octaves.
    - <ins>Line Rider</ins>: Draws a collection of lines based on notes and octaves.
    - <ins>Curvy</ins>: Draws a collection of arcs based on notes and octaves.
    - <ins>Grid</ins>: Draws a grid based on notes.
    - <ins>Speech</ins>:  Draws a word map based on the most common words in the selected speech.
3. Use the sliders to adjust the parameters of the processed audio file.
    - <ins>Frequency</ins>: Increases or decreases the frequencies of the provided audio file by the percent selected.
    - <ins>Sample Rate</ins>: Determines the number of samples taken per second of audio. The larger the sample rate the increased processing time.
    - <ins>Octave</ins>: Increases or decreases the octaves by the number selected which changes the octaves by the selected amount which impact the size of the shapes, lines, etc. in the resulting image.
4. Select the "Process" button to digest the audio file apply any adjustments and create the artistic rendering of the audio.
    - This can be stopped at any time by pressing the Cancel button.
    - If the audio file selected is corrupt, you will see an error on the audio processing.
5. Right click the image to perform a save as of the generated image.
    - This is not an option for the Speech algorithm, since the image is stored as a png file where the audio file was selected from.
6. Select the help button in the top right for more information.

## Virtual Environment ##
It is recommended to run the application in a virtual environment. To do so, follow the below instructions. 
  1. Open WSL in the Windows Terminal, Command Prompt or PowerShell
  2. cd into any desired folder.
  3. Run the command `mkdir synesthesia` (folder name is arbitrary).
  4. cd into the folder created above.
  5. Run the command `python -m venv ./` to create the virtual environment (`python3` might be required depending on your install).
  6. Run the command `source ./bin/activate` to activate the virtual environment
  7. Follow the commands in the pip installation

## pip Installation ## 
_Note: The pip package may not be as current as the code on Github._

To install Synesthesia, enter an Ubuntu based terminal and run the command `pip install synesthesia-uf` or `pip3 install synesthesia-uf` depending on your python instillation.

## Local build/installation ##
If you want to build it locally, simply extract the tar and enter the "src" folder. From that folder, run command "make build" in the terminal to install.

## Dependencies ## 
_Note: All dependencies are included in the "install_requires" part of the setup.py file and should be installed when you run the application._

Dependencies include: PyQt5, librosa, essentia, and musicnn.

## Program Execution ##
To run Synesthesia after installing (via pip or local), enter an Ubuntu based terminal and run the command `syne`. After installing any dependencies, the application will be launched.


## Sample Install ## 
It is assumed that a Windows Shell is opened.
`wsl`
`mkdir synesthesia && cd synesthesia && python3 -m venv ./ && source ./bin/activate && pip3 install synesthesia-uf && syne`

## Github Repository ##
https://github.com/cbaddeley/Synesthesia

## Trello ##
https://trello.com/b/VGXHTDLq/synesthesia


## Team Members ##
Cory Baddeley, Scott Engelhardt, Drew Garmon, George Kolasa, Zack Simmons

