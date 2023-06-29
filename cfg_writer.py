import re
from pathlib import Path

# SET YOUR CONFIG FILE LOCATION HERE INSIDE APOSHTROPHES
# THIS FILE LOCATION COULD LOOK SOMETHING LIKE:
# C:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg
# WHICH MEANS THE WHOLE ROW SHOULD LOOK SOMETHING LIKE:
# path = r'C:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg'
path = r''

def process_input_commands(config_file_path, temp_file_path, input_cmd_full):
    input_cmd_full = input_cmd_full.lower()
    input_split = re.findall(r"(\w+)\s+(-?\w+)", input_cmd_full)
    input_cmds, input_values = zip(*input_split)

    num_changed = 0
    val_not_changed = 0

    with open(config_file_path, 'r') as config, open(str(temp_file_path), 'w') as cfg_out:
        for line_number, line in enumerate(config, 1):
            if line.strip():
                command = line.lower().split()[0]
                if command in input_cmds:
                    cmd_i = input_cmds.index(command)
                    if line.lower().split()[1] != input_values[cmd_i]:
                        line_old = line
                        line = f"{input_cmds[cmd_i]} {input_values[cmd_i]}\n"
                        print('Line Number:', line_number)
                        print(f"{line_old.strip()} changed to -> {line.strip()}\n")

                    else:
                        val_not_changed += 1
                    num_changed += 1

            cfg_out.write(line)

    if num_changed == 0:
        print("No matches found")
    if val_not_changed != 0:
        print("Some commands were found, but no changes were made")

def main():
    cfg_loc = Path(path)
    if str(cfg_loc) == '.':
        print("Please set path before proceeding")
        exit()
    config_file_path = cfg_loc / 'autoexec.cfg'
    temp_file_path = cfg_loc / 'autoexec_temp.cfg'

    print("When inputting multiple commands, include ';' between each command")
    print("e.g., cl_crosshairstyle 5; cl_crosshaircolor 3; cl_crosshairgap -2")
    print("Enter 'q' to quit\n")

    while True:
        input_cmd_full = input("Enter CS:GO console command(s): ")
        if input_cmd_full == 'q':
            break
        process_input_commands(config_file_path, temp_file_path, input_cmd_full)

        # Rename files
        backup_file_path = cfg_loc / 'autoexec_old.cfg'
        temp_file_path = cfg_loc / 'autoexec_temp.cfg'

        try:
            config_file_path.rename(backup_file_path)  # Backup the original file
            temp_file_path.rename(config_file_path)  # Rename the temporary file
            backup_file_path.unlink()  # Delete the backup file
            print("Configuration file updated successfully!")
        except Exception as e:
            print(f"Error occurred during file operations: {str(e)}")

if __name__ == '__main__':
    main()
