import pprint
print
original_list = ['orange', 'apple', 'CPU', 'hard drive']

def list2dict(list):
    dict = {}
    for index, value in enumerate(list):
        dict[index] = value
    return dict




new_dict = list2dict(original_list)
pprint.pprint(new_dict)
print new_dict[3] 
