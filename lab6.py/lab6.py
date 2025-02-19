# lab6.py

# Starter code for lab 6 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jordan Netz
# jnetz@uci.edu
# 56628532

"""
This program enables a user to input short one line notes and have them stored in a file called pynote.txt

"""
import webbrowser 
from pathlib import Path

BOOKMARK_PATH = "."
BOOKMARK_FILE = "pybookmark.txt"

from note import Note

class Bookmarker(Note):
    
    def __init__(self, p):
        from pathlib import Path 
        super().__init__(p)
    
    def add(self, url:str):
        
        """
        add a url to bookmark

        :param url: a valid url, must begin with http

        :raises ValueError: raised if url parameter does not start with http
        """
        # perform some lightweight validation checking. Note, this is quite simplistic,
        # but reinforces why inheritance can be useful. We are reusing the save_note code, 
        # while introducing custom operations that meet the needs of our program.
        if url.startswith("http"):
            super().save_note(url)
        else:
            raise ValueError("The value assigned to the url parameter is not valid.")
    
    def remove_by_url(self, url:str):
        """
        attempt to remove a url from bookmarks. If bookmark is not found, operation is ignored

        :param url: a valid url, must begin with http
        """
        id = -1

        # attempt to remove by index, if exception, ignore.
        # ignore here is a design decision, but is it the right one? Perhaps a raised ValueError
        # would be more useful, but that would require the calling code to handle the exception.
        # What would you do?
        try:
            id = self.all_notes.index(url)
        except ValueError:
            pass
        else:
            super().remove_note(id)
    
    def remove_by_id(self, url_id:str):
        """
        removes the url in all_notes associated with to the url_id parameter in the local system's default browser

        :param url_id: the index of the url to open
        """

        if self._is_int(url_id):
            id = int(url_id)
            super().remove_note(id)

    def find(self, keyword:str) -> list[str]:
        """
        given a search parameter, attempts to find a list of matching urls.

        :param keyword: the word or words to use for search

        :returns list: a list of url's that contain the words assigned to the keyword param 
        """
        results = [x for x in self.all_notes if keyword in x]
        return results
    
    def open(self, url_id:str):
        """
        opens the url in all_notes associated with to the url_id parameter in the local system's default browser

        :param url_id: the index of the url to open
        """
        if self._is_int(url_id):
            id = int(url_id)
            url = self.all_notes[id].strip()
            
            # Note: you can uncomment "webbrowser.open(url)" and comment out the "return url line" to see it actually open the URL
            # However, make sure to restore the code back for autograder testing

            # webbrowser.open(url)
            return url
        else:
            raise ValueError("The url_id does not match a valid bookmark")

# input/output messages. Keeping them together for easy translation and editing!
INPUT_MAIN_MENU = "What would you like to do? \n 1. Add a bookmark\n 2. Open a bookmark\n 3. View all bookmarks\n 4. Find a bookmark\n 5. Remove a bookmark\n 6. Quit\n"
INPUT_ADD = "Great. What bookmark would you like to add?\n"
INPUT_OPEN = "What bookmark would you like to open (enter item number)?\n"
INPUT_REMOVE = "What bookmark would you like to remove (enter item number)?\n"
INPUT_FIND = "Great. Enter a few words associated with the bookmark you want to find:\n"
MSG_OPEN_MENU = "Here is a list of your current bookmarks:\n"
MSG_EMPTY = "You currently do not have any bookmarks saved.\n"


def print_bookmarks(bookmarks:list):
    print(MSG_OPEN_MENU)
    id = 0
    for b in bookmarks:
        print(f"{id}: {b}")
        id+=1

# abstract exception handling to a single location, keeps menu conditional table clean
def call(func, param):
    try:
        return func(param)
    except Exception as ex:
        print(ex)

def run(bookmarker: Bookmarker):
    if len(bookmarker.all_notes) < 1:
        print(MSG_EMPTY)

    resp = input(INPUT_MAIN_MENU)
    while resp != '6':
        if resp == '1':
           call(bookmarker.add, input(INPUT_ADD))
        elif resp == '2':
            print_bookmarks(bookmarker.all_notes) 
            call(bookmarker.open, input(INPUT_OPEN))
        elif resp == '3':
            print_bookmarks(bookmarker.all_notes) 
        elif resp == '4':
            results = call(bookmarker.find, input(INPUT_FIND))
            print_bookmarks(results)
        elif resp == '5':
            print_bookmarks(bookmarker.all_notes) 
            call(bookmarker.remove_by_id, input(INPUT_REMOVE))
        
        resp = input(INPUT_MAIN_MENU)

if __name__ == "__main__":
    print("Welcome to PyBookmarker! \n")

    # the file used to store bookmarks
    p = Path(BOOKMARK_PATH) / BOOKMARK_FILE

    # if file does not exist, create it.
    if not p.exists():
        p.touch()

    # instantiate the bookmark class and pass to run 
    bm = Bookmarker(p)
    try:
        run(bm)
    except: 
        print("Uh oh. The programming team for pybookmark has clearly missed handling a critical error. Please direct all complaints to the TAs! :)")
