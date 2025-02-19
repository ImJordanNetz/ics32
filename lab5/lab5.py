# lab5.py

# Starter code for lab 5 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jordan Netz
# jnetz@uci.edu
# 56628532

# ---------------------------------------------------------------
# Complete your Note class in a file called note.py
# Include the above header in note.py
#
# Do not change any of the provided code in this file
# ---------------------------------------------------------------

from note import Note

from pathlib import Path
NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def print_notes(notes:list[str]):
    id = 0
    for n in notes:
        print(f"{id}: {n}")
        id+=1


def delete_note(note:Note):
    try:
        remove_id = input("Enter the number of the note you would like to remove: ")
        remove_note = note.remove_note(int(remove_id))
        print(f"The following note has been removed: \n\n {remove_note}")
    except FileNotFoundError:
        print("The PyNote.txt file no longer exists")
    except ValueError:
        print("The value you have entered is not a valid integer")

def main():
    p = Path(NOTES_PATH) / NOTES_FILE
    if not p.exists():
        p.touch()
    note = Note(p)
    
    print(f"Here are your notes stored in {note} \n")
    print_notes(note.read_notes())

    user_input = input("Please enter a note (enter :d to delete a note or :q to exit):  ")

    if user_input == ":d":
        delete_note(note)
    elif user_input == ":q":
        return
    else:    
        note.save_note(user_input)
    main()


if __name__ == "__main__":
    print("Welcome to PyNote! \n")

    main()