def exception_v1(filename):
    s = 0
    try:
        file = open(filename, "r")
    except Exception as e:
        print(e)
        
    for i in file:
        if i.isDigit():
            s = s + int(i)
        else: 
            print("File reading non-number string")
    file.close()

    print(s)
