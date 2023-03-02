import sys
sys.path.append("../decorators")

from execution_time import execution_time

@execution_time
def remove_duplicates(lst):
    return list( set(lst) )

@execution_time
def remove_duplicates_w_for(lst):
    non_repeated = []

    for item in lst:
        if item not in non_repeated:
            non_repeated.append(item)

    return non_repeated

if __name__ == "__main__":
    my_list = [7,3,7,8,3,6,0,9,4,9,4,3,7,3,1,7,8,2,7,3,6,3,6,7,2,7,6,2,7,6,1,2,7,2,1,1,9,1,9,2,0,0,4,3,8]
    print(
        remove_duplicates(my_list)
    )
    print(
        remove_duplicates_w_for(my_list)
    )