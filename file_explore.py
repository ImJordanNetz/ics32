def lookup():
    p = Path(".")
    output = ""
    
    if p.exists() and p.is_dir():
        items = list(p.iterdir())
    else:
        return "ERROR: Invalid Pathcat .\n"
    
    
    files = [item for item in items if item.is_file()]
        
    
    files.sort()
    
    for file in files:
        output += str(file) + '\n'
    

    
    directories = sorted([item for item in items if item.is_dir()])
    
    for directory in directories:
            output += str(directory) + '\n'
    
    for directory in directories:
        output += ls(options, str(directory), options_input)


    
    return output