# lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jordan Netz
# jnetz#uci.edu
# 56628532
#
# High-level Design

import random

"""
The default numbers here are generally good enough to create a rich tree. 
You can change the constants to smaller values for testing. 
Lower numbers will simplify the results, 
larger numbers will take more time to render and create hundreds of acorns.
"""

MAX_DEPTH = 5
MAX_BRANCHES = 5

def tree_builder(level):
    """
    Recursively builds a tree using nested dictionaries.
    Each branch is named using the 'Level.Branch' naming convention, and branches may contain acorns.
    
    Parameters:
    - level (int): The current depth of the tree.

    Returns:
    - A nested dictionary (dict) representing the tree with potential acorns.
    """
    tree = {}
    num_branches = random.randrange(1, MAX_BRANCHES)  # Determine how many branches at this level

    for i in range(num_branches):
        if level <= MAX_DEPTH:
            # Naming each branch with the 'Level.Branch' format
            branch_name = f"{level}.{i + 1}"
            
            # Randomly place an acorn
            if random.choice([True, False]):
                tree[branch_name] = "Acorn"
            else:
                # Recurse deeper into the tree to create sub-branches
                tree[branch_name] = tree_builder(level + 1)  # Pass i+1 to count branch at next level
    
    return tree

def tree_builder_with_root():
    """
    Builds a tree with an explicit 'Root' node.
    
    Returns:
    - A dictionary (dict) representing the entire tree, starting from the root.
    """
    tree = {"Root": tree_builder(1)}  # Call the original tree_builder for sub-branches
    return tree


def print_nested_dict(d, indent=0):
    """
    Prints a nested dictionary in a structured way with {} format.
    
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

    print(' ' * indent + '}', end='')  # Closing curly brace for the current level


def visualize_tree(tree, indent=0):
    """
    Recursively builds a string that visualizes the tree structure with indentation.
    
    Parameters:
    - tree (dict): The tree to be visualized.
    - indent (int): The current indentation level (used for proper formatting).
    
    Returns:
    - str: A string that visualizes the tree structure.


    """
    """
    Prints a nested dictionary in a structured way with {} format.
    
    Parameters:
    - d (dict): The nested dictionary to be printed.
    - indent (int): The current indentation level (used for proper formatting).
    """
    output = ''
    
    for i, (key, value) in enumerate(tree.items()):
        # Print the key
        output += ' ' * (indent) + f'{key}' + '\n'
        
        if isinstance(value, dict):  # If the value is a dictionary, recurse
            output += visualize_tree(value, indent + 4)
        else:  # If the value is not a dictionary, print the value directly
            output += ' ' * (indent+4) + 'Acorn' + '\n'
        

    return output


def find_acorns(tree, path=""):
    """
    Recursively searches for acorns in the tree and removes them.
    
    Parameters:
    - tree (dict): The tree to search through.
    - path (str): The current path to the node being searched.
    
    Returns:
    - acorn_paths (list): A list of full paths where acorns were found.
    - each path is in the format of "Root -> 1.1 -> 2.4 -> 3.1 -> 4.1"

    TODO: Finish implementation.
    """
    acorn_paths = []
    for i, (key, value) in enumerate(tree.items()):
    # Print the key

            
        if isinstance(value, dict):  # If the value is a dictionary, recurse
            acorn_paths += find_acorns(value, path + f"{key}" + " -> ")
        elif value == "Acorn":  # If the value is not a dictionary, print the value directly
            acorn_paths.append(path + f"{key}")
            tree[key] = {}
        

    return acorn_paths



def main():
    # Create a tree using the new nested dictionary structure
    tree = tree_builder_with_root()

    # printing nested dictionary
    print_nested_dict(tree)

    # Visualize the tree using indentation for clarity
    print("\nHere is the structure of your tree:\n")
    print(visualize_tree(tree))

    # Recursively find all acorns
    acorn_paths = find_acorns(tree)

    # Report the acorn findings
    if acorn_paths:
        acorn_count = len(acorn_paths)
        print(f"\nYou have {acorn_count} acorn{'s' if acorn_count != 1 else ''} on your tree!")
        
        if acorn_count > 0:
            print("They are located on the following branches:")
            for path in acorn_paths:
                print(path)

if __name__ == "__main__":
    print("Welcome to PyAcornFinder! \n")
    main()