from project1 import parse_command


# if user_input == "man cat":
#         p = Path("test_project1.py")
#         with p.open() as file:
#             text = file.read()
#             print(text)
#             return text

def run_test(test_name, command, expected_output):
    actual_output = parse_command(command)
    passed = actual_output.strip() == expected_output.strip()
    if passed:
        print(f"✓ {test_name} passed!")
    else:
        print(f"✗ {test_name} failed!")
        print("Expected output:")
        print(expected_output)
        print("Actual output:")
        print(actual_output)
        print("---")
    return passed

def run_alt_test(test_name, command, expected_output1, expected_output2):
    actual_output = parse_command(command)
    passed = actual_output.strip() == expected_output1.strip() or actual_output.strip() == expected_output2.strip()
    if passed:
        print(f"✓ {test_name} passed!")
    else:
        print(f"✗ {test_name} failed!")
        print("Expected output 1:")
        print(expected_output1)
        print("Expected output 2:")
        print(expected_output2)
        print("Actual output:")
        print(actual_output)
        print("---")
    return passed

def run_contains_test(test_name, command, expected_output):
    actual_output = parse_command(command)
    passed = expected_output.strip() in actual_output.strip()
    if passed:
        print(f"✓ {test_name} passed!")
    else:
        print(f"✗ {test_name} failed!")
        print("Expected to contain:")
        print(expected_output)
        print("Actual output:")
        print(actual_output)
        print("---")
    return passed

def run_all_tests():
    total_tests = 0
    passed_tests = 0

    # Active test cases
    print("\nRunning active test cases:")
    print("-------------------------")
    
    # Test 1: q command
    total_tests += 1
    if run_contains_test("Test 1: q command", "q", "quit"):
        passed_tests += 1

    # Test 3: man q
    total_tests += 1
    if run_test("Test 3: man q", "man q", 
        "The File System Explorer supports this command in the following format/s:\n"
        "[COMMAND]\n"
        "q is a command that quits the file system explorer.\n"):
        passed_tests += 1

    # Test 4: man ls
    total_tests += 1
    if run_test("Test 4: man ls", "man ls",
        "The File System Explorer supports this command in the following format/s:\n"
        "[COMMAND] [INPUT]\n"
        "[COMMAND] [-OPTIONS] [INPUT]\n"
        "[COMMAND] [-OPTIONS] [INPUT] [OPTION_INPUT]\n"
        "The [INPUT] corresponds to the [COMMAND].\n"
        "The [OPTIONAL_INPUT] corresponds to [-OPTIONS].\n"
        "ls is a command that lists the contents of a directory. [INPUT] is the path.\n"
        "ls options include -r, -f, -s, -e, -g and -l.\n"
        "-r = recursive, -f file only, -s match specific file name, -e match specific extension.\n"
        "-g and -l prints only files with size greater (g) or less (l) than [OPTION_INPUT].\n"):
        passed_tests += 1

    # Test 5: man cat
    total_tests += 1
    if run_test("Test 5: man cat", "man cat",
        "The File System Explorer supports this command in the following format/s:\n"
        "[COMMAND] [INPUT]\n"
        "[COMMAND] [-OPTIONS] [INPUT]\n"
        "The [INPUT] corresponds to the [COMMAND].\n"
        "cat is a command that prints the contents of a file. [INPUT] is the file path.\n"
        "cat options include -f and -d.\n"
        "-f = prints the first line only, -d duplicates the file into filename.dup.\n"):
        passed_tests += 1

    # Test 7: ls .
    total_tests += 1
    if run_test("Test 7: ls .", "ls .",
        "solution.py\n"
        "test_project1.py\n"
        "test_solution.py\n"
        "__pycache__\n"
        "autograder\n"):
        passed_tests += 1

    # Test 8: ls -r .
    total_tests += 1
    if run_test("Test 8: ls -r .", "ls -r .",
        "solution.py\n"
        "test_project1.py\n"
        "test_solution.py\n"
        "__pycache__\n"
        "autograder\n"
        "__pycache__/solution.cpython-310.pyc\n"
        "__pycache__/test_project1.cpython-310.pyc\n"
        "__pycache__/test_solution.cpython-310.pyc\n"
        "autograder/deploy_key\n"
        "autograder/run_autograder\n"
        "autograder/run_tests.py\n"
        "autograder/setup.sh\n"
        "autograder/ssh_config\n"):
        passed_tests += 1

    # Test 9: ls -f .
    total_tests += 1
    if run_test("Test 9: ls -f .", "ls -f .",
        "solution.py\n"
        "test_project1.py\n"
        "test_solution.py\n"):
        passed_tests += 1

    # Test 10: ls -fr .
    total_tests += 1
    if run_test("Test 10: ls -fr .", "ls -fr .",
        "solution.py\n"
        "test_project1.py\n"
        "test_solution.py\n"
        "__pycache__/solution.cpython-310.pyc\n"
        "__pycache__/test_project1.cpython-310.pyc\n"
        "__pycache__/test_solution.cpython-310.pyc\n"
        "autograder/deploy_key\n"
        "autograder/run_autograder\n"
        "autograder/run_tests.py\n"
        "autograder/setup.sh\n"
        "autograder/ssh_config\n"):
        passed_tests += 1

    # Test 15: cat -d and ls -s
    total_tests += 1
    parse_command("cat -d solution.py")
    if run_alt_test("Test 15: cat -d and ls -s", "ls -s . solution",
        "solution.py\n"
        "solution.py.dup\n"
        "test_solution.py\n",
        "./solution.py\n"
        "./solution.py.dup\n"
        "./test_solution.py\n"):
        passed_tests += 1



    # Commentec test cases

    print("\nRunning commented test cases:")
    print("---------------------------")

    # Test 2: man man
    total_tests += 1
    if run_test("Test 2: man man", "man man",
        "The File System Explorer supports this command in the following format/s:\n"
        "[COMMAND] [INPUT]\n"
        "man is a command that prints the directions for the command. [INPUT] is the command.\n"):
        passed_tests += 1

    # Test 6: man test
    total_tests += 1
    if run_test("Test 6: man test", "man test",
        "ERROR: Invalid Command.\n"):
        passed_tests += 1

    # Test 11: ls -frs
    total_tests += 1
    if run_test("Test 11: ls -frs", "ls -frs ../project1 solution",
        "../project1/solution.py\n"
        "../project1/test_solution.py\n"
        "../project1/__pycache__/solution.cpython-310.pyc\n"
        "../project1/__pycache__/test_solution.cpython-310.pyc\n"):
        passed_tests += 1

    # Test 12: ls -fre
    total_tests += 1
    if run_test("Test 12: ls -fre", "ls -fre ../project1 sh",
        "../project1/autograder/setup.sh\n"):
        passed_tests += 1

    # Test 13: ls -fre invalid format
    total_tests += 1
    if run_test("Test 13: ls -fre invalid", "ls -fre ../project1",
        "ERROR: Invalid Format.\n"):
        passed_tests += 1

    # Test 14: ls invalid path
    total_tests += 1
    if run_test("Test 14: ls invalid path", "ls test",
        "ERROR: Invalid Path.\n"):
        passed_tests += 1

    # Test 16: cat -f
    total_tests += 1
    if run_test("Test 16: cat -f", "cat -f test_project1.py",
        "import unittest\n"):
        passed_tests += 1

    # Test 17: cat invalid format
    total_tests += 1
    if run_test("Test 17: cat invalid format", "cat",
        "ERROR: Invalid Format.\n"):
        passed_tests += 1

    # Print summary
    print("\nTest Summary:")
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {total_tests - passed_tests}")
    print(f"Success rate: {(passed_tests/total_tests)*100:.2f}%")

if __name__ == "__main__":
    run_all_tests()