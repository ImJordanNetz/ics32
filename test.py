   p = Path(".")
    target_filename = "test_project2.py"  # Change this to the desired filename

    for item in p.iterdir():
        print("I see", item.name)
        if item.name == target_filename and item.is_file():
            with item.open("r", encoding="utf-8") as file:
                print("Contents of", item.name, ":\n", file.read())