from pathlib import Path


def write_notes(to_write, file_path):
    with open(file_path, "a+") as f:
        f.write(to_write + "\n\n")

def start_notes():
    path = Path("pynote.txt")
    welcome_message = ''
    
    if path.is_file() and path.exists():
        welcome_message = "Welcome to PyNote!\n\n"
        welcome_message += f"Below are the notes stored in this file: {path}\n\n"

        with open(path, "r") as f:
            for line in f:
                welcome_message+=line

    return(welcome_message, path)

def main():
    welcome, path = start_notes()
    print(welcome)
    user_input = input("Please enter a new note (enter q to exit): ")
    while user_input != "q":
        write_notes(user_input, path)
        user_input = input("Please enter a new note (enter q to exit): ")

if __name__ == "__main__":
    main()