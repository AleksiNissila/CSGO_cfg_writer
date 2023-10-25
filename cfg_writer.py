import re
from pathlib import Path
import json
import tkinter as tk
import gui

# Get list of commands as a global variable
with open("cmds.txt", "r") as cmds:
    cmd_list = sorted(set(cmd.strip() for cmd in cmds))
    cmds.close()
def init_path():
    """
    Function to get path from config.json
    :return: String containing path got from config.json
    """
    with open("config.json", "r") as cfg:
        data = json.load(cfg)
        path = str(data["path"])
        cfg.close()
        return path


def update_path(new_path):
    """
    Edit config.json file if config location is edited by user
    :param new_path: path to new location
    :return: nothing
    """
    with open("config.json", "r") as cfg:
        data = json.load(cfg)
        data["path"] = new_path

    with open("config.json", "w") as cfg:
        json.dump(data, cfg, indent=4)

def update_cmd_list(cmds, app):
    """
    Function for adding new commands to cmds.txt
    :param cmd: command to be added to the list
    :return: nothing
    """
    for cmd in cmds:
        if cmd not in cmd_list:
            with open("cmds.txt", "a+") as cmds:
                cmds.write("\n" + cmd)
            cmd_list.append(cmd)
            print("command added to file")
            app.update_cmd_combobox()
            # Sort the file if new commands get added
            sort_cmds()
        else:
            print("command exists in file")
    app.update_cmd_combobox()

def get_cmd_list():
    """
    Function for initializing the commands from text file
    :return: List of commands that exist in cmds.txt
    """
    with open("cmds.txt", "r") as cmds:
        cmd_list = set(cmd.strip() for cmd in cmds)
    return cmd_list

def process_input_commands(config_file_path, input_cmd_full, info_box, app):
    """
    Main function that writes the changes to the config file.
    :param config_file_path: Path to the config file that is to be edited
    :param input_cmd_full: Users input. Can be one command + value, or multiple commands
    and values separated by ';'
    :param info_box: GUI element into which information about changes is written for the user
    :param app: Tkinter app
    :return: nothing
    """

    # initiate file locations
    cfg_loc = Path(config_file_path)
    config_file_path = cfg_loc / 'autoexec.cfg'
    temp_file_path = cfg_loc / 'autoexec_temp.cfg'

    # split user input(s) to commands and values
    input_cmd_full = input_cmd_full.lower()
    input_split = re.findall(r"(\w+)\s+(-?\w+(?:\.\w+)?)", input_cmd_full)
    print(input_split)
    try:
        input_cmds, input_values = zip(*input_split)
    except:
        print_info("Bad input", info_box)
        return


    num_changed = 0
    val_not_changed = 0

    # Edit configuration file
    with open(config_file_path, 'r') as config, open(str(temp_file_path), 'w') as cfg_out:
        for line_number, line in enumerate(config, 1):
            if line.strip():
                # Check if line in cfg file corresponds to user inputted command
                command = line.lower().split()[0]
                if command in input_cmds:
                    cmd_i = input_cmds.index(command)
                    # If command is found in the file
                    # Edit cfg file to new value
                    if line.lower().split()[1] != input_values[cmd_i]:
                        line_old = line
                        line = f"{input_cmds[cmd_i]} {input_values[cmd_i]}\n"
                        msg = 'Line Number: ' + str(line_number)
                        print_info(msg, info_box)
                        print_info(f"{line_old.strip()} changed to -> {line.strip()}\n", info_box)
                        update_cmd_list(input_cmds, app)

                    else:
                        val_not_changed += 1
                    num_changed += 1

            cfg_out.write(line)

    if num_changed == 0:
        print_info("No matches found", info_box)
    if val_not_changed != 0:
        print_info("Some commands were found, but no changes were made", info_box)

    # Rename files
    backup_file_path = cfg_loc / 'autoexec_old.cfg'
    temp_file_path = cfg_loc / 'autoexec_temp.cfg'

    try:
        # Backup the original file
        config_file_path.rename(backup_file_path)
        # Rename the temporary file
        temp_file_path.rename(config_file_path)
        # Delete the backup file
        backup_file_path.unlink()
        print_info("Configuration file updated successfully!", info_box)
    except Exception as e:
        print_info(f"Error occurred during file operations: {str(e)}", info_box)




def print_info(msg, info_box):
    """
    Print information about the changes made for the user
    :param msg: Message to be printed
    :param info_box: GUI element to which message is printed to
    :return: nothing
    """
    info_box.insert(tk.END, msg + '\n', 'black')
    info_box.see('end')

def sort_cmds():
    """
    Function for sorting the commands in cmds.txt to alphabetical order
    :return: nothing
    """
    rows = []
    with open("cmds.txt", 'r') as file:
        for line in file:
            stripped = line.strip('\n')
            rows.append(stripped)
    file.close()
    rows.sort()


    with open("cmds.txt", 'w') as file:
        for cmd in rows[1:]:
            file.write(cmd + '\n')
    file.close()


def main():
    path = init_path()
    root = tk.Tk()
    app = gui.Gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
