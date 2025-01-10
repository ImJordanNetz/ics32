def sample(filename):
    with open(filename, 'r') as f:
        for i in range(10):
            print(f.readline().strip())

def select_write(filename):
    with open(filename) as f:
        with open("sample.txt", 'w') as f2:
            for i in range(10):
                f2.write(f.readline().strip())

                

if __name__ == "__main__":
   sample("")
   select_write("")