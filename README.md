Use at your own risk! Still contains a lot of bugs and oversights which could cause your config file unwanted changes.

CSGO_cfg_writer

This is a script for editing the autoexec -file for CS:GO. 
Input CS:GO console commands you wish to edit. The script searches them from the autoexec -file and edits them to correspond the values inputted. 
Note: You need to have the autoexec -file already setup for this to work (atleast in the current state of this script)

### Before using
Select your CS2 config file location at the start of the program. Click "Select file location" -button, and navigate to your CS folder. Select the *folder* which
contains your config-file, do not select the file itself. The location could look romething like this: C:\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg
This location of course depends on where you have installed Steam and CS2.

### How to use
Run the script, and if you have set the path to your config location correctly, the script asks you for CS2 commands to input.
Input commands in the same way as you would into the CS2 console, for example: cl_crosshairstyle 1
You can input multiple commands at the same time by separating them with a ';', for example: cl_crosshairstyle 1;cl_crosshaircolor 5
If the commands are found in the autoexec -file, they are updated with the values given as the inputs.

