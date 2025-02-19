from pathlib import Path

def run():
    path = Path(directory)

    if not path.exists() or not path.is_dir():
        print(f"Error: '{directory}' is not a valid directory.")
        return []

    files = [str(file) for file in path.iterdir() if file.is_file()]

    for file in files:
        print(file)

    return files