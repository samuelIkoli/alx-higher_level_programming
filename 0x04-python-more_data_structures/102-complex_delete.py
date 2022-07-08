#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for v in a_dictionary.values:
        if v == value:
            k = list(a_dictionary.keys())[list(a_dictionary.values()).index(v)]
            del a_dictionary[k] 
