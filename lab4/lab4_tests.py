import unittest
try:
    from lab4 import is_int, remove_note, save_note
except Exception as e:
    raise Exception(f'Couldnt import your class Basics from "solution.py", remember to work off of the template. The error is {e}')

import os

import random, copy

from pathlib import Path

# from solution

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def remove_note_soln() -> str:
    p = Path(NOTES_PATH) / NOTES_FILE

    # check if storage file exists, if not return.
    if not p.exists():
        # fix
        raise FileNotFoundError
        # return
    
    print("Here are your notes: \n")
    # open and write user note to file

    # fix to assertion error
    if not p.exists():
        raise FileNotFoundError
    
    f = p.open()
    id = 1
    lines = []

    # print each note with an id and store each line in a list
    for line in f:
        lines.append(line)
        print(f"{id}: {line}")
        id = id+1
    f.close()

    remove_id = input("Enter the number of the note you would like to remove: ")
    
    if not is_int(remove_id):
        print ("Not a valid number, cancelling operation.")
        return ""

    # open as write to overwrite existing notes, add notes back while skipping user selection 
    f = p.open('w')
    id = 1
    removed_note = ""

    for line in lines:
        if id == int(remove_id):
            removed_note = line
        else:
            f.write(line)
        id = id+1
    f.close()

    return removed_note

def test_no_file_soln():
    p = Path(NOTES_PATH) / NOTES_FILE
    # if p.exists():
    #     p.unlink()  # Delete the file if it exists
    try:
        remove_note()
        assert False, "Expected FileNotFoundError when file does not exist"
    except FileNotFoundError:
        pass  # This is expected


class TestBasics(unittest.TestCase):
    def setUp(self):
        pass
    
    # #hide_errors("A hidden test case has failed! )")
    #weight(1.25)
    def test_case1(self):
        '''is_int("234")'''
        print(f"your submission output: {is_int('234')}")
        print(f"correct answer: True")
        self.assertTrue(is_int("234") == True)

    #weight(1.25)
    def test_case2(self):
        print("is_int('')")
        print(f"your submission output: {is_int('')}")
        print(f"correct answer: False")
        self.assertTrue(is_int("") == False)    

    #weight(1.25)
    def test_case3(self):
        print("is_int('True')")
        self.assertTrue(is_int("True") == False)    

    #weight(1.25)
    def test_case4(self):
        print("is_int('124.3')")
        self.assertTrue(is_int("124.3") == False)    

    #weight(1)
    def test_case5(self):
        print("is_int(234)")
        self.assertTrue(is_int(234) == True)  

    #weight(1)
    def test_case6(self):
        print("is_int(11.1)")
        self.assertTrue(is_int(11.1) == False)  

    #weight(1)
    def test_case7(self):
        print("is_int(True)")
        self.assertTrue(is_int(True) == False)  


    #weight(2)
    def test_case8(self):
        print("Testing remove_note() without existing pynote.txt file")
        try:
            remove_note()
            print("FileNotFoundError is not raised when deleting from file which does not exist")
            self.assertTrue(False)
        except FileNotFoundError:
            pass  # This is expected
            self.assertTrue(True)  
 
if __name__ == '__main__':
    unittest.main()

