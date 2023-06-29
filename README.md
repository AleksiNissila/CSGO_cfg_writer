CSGO_cfg_writer

This is a script for editing the autoexec -file for CS:GO. 
Input CS:GO console commands you wish to edit. The script searches them from the autoexec -file and edits them to correspond the values inputted. 
Note: You need to have the autoexec -file already setup for this to work (atleast in the current state of this script)

### Before using
Set your CS:GO config file location at the start of the script inside the apostrophes. The row looks like: **path = r''** 
For example, the row could look something like this: path = r'C:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg'
This of course depends on where you have installed CS:GO.

### How to use
Run the script, and if you have set the path to your config location correctly, the script asks you for CS:GO commands to input.
Input commands in the same way as you would into the CS:GO console, for example: cl_crosshairstyle 1
You can input multiple commands at the same time by dividing them with a ';', for example: cl_crosshairstyle 1;cl_crosshaircolor 5
If the commands are found in the autoexec -file, they are updated with the values given as the inputs.

### Why?
Just because I was too lazy to search and edit the autoexec manually every time I want to edit my config file.
