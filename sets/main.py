def remove_duplicates(lst):
    return list( set(lst) )

def remove_duplicates_w_for(lst):
    to_set = set({})
    for item in lst:
        to_set.add(item)
        
    return list(to_set)

if __name__ == "__main__":
    my_list = [7,3,7,8,3,6,0,9,4,9,4,3,7,3,1]
    print(
        remove_duplicates(my_list)
    )
    print(
        remove_duplicates_w_for(my_list)
    )