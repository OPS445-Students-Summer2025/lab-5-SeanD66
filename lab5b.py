#!/usr/bin/env python3

# Author ID: sdaweng

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    file_open = open(str(file_name), 'r')
    read_data = file_open.read()
    file_open.close()
    return read_data
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    contents = ''
    line = f.readline()
    while line:
        contents += line
        line = f.readline()
    f.close()
    return contents

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    file_append = open(str(file_name), 'a')
    append_str = file_append.write(string_of_lines)
    file_append.close()
    return append_str
    


def write_file_list(file_name, list_of_lines):
#     # Takes a string and list, writes all items from list to file where each item is one line
    write_in_one_line = open(str(file_name), 'w')
    for num in list_of_lines:
        write_in_one_line.write(str(num) + '\n')
    write_in_one_line.close()
    


def copy_file_add_line_numbers(file_name_read, file_name_write):
     # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    f_read = open(file_name_read, 'r')
    lines = f_read.readlines()
    f_read.close()

    f_write = open(file_name_write, 'w')
    i = 0
    while i < len(lines):
        f_write.write(str(i + 1) + ':' + lines[i])
        i += 1
    f_write.close()








if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))