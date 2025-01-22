TESTING = 32

# Good ways to import
from powers import square, cube as correct_cube

# Python processes the file sequentially, top to bottom

def cube(test):
    return test*test

def main():
    print(square(3))
    print(correct_cube(2))

    print(f"\nmain() local namespace: {locals()} \n")
    print(f"global namespace: {globals()} \n")
 
if __name__ == "__main__":
    main()