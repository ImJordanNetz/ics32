import unittest
try:
    from note import Note
    from note_soln import Note as Note_soln

except Exception as e:
    raise Exception(f'Couldnt import your class Note from "note.py", remember to work off of the template. The error is {e}')

import os

import random, copy

from pathlib import Path


NOTES_PATH = "."
NOTES_FILE = "pynote.txt"
NOTES_FILE2 = "pynote2.txt"

class TestBasics(unittest.TestCase):
    def setUp(self):
        pass
    
    # @weight(2)
    def test_case1(self):
        print("Testing constructor is creating a Note object")
        p = Path(NOTES_PATH) / NOTES_FILE
        note = Note(p)
        self.assertTrue(note)
        self.assertTrue(type(note)==Note)

    # @weight(2)
    def test_case2(self):
        print("Testing read_notes()")
        p = Path(NOTES_PATH) / NOTES_FILE
        note = Note(p)
        out = note.read_notes()

        note_ans = Note_soln(p)
        ans = note_ans.read_notes()
        
        print(f"out: {out}")
        print(f"ans: {ans}")

        for elem in ans:
            self.assertTrue(elem in out)
          

    # @weight(2)
    def test_case3(self):
        print("Testing save_notes()")
        p = Path(NOTES_PATH) / NOTES_FILE
        note = Note(p)
        user_input = "new line"
        out = note.read_notes()
        # print(f"out: {out}")

        note.save_note(user_input)

        p2 = Path(NOTES_PATH) / NOTES_FILE2
        note_ans = Note_soln(p2)
        note_ans.save_note(user_input)
        
        out = note.read_notes()
        ans = note_ans.read_notes()
        
        print(f"out: {out}")
        print(f"ans: {ans}")

        for elem in ans:
            self.assertTrue(elem in out)

    # @weight(2)
    def test_case4(self):
        print("Testing remove_note()")
        p = Path(NOTES_PATH) / NOTES_FILE
        note = Note(p)
        user_input = int("6")
        note.remove_note(user_input)

        p2 = Path(NOTES_PATH) / NOTES_FILE2
        note_ans = Note_soln(p2)
        note_ans.remove_note(user_input)
        
        out = note.read_notes()
        ans = note_ans.read_notes()
        
        print(f"out: {out}")
        print(f"ans: {ans}")

        for elem in ans:
            self.assertTrue(elem in out)

    # @weight(2)
    # def test_case5(self):
    #     print("Testing printing of Note objects")
    #     p = Path("/test/test_folder") / NOTES_FILE
    #     note = Note(p)
    #     print_text = f'{note}'
    #     ans_text = "/test/test_folder/pynote.txt"

    #     print(f"out: {print_text}")
    #     print(f"ans: {ans_text}")

    #     self.assertTrue(ans_text in print_text)



if __name__ == '__main__':
    unittest.main()