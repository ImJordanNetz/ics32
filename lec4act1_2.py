def remove_from(the_list, value):
    new_list = []
    try:
        found = False
        for element in the_list:
            if element != value:
                new_list.append(element)
            else:
                found = True
                
        if found == False:
            raise ValueError("value to remove was not found in the_list")
        return new_list
    except ValueError:
        print("ValueError detected!")
        return the_list


def test():
    x = [1, 3, 5, 7, 9, 11, 13]
    assert 1 not in remove_from(x, 1), "remove_from failed to remove correct value"
    assert 13 not in remove_from(x, 13), "remove_from failed to remove correct value"
    assert 2 not in remove_from(x, 2), "remove_from failed to remove correct value"
    x = [2]
    assert 2 not in remove_from(x, 2), "remove_from failed to remove correct value"

    
if __name__ == "__main__":
    test()