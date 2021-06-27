# Synesthesia #
Synesthesia is a lightweight audio visualization tool. Add an MP3 or WAV file and select your parameters, and Synesthesia creates an image based on the mood, rhythm, and melody of your audio file.

## Instructions ##
1. Once running the application, use the file picker ("Choose..." button) or enter a file path to a MP3 or WAV audio file. 
2. Choose the desired algorithm from the algorithm combo box.
  - Shape of You: Draw a collection of shapes based on notes and octaves.
  - Line Rider: Draws a collection of lines based on notes and octaves.
  - /r/curvy: Draws a collection of arcs based on notes and octaves.
3. Use the sliders to adjust the parameters of the processed audio file.
  - Sample Rate: Determines the number of samples taken per second of audio.
    - Higher SR = more notes, longer processing.
  - Frequency: Increases or decreases the frequency by a given percentage leading to a alteration of the shapes, line, etc. depending on the chosen algorithm.
  - Octave: Changes the octaves by the selected amount which impact the size of the shapes, lines, etc. in the resulting image.
4. Select the "Process" button to digest the audio file apply any adjustments and create the artistic rendering of the audio.

## Running it via Pip ## 
_Note: The Pip package may be behind what is currently up here on Github_

**Enter in Linux console:**

pip install synesthesia-uf

syne

## Dependencies ## 
Included in the "install_requires" part of the setup.py file (should be installed when you run "pip install synesthesia-uf") 

Ubuntu (apt) dependencies can be automatically installed by running the program via pip.

## Github Repository ##
![Synesthesia](https://github.com/cbaddeley/Synesthesia/blob/main/synesthesia.png)

## Trello ##
https://trello.com/b/VGXHTDLq/synesthesia
