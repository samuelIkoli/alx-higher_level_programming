#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        k = list(a_dictionary.keys())[list(a_dictionary.values()).index(0)]
        del a_dictionary[k] 
