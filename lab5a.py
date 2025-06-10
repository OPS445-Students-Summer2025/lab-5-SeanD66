#!/usr/bin/env python3

# Author ID: sdaweng

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    file_open = open(str(file_name), 'r')
    read_data = file_open.read()
    return read_data
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))