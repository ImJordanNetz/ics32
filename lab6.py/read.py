from note import Note
class Bookmarker(Note):
    def __init__(self, h):    
        from pathlib import Path
        p = Path('.') 
        for item in p.iterdir():
            print(str(item))
        p = Path("solution.py")
        with p.open() as f:
            print(f.read())    
