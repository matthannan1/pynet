import urllib2
import re

def separate_interface_data(ospf_data):
    # Split the data based on 'is up, line protocol is up' but retain this string
    ospf_data = re.split(r'(.+ is up, line protocol is up)', ospf_data)
    # Dump any data before the first 'is up, line protocol is up'
    ospf_data.pop(0)
    ospf_list = []
    while True:
        if len(ospf_data) >= 2:
            intf = ospf_data.pop(0)
            section = ospf_data.pop(0)
            # reunify because it was split up in the re.split
            ospf_string = intf + section
            ospf_list.append(ospf_string)
        else:
            break
    return ospf_list

def generic_ospf_parser(pattern, ospf_data):
    '''
    Takes a generic regular expression pattern that has a group(1) match
    pattern and returns this
    Else returns None
    '''
    a_match = re.search(pattern, ospf_data)
    if a_match:
        return a_match.group(1)
    return None

def print_ospf_out(a_dict):
    '''
    Prints a given ospf interface section to STDOUT
    '''
    field_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')
    print
    for a_field in field_order:
        if a_dict.get(a_field) is not None:
            print "%15s:   %-20s" % (a_field, a_dict.get(a_field))

# Technique to allow importable and executable code to coexist (will explain in class#8)
if __name__ == '__main__':
    path = 'https://raw.githubusercontent.com/ktbyers/pynet/master/learnpy_ecourse/class7/OSPF_DATA/ospf_data.txt'
    a_file = urllib2.urlopen(path)
    ospf_output = a_file.read()
    ospf_data_sections = separate_interface_data(ospf_output)
#    ospf_output.close()

    ospf_dict_patterns = {
        'Int' : r"^(.+) is up, line protocol is up",
        'IP' : r"Internet Address (.+?),",
        'Area' : r"Area (.+?), ",
        'Type' : r"Network Type (.+?),",
        'Hello' : r"Hello (.+),",
        'Dead' : r"Dead (.+?),",
    }

    for int_section in ospf_data_sections:
        master_dict = {}
        for i, ospf_pattern in ospf_dict_patterns.items():
            return_val = generic_ospf_parser(ospf_pattern, int_section)
            if return_val is not None:
                master_dict[i] = return_val
        print_ospf_out(master_dict)

print
