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
