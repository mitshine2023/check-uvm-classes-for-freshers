# import OS module
import os

import re
import glob

# Get the list of all files and directories
path = "uvm_files"
#print(path)

a = ["uvm_test", "uvm_driver", "uvm_monitor", "uvm_sequence", "uvm_sequence_item", "uvm_env"]
print("\nChecking for: ", a, " in uvm hierarchy files.\n")

existing_classes = []

#for i in dir_list:
for i in glob.glob(path + '/*.sv'):
    #print(i)
    # string to search in file
    with open(i, 'r') as fp:
        # read all lines using readline()
        lines = fp.readlines()
        for row in lines:
            # check if string present on a current line
            for word in a:
               #print(word)
               #r = re.compile('|'.join([r'\b%s\b' % w for w in words]), flags=re.I)
               #print(row.find(word))
               # find() method returns -1 if the value is not found,
               # if found it returns index of the first occurrence of the substring
               if row.find(word) != -1:
                   print(f'"{word}"', " exists in the file: ",f'"{i}"', " in line number: ", lines.index(row) + 1)
                   existing_classes.append(word)

print("\nFound these classes in the uvm hierachy: ", existing_classes)
print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)))

#OUTPUT:
#
#Checking for:  ['uvm_test', 'uvm_driver', 'uvm_monitor', 'uvm_sequence', 'uvm_sequence_item', 'uvm_env']  in uvm hierarchy files.
#
#"uvm_driver"  exists in the file:  "uvm_files\driver1.sv"  in line number:  2
#"uvm_test"  exists in the file:  "uvm_files\test1.sv"  in line number:  3
#
#Found these classes in the uvm hierachy:  ['uvm_driver', 'uvm_test']
#
#Need these classes to be defined in the uvm hierarchy:  ['uvm_env', 'uvm_sequence', 'uvm_sequence_item', 'uvm_monitor']
