def countStudents():
    #if there is no one behind you
    return countStudentsToLeft()
    
    #else:
    return countStudents()

def countStudentsToLeft():
    
    #if there are students to your left:
    return countStudentsToLeft() + 1
    
    # else if you have to students to your left:
    return 1

def main():
    print(countStudentsToLeft())

if __name__ == "__main__":
    main()