def list_to_dictionary(list):
    dictionary = {}
    for i, value in list:
        dictionary.append(i,value)
        i = i + 1
    return dictionary






the_list = ['apple', 'banana', 'CPU', 'RAM', 'cam shaft', 'oil filter']


list_to_dictionary(the_list)
print the_dictionary

####################################################

def list_to_dict(a_list):
    '''
    Convert a list to a dictionary
    '''

    new_dict = {}

    for i, v in enumerate(a_list):
        new_dict[i] = v

    return new_dict



# Create a simple test list
test_list = range(100, 110)
test_list.append('whatever')

# Call the function
test_dict = list_to_dict(test_list)

# Display the results
print
print "List: %s" % str(test_list)
print "Dict: %s" % str(test_dict)
print
