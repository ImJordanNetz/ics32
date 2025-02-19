def modify_tup(tup):
    tup = tup + (4, 5)
    print(tup)

def modify_dict(d):
    d["hello"] = "world"
    print(d)
    
    
if __name__ == "__main__":
    tup = (1, 2, 3)
    modify_tup(tup)
    print(tup)
    d = {}
    modify_dict(d)
    print(d)