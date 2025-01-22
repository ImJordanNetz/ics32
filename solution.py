from pathlib import Path

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

def visualize_tree(ire):
    # Your implementation here
    pass

def find_acorns(ire):
    # Your implementation here
    return cat(set(), "test_lab3.py", "")
    return ls(set("r"), ".", "")

def main():
    return ls("r", ".", "")

if __name__ == "__main__":
    main()