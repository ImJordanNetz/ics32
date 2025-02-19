from pathlib import Path
class Note:
    def __init__(self, p: Path):
        self.p = p
    
    
    def read_notes(self):
        if not self.p.exists():
            return
        
        notes = []
        f = self.p.open()
        for line in f:
            notes.append(line.strip())
        f.close()
        return notes
    
    def __str__(self):
        return str(self.p)
    def save_note(self, note: str):
        # create path obj to notes storage file
        # check if storage file exists, if not create it.
        if not self.p.exists():
            self.p.touch(exist_ok=True)
        
        # open and write user note to file
        f = self.p.open('a')
        f.write(note + '\n')
        f.close()
    
    def is_int(self, val):
        if isinstance(val, (bool, float)):
            return False
        try:
            int(val)
            return True
        except ValueError:
            return False
    
    def remove_note(self, remove_id) -> str:

        # check if storage file exists, if not return.
        if not self.p.exists():
            raise FileNotFoundError
        # open and write user note to file
        f = self.p.open()
        id = 1
        lines = []

        # print each note with an id and store each line in a list
        for line in f:
            lines.append(line)
            id = id+1
        f.close()
        if not self.is_int(remove_id):
            print ("Not a valid number, cancelling operation.")
            return ""
        
            # open as write to overwrite existing notes, add notes back while skipping user selection 
        f = self.p.open('w')
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
