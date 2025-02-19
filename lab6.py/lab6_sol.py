import unittest

try:
    from lab6 import Bookmarker
    # from solution import Bookmarker
    from note import Note
    # from solution import Bookmarker as Bookmarker_soln
    # from note_soln import Note as Note_soln

except Exception as e:
    raise Exception(f'Couldnt import your class Bookmarker from "lab6.py", remember to work off of the template. The error is {e}')

import os

import random, copy

from pathlib import Path


import webbrowser 

BOOKMARK_PATH = "."
BOOKMARK_FILE = "pybookmark.txt"

class TestBasics(unittest.TestCase):
    def setUp(self):
        pass

    #weight(1)
    def test_case1(self):
        print("Testing constructor")
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)
        self.assertTrue(bm)

    #weight(1)
    def test_case2(self):
        print("Testing constructor - checking all_notes instance variable")
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)
        bm_soln = Bookmarker_soln(p)

        print(f"out: {bm.all_notes}")
        print(f"ans: {bm_soln.all_notes}")
        self.assertTrue(len(bm.all_notes) == len(bm_soln.all_notes))
        for elem in bm.all_notes:
            self.assertTrue(elem in bm_soln.all_notes)

    #weight(2)
    def test_case3(self):
        print("Testing add with valid URL http://test32")
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)

        test_url = "http://test32"

        bm.add(test_url)

        bm_soln = Bookmarker_soln(p)
        test_url = test_url + "\n"
        print(f"out: {bm.all_notes}")
        # print(bm_soln.all_notes)
        self.assertTrue(test_url in bm.all_notes)

    #weight(2)
    def test_case4(self):
        print("Testing add with invalid URL test8000 - ValueError should be raised")
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)

        error = False
        
        test_url = "test8000"
        try:
            bm.add(test_url)
        except ValueError:
            error = True


        bm_soln = Bookmarker_soln(p)

        self.assertTrue(test_url not in bm_soln.all_notes and error)

    #weight(1.5)
    def test_case5(self):
        print("Testing remove_by_url with http://test32 as input")
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)
        
        print(f"Before remove all_notes: {bm.all_notes}")
        test_url = "http://test32\n"


        bm.remove_by_url(test_url)
        bm._save_notes()

        bm_soln = Bookmarker_soln(p)
        # print(f"After remove bm .all_notes: {bm.all_notes}")
        print(f"After remove all_notes: {bm_soln.all_notes}")

        self.assertTrue(test_url not in bm_soln.all_notes)

    #weight(1.5)
    def test_case6(self):
        print("Testing open with index 0, should return correct URL")
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)

        result = bm.open(0)
        print(f"Return value from calling open(0): {result}",flush=True)
        # self.assertTrue(result == "https://drive.google.com/drive/folders/1AX2LTqH89T-l_FoIVamXni17alGd8-o6")
        self.assertTrue("https://drive.google.com/drive/folders/1AX2LTqH89T-l_FoIVamXni17alGd8-o6" in result)

    # @weight(2)
    def test_add_calls_parent(self):
        # Test that the add method calls the parent's save_note method
        # Since we cannot directly test if the parent's method is called,
        # we can check if the all_notes list is updated correctly
        url = 'http://example.com'
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)

        bm.add(url)
        self.assertEqual(bm.all_notes, [url + '\n'])
    
    # @weight(2)
    def test_inheritance(self):
            # print("Testing open with index 0, should return correct URL")
        p = Path(BOOKMARK_PATH) / BOOKMARK_FILE
        bm = Bookmarker(p)

        self.assertTrue(isinstance(bm, Note))


if __name__ == '__main__':
    unittest.main()

    