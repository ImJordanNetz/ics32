def make_list(items):
    l = []
    for i in items:
        l.append(i)
    return l

if __name__ == "__main__":
    print(make_list([1,2,3]))
    print(make_list((1,2,3)))
    print(make_list({'a','b','c'}))
    print(make_list(range(5)))

    # print(make_list(3))