def visualize_tree(tree, indent=0):
    """
    Recursively builds a string that visualizes the tree structure with indentation.
    
    Parameters:
    - tree (dict): The tree to be visualized.
    - indent (int): The current indentation level (used for proper formatting).
    
    Returns:
    - str: A string that visualizes the tree structure.
    """
    tree_str = ""
    
    for key, value in tree.items():
        # Add the key (node) to the string with indentation
        tree_str += ' ' * indent + str(key) + "\n"
        
        if isinstance(value, dict):  # If the value is another dictionary, recurse
            tree_str += visualize_tree(value, indent + 4)  # Increase indentation for next level
        else:
            # If the value is not a dictionary (e.g., an Acorn), print the value
            tree_str += ' ' * (indent + 4) + str(value) + "\n"
    
    return tree_str

def find_acorns(tree, path=""):
    """
    Recursively searches for acorns in the tree and removes them.
    
    Parameters:
    - tree (dict): The tree to search through.
    - path (str): The current path to the node being searched.
    
    Returns:
    - acorn_paths (list): A list of full paths where acorns were found.

    """
    acorn_paths = []

    
    for key, value in tree.items():
        # Construct the new path to the current node
        
        current_path = f"{path} -> {key}" if path else key  # Avoid adding "->" at root level
        
        if isinstance(value, dict):  # If the value is a dictionary (a branch), recurse into it
            sub_acorn_paths = find_acorns(value, current_path)
            acorn_paths.extend(sub_acorn_paths)  # Collect acorn paths from sub-branches

        elif value == "Acorn":  # If an acorn is found
            acorn_paths.append(current_path)  # Record the path to the acorn
            tree[key] = {}  # Remove the acorn by replacing it with an empty branch

    
    return acorn_paths

def print_nested_dict(d, indent=0):
    """
    Recursively prints a nested dictionary in a structured way with {} format.
    
    Parameters:
    - d (dict): The nested dictionary to be printed.
    - indent (int): The current indentation level (used for proper formatting).
    """
    print(' ' * indent + '{')  # Opening curly brace for the current level
    
    for i, (key, value) in enumerate(d.items()):
        # Print the key
        print(' ' * (indent + 4) + f'"{key}": ', end='')
        
        if isinstance(value, dict):  # If the value is a dictionary, recurse
            print_nested_dict(value, indent + 4)
        else:  # If the value is not a dictionary, print the value directly
            print(f'"{value}"', end='')
        
        # Add a comma after each item, except for the last one
        if i < len(d) - 1:
            print(',')
        else:
            print()

    print(' ' * indent + '}', end='')