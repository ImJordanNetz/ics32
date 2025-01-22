import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility, hide_errors

try:
    from solution import visualize_tree, find_acorns
except Exception as e:
    raise Exception(f'Couldnt import your class Basics from "solution.py", remember to work off of the template. The error is {e}')

import os

import random, copy

# from solution

MAX_DEPTH = 5
MAX_BRANCHES = 5

def tree_builder(level: int, branch_num: int) -> dict:
    """
    Recursively builds a tree using nested dictionaries.
    Each branch is named using the 'Level.Branch' naming convention, and branches may contain acorns.
    
    Parameters:
    - level: The current depth of the tree.
    - branch_num: The branch number at this level.

    Returns:
    - A nested dictionary representing the tree with potential acorns.
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
                tree[branch_name] = tree_builder(level + 1, i + 1)  # Pass i+1 to count branch at next level
    
    return tree

def tree_builder_with_root() -> dict:
    """
    Builds a tree with an explicit 'Root' node.
    
    Returns:
    - A dictionary representing the entire tree, starting from the root.
    """
    tree = {"Root": tree_builder(1, 1)}  # Call the original tree_builder for sub-branches
    return tree

def visualize_tree_soln(tree, indent=0):
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
            tree_str += visualize_tree_soln(value, indent + 4)  # Increase indentation for next level
        else:
            # If the value is not a dictionary (e.g., an Acorn), print the value
            tree_str += ' ' * (indent + 4) + str(value) + "\n"
    
    return tree_str

def find_acorns_soln(tree, path=""):
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
            sub_acorn_paths = find_acorns_soln(value, current_path)
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

    print(' ' * indent + '}', end='')  # Closing curly brace for the current level


class TestBasics(unittest.TestCase):
    def setUp(self):
        pass
    
    # @hide_errors("A hidden test case has failed! )")
    @weight(2)
    def test_case1(self):
        # random.seed(32)
 
        tree = tree_builder_with_root()
        tree2 = copy.deepcopy(tree)

        soln = visualize_tree_soln(tree)
        submission = visualize_tree(tree2)
        print("Testing visualize_tree with a randomly generated tree")
        print_nested_dict(tree)
        print(f"your submission output: {submission}")
        print(f"correct answer: {soln}")
        # self.assertEqual(out, ans)
        self.assertTrue(soln.strip() == submission.strip())
    
    @weight(2)
    def test_case2(self):
        # random.seed(32)  
        tree = tree_builder_with_root()
        tree2 = copy.deepcopy(tree)
        print("Testing find_acorns with a randomly generated tree")
        print_nested_dict(tree)

        soln = find_acorns_soln(tree)
        submission = find_acorns(tree2)

        print(f"your submission output: {submission}")
        print(f"correct answer: {soln}")
        # self.assertEqual(out, ans)
        for elem in soln:
            self.assertTrue(elem in submission)

    @weight(2)
    def test_case3(self):
        # random.seed(1)
        tree = tree_builder_with_root()
        tree2 = copy.deepcopy(tree)

        print("Testing visualize_tree with a randomly generated tree (remove spaces and newlines)")
        print_nested_dict(tree)

        soln = visualize_tree_soln(tree)
        submission = visualize_tree(tree2)

        print(f"your submission output: {submission}")
        print(f"correct answer: {soln}")
        # self.assertEqual(out, ans)
        self.assertTrue(soln.strip(' ').strip('\n') == submission.strip(' ').strip('\n'))

    @weight(1)
    def test_case4(self):
        random.seed(1)
        tree = tree_builder_with_root()
        tree2 = copy.deepcopy(tree)

        print("Testing visualize_tree with a randomly generated tree (exact match)")
        print_nested_dict(tree)

        soln = visualize_tree_soln(tree)
        submission = visualize_tree(tree2)

        print(f"your submission output: {submission}")
        print(f"correct answer: {soln}")
        # self.assertEqual(out, ans)
        self.assertTrue(soln.strip() == submission.strip())
    
    @weight(1)
    def test_case5(self):
        random.seed(1)
        tree = tree_builder_with_root()
        tree2 = copy.deepcopy(tree)

        print("Testing find_acorns with a randomly generated tree (all submitted paths are in solution)")
        print_nested_dict(tree)

        soln = find_acorns_soln(tree)
        submission = find_acorns(tree2)

        print(f"your submission output: {submission}")
        print(f"correct answer: {soln}")
        # self.assertEqual(out, ans)
        for elem in submission:
            self.assertTrue(elem in soln)

    @weight(1)
    def test_case6(self):
        # random.seed(1)
        tree = tree_builder_with_root()
        # tree2 = copy.deepcopy(tree)
        print("Testing find_acorns to check all acorns are removed after find_acorns is executed.")
        print("Tree before find_acorns: ", tree)
        soln = find_acorns(tree)

        print("Tree after find_acorns: ", tree)
        submission = find_acorns_soln(tree)
      
        self.assertTrue(submission == [])

    @weight(1)
    def test_case7(self):
        random.seed(1)
        tree = tree_builder_with_root()
        tree2 = copy.deepcopy(tree)

        print("Testing find_acorns with a randomly generated tree (all paths match)")
        print("Tree before find_acorns: ", tree)

        soln = find_acorns_soln(tree)
        submission = find_acorns(tree2)

        print(f"your submission output: {submission}")
        print(f"correct answer: {soln}")
        # self.assertEqual(out, ans)
        for elem in soln:
            self.assertTrue(elem in submission)
        self.assertTrue(len(soln) == len(submission))
        # self.assertTrue(soln.strip() == submission.strip())

    # # @hide_errors("A hidden test case has failed! (core functionality)")
    # @weight(1)
    # def test_case2(self):
    #     msg, running = pycalc('3','2',"x", "pycalc.txt")
    #     ans = "3 x 2 = 6"
    #     print(f"your submission output: {msg}")
    #     print(f"correct answer: {ans}")
    #     self.assertTrue(ans.strip() in msg.strip())

    # @weight(1)
    # def test_case3(self):
    #     msg, running = pycalc('5','4',"*", "pycalc.txt")
    #     ans = "Invalid operator! Please use one of the following: +, -, x, /, or q."
    #     print(f"your submission output: {msg}")
    #     print(f"correct answer: {ans}")
    #     self.assertTrue(ans.strip() in msg.strip())

    # @hide_errors("A hidden test case has failed! (ZeroDivisionError handling)")
    # @weight(2)
    # def test_case4(self):
    #     msg, running = pycalc('5','0',"/", "pycalc.txt")
    #     ans = "ZeroDivisionError"
    #     # print(f"msg: {msg}")
    #     # print(f"ans: {ans}")
    #     # self.assertEqual(out, ans)
    #     self.assertTrue(ans.strip() in msg.strip())

    # @hide_errors("A hidden test case has failed! (ValueError handling)")
    # @weight(2)
    # def test_case5(self):
    #     msg, running = pycalc('5.0','2',"/", "pycalc.txt")
    #     ans = "ValueError"
    #     self.assertTrue(ans.strip() in msg.strip())

    # @hide_errors("A hidden test case has failed! (Incorrect output in txt file)")
    # @weight(1)
    # def test_case6(self):
    #     soln_path = Path("answer.txt")
    #     answer_path = Path("pycalc.txt")
    #     soln_file = soln_path.open('r')
    #     answer_file = answer_path.open('r')

    #     soln = soln_file.read()
    #     answer = answer_file.read()
    #     self.assertTrue(soln.strip() == answer.strip())
    #     soln_file.close()
    #     answer_file.close()

    # @hide_errors("A hidden test case has failed! (IOError handling)")
    # @weight(2)
    # def test_case7(self):
    #     msg, running = pycalc("5","4","/","")
    #     ans = "5 / 4 = 1.25\nIOError"
    #     # print(f"msg: {msg}")
    #     # print(f"ans: {ans}")
    #     self.assertTrue(ans.strip() in msg.strip())
    # # @hide_errors("A hidden test case has failed! (edge case)")


if __name__ == '__main__':
    unittest.main()
