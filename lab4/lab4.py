# lab4.py

# Starter code for lab 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jordan Netz
# jnetz
# 56628532
#
# This program enables a user to input short one line notes and have them stored
# in a file called pynote.txt
#
# Complete the following with True or False
# is_int("123") ==
# is_int("abc") ==
# is_int("12.3") ==
# is_int("") ==
# is_int(123) ==
# is_int(12.3) ==
# is_int(True) ==
# is_int(False) ==


from pathlib import Path

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def is_int(val):
    if isinstance(val, (bool, float)):
        return False
    try:
        int(val)
        return True
    except ValueError:
        return False

def save_note(note: str):
    # create path obj to notes storage file
    p = Path(NOTES_PATH) / NOTES_FILE

    # check if storage file exists, if not create it.
    if not p.exists():
        p.touch(exist_ok=True)
    
    # open and write user note to file
    f = p.open('a')
    f.write(note + '\n')
    f.close()

def read_notes():
    p = Path(NOTES_PATH) / NOTES_FILE
    # check if storage file exists, if not return.
    if not self.p.exists():
        return
    
    print("Here are your notes: \n")
    # open and write user note to file
    f = self.p.open()
    for line in f:
        print(line)
    f.close()

def remove_note(remove_id) 
    p = Path(NOTES_PATH) / NOTES_FILE

    # check if storage file exists, if not return.
    if not p.exists():
        raise FileNotFoundError
        # open and write user note to file
    f = p.open()
    id = 1
    lines = []

    # print each note with an id and store each line in a list
    for line in f:
        lines.append(line)
        id = id+1
    f.close()

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

def test_is_int():
    assert is_int("123") == True
    assert is_int("abc") == False
    assert is_int("12.3") == False
    assert is_int("") == False
    assert is_int(123) == True
    assert is_int(12.3) == False
    assert is_int(True) == False
    assert is_int(False) == False
    

def test_no_file():
    try:
        remove_note()
        assert False, "Expected FileNotFoundError when file does not exist"
    except FileNotFoundError:
        return


def main():
    print("Welcome to PyNote! \n")
    read_notes()

    while True:
        note = input("Please enter a note (enter :d to delete a note or :q to exit):  ")
        if note == ":d":
            note = remove_note()
            print(f"The following note has been removed: \n\n {note}")
        elif note == ":q":
            return
        else:    
            save_note(note)
            

if __name__ == "__main__":
    main()
