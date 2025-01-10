# project0.py

# Starter code for project 0 in ICS 32 Programming with Software Libraries in Python

# Jordan Netz
# jnetz@uci.edu
# 56628532

def square(n):
    output = ''
    if n == 0: return output
    
    output += "+-+" + '\n'
    output += "| |" + '\n'
    for i in range(n-1):
        output += i*'  ' + "+-+-+" + '\n'
        output += (i+1)*'  ' + "| |" + '\n'
    output += (n-1)*'  ' + "+-+" + '\n'
    return output

def main():
    n = int(input())
    square(n)
if __name__ == "__main__":
    main()