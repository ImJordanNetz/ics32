from pathlib import Path
def print_path(path):
    dir = Path(path)
    if dir.is_dir() and dir.exists():
        [print(d) for d in dir.iterdir()]

if __name__ == "__main__":
    print_path("/Users/user/Desktop")