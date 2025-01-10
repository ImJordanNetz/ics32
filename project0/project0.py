# project0.py

# Starter code for project 0 in ICS 32 Programming with Software Libraries in Python

# Jordan Netz
# jnetz@uci.edu
# 56628532

def square(n):
    if n == 0: return
    
    print("+-+")
    print("| |")
    for i in range(n-1):
        print(i*'  ' + "+-+-+")
        print((i+1)*'  ' + "| |")
    print((n-1)*'  ' + "+-+")

def main():
    n = int(input())
    square(n)
if __name__ == "__main__":
    main()