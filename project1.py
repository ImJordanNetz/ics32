# project1.py
#
# ICS 32 Fall 2024
# Project #1: File System Explorer
# 
# NAME: Jordan Netz
# EMAIL: jnetz#uci.edu
# STUDENT ID: 56628532
#
# High-level Design:
# 

from pathlib import Path
from sys import exit
# These string constants are provided to avoid typo errors for the man command.
# Each constant holds one line of text. 
# These can be concatenated to create the correct man directions.

GENERIC1 = "The File System Explorer supports this command in the following format/s:\n"
GENERIC2 = "[COMMAND]\n"
GENERIC3 = "[COMMAND] [INPUT]\n"
GENERIC4 = "[COMMAND] [-OPTIONS] [INPUT]\n"
GENERIC5 = "[COMMAND] [-OPTIONS] [INPUT] [OPTION_INPUT]\n"
GENERIC6 = "The [INPUT] corresponds to the [COMMAND].\n"
GENERIC7 = "The [OPTIONAL_INPUT] corresponds to [-OPTIONS].\n"
LS_DIR = "ls is a command that lists the contents of a directory. [INPUT] is the path.\n"
LS_DIR2 = "ls options include -r, -f, -s, -e, -g and -l.\n"
LS_DIR3 = "-r = recursive, -f file only, -s match specific file name, -e match specific extension.\n"
LS_DIR4 = "-g and -l prints only files with size greater (g) or less (l) than [OPTION_INPUT].\n"
CAT_DIR = "cat is a command that prints the contents of a file. [INPUT] is the file path.\n"
CAT_DIR2 = "cat options include -f and -d.\n"
CAT_DIR3 = "-f = prints the first line only, -d duplicates the file into filename.dup.\n"
MAN_DIR = "man is a command that prints the directions for the command. [INPUT] is the command.\n"
Q_DIR = "q is a command that quits the file system explorer.\n"

def man(options, command_input, options_input):
    if len(options) != 0:
        return "ERROR: Invalid Format.\n"
    if len(options_input) != 0:
        return "ERROR: Invalid Format.\n"
    
    
    command_desc = {
    "man": GENERIC1 + GENERIC3 + MAN_DIR,
    
    "q": GENERIC1 + GENERIC2 + Q_DIR,
    
    "cat": GENERIC1 + GENERIC3 + GENERIC4 + GENERIC6 + CAT_DIR + CAT_DIR2 + CAT_DIR3,
    
    "ls": GENERIC1 + GENERIC3 + GENERIC4 + GENERIC5 + GENERIC6 + GENERIC7 + LS_DIR + LS_DIR2 + LS_DIR3 + LS_DIR4
}
    
    if command_input in command_desc:
        return command_desc[command_input]
    else:
        return "ERROR: Invalid Command.\n"


def ls(options, command_input, options_input):
    
    if len(command_input) == 0:
        return "ERROR: Invalid Format.\n"
    if len(options) == 0 and len(options_input) != 0:
        return "ERROR: Invalid Format.\n"
    
    exclusive_options = options.intersection(set("segl"))
    
    if len(exclusive_options) > 1:
        return "ERROR: Invalid Format.\n"
    if len(exclusive_options) == 1 and len(options_input) == 0:
        return "ERROR: Invalid Format.\n"
    
    
    exclusive_option = ''
    if len(exclusive_options) == 1:
        exclusive_option = list(exclusive_options)[0]
        
    
    p = Path(command_input)
    output = ""
    
    if p.exists() and p.is_dir():
        items = list(p.iterdir())
    else:
        return "ERROR: Invalid Pathcat .\n"
    
    
    if exclusive_option == '':
        files = [item for item in items if item.is_file()]
        
    elif exclusive_option == 's':
        files = [item for item in items if item.is_file() and options_input in item.name]
    
    elif exclusive_option == 'e':
        files = [item for item in items if item.is_file() and any(options_input in suffix for suffix in item.suffixes)]
    
    elif exclusive_option == 'g':
        if options_input.isdigit():
            files = [item for item in items if item.is_file() and item.stat().st_size > int(options_input)]        
        else:
            return "ERROR: Invalid Format.\n"
        
    elif exclusive_option == 'l':
        if options_input.isdigit():
            files = [item for item in items if item.is_file() and item.stat().st_size < int(options_input)]        
        else:
            return "ERROR: Invalid Format.\n"
    else:
        return "ERROR: Invalid Format.\n"
    
    files.sort()
    
    for file in files:
        output += str(file) + '\n'
    

    
    directories = sorted([item for item in items if item.is_dir()])
    
    for directory in directories:
        if len(exclusive_option) == 0 and "f" not in options:
            output += str(directory) + '\n'
            
    
    
    for directory in directories:
        if 'r' in options:
            output += ls(options, str(directory), options_input)


    
    return output
    
    

def cat(options, command_input, options_input):
    if len(options_input) != 0:
        return "ERROR: Invalid Format.\n"
    if len(command_input) == 0:
        return "ERROR: Invalid Format.\n" 
    if len(options) > 1:
        return "ERROR: Invalid Format.\n" 

    
    try:
        p = Path(command_input)
        
        if not p.is_file():
            return "ERROR: Invalid Path.\n" 
        
        
        if 'd' in options:
                duplicate = Path(str(p) + '.dup')
                content = p.read_bytes()
                duplicate.write_bytes(content)
                return ''
        else:
            with p.open() as file:
                if 'f' in options:
                    text = file.readline()
                else:
                    text = file.read()

            
        
            return text + '\n'
    except (OSError, PermissionError) as e:
        return "ERROR: Invalid Path.\n"

def q(options, command_input, options_input):
    if len(options) != 0:
        return "ERROR: Invalid Format.\n"
    if len(command_input) != 0:
        return "ERROR: Invalid Format.\n"
    if len(options_input) != 0:
        return "ERROR: Invalid Format.\n"
    
    return "quit"

def parse_command(user_input):
    user_input_split = user_input.split()
    
    command = ""
    options = set()
    command_input = ""
    options_input = ""
    
    if len(user_input_split) == 0 or len(user_input_split) > 4:
        return "ERROR: Invalid Command.\n"
    
    
    try:
        command = user_input_split[0]
        if len(user_input_split) > 1:
            if user_input_split[1][0] == '-':
                options = set(user_input_split[1][1:])
                command_input = user_input_split[2]
                if len(user_input_split) == 4:
                    options_input = user_input_split[3]
            else:
                command_input = user_input_split[1]
                if len(user_input_split) > 2:
                    return "ERROR: Invalid Format.\n"
                    
    except:
        return "ERROR: Invalid Format.\n"
        
    
    
    if command == "q":
        return q(options, command_input, options_input)
    elif command == "man":
        return man(options, command_input, options_input)
    elif command == "ls":
        return ls(options, command_input, options_input)
    elif command == "cat":
        return cat(options, command_input, options_input)
    else:
        return "ERROR: Invalid Command.\n"

def main() -> None:
    while True:
        user_input = input()
        value = parse_command(user_input)
        if (value == "quit"):
            exit()
        else:
            print(value, end="")

if __name__ == '__main__':
    main()