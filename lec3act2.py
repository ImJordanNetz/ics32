from random import randint

def classroom(seats):
    # returns a list which describes the classroom  
    # 1 indicates a student and 0 indicates an empty seat

    students = []
    for i in range(seats):
        students.append(randint(0,1))
    return students

def count(students):
    if len(students) == 1:
        return student[0]
    else:
        return student[0] + count(students[1:])

def main():
    students = classroom(150)
    check = sum(students)

    number = count(students) 
    print(f"\nThere are {number} students in class today." )
    print(f"That is {int(number*100/137)} percent of the class.")
    print(f"sum(students) == {check}.\n")

if __name__ == "__main__":
    main()
