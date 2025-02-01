# import OS module
import os

import re
import glob

class Format:
    end = '\033[0m'
    underline = '\033[4m'

# Get the list of all files and directories
path = "uvm_files"
#print(path)

print("\n")
print(Format.underline + "SEE DETAILS BELOW" + Format.end)
print("\n")
print(Format.underline + "INHERITED CLASSES" + Format.end)

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
print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)), "\n")

print(Format.underline + "CONSTRAINTS" + Format.end)

a = ["constraint"]

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
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

#print("\nFound these constraints in the uvm hierachy: ", existing_classes)
#print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)))

print((Format.underline + "RANDOMIZATIONS" + Format.end).rstrip())

a = ["randomize"]

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
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

#print("\nFound these randomizations in the uvm hierachy: ", existing_classes)
#print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)))

print(Format.underline + "FACTORY METHODS" + Format.end)

a = ["uvm_component_utils", "uvm_object_utils"]

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
                   #existing_classes.append(row.strip("\n"))
                   print("Found: ", f'"{row.strip("\n").strip()}"', "\n")

#print("\nNeed these classes to be defined in the uvm hierarchy: ", list(set(a) - set(existing_classes)))

#OUTPUT:
#
#
#SEE DETAILS BELOW
#
#
#INHERITED CLASSES
#
#Checking for:  ['uvm_test', 'uvm_driver', 'uvm_monitor', 'uvm_sequence', 'uvm_sequence_item', 'uvm_env']  in uvm hierarchy files.
#
#"uvm_sequence"  exists in the file:  "uvm_files\constraints.sv"  in line number:  2
#"uvm_sequence_item"  exists in the file:  "uvm_files\constraints.sv"  in line number:  2
#"uvm_driver"  exists in the file:  "uvm_files\driver1.sv"  in line number:  2
#"uvm_test"  exists in the file:  "uvm_files\test1.sv"  in line number:  3
#
#Found these classes in the uvm hierachy:  ['uvm_sequence', 'uvm_sequence_item', 'uvm_driver', 'uvm_test']
#
#Need these classes to be defined in the uvm hierarchy:  ['uvm_env', 'uvm_monitor']
#
#CONSTRAINTS
#
#Checking for:  ['constraint']  in uvm hierarchy files.
#
#"constraint"  exists in the file:  "uvm_files\constraints.sv"  in line number:  6
#Found:  "constraint addr {addr > 0; addr < 10};"
#
#"constraint"  exists in the file:  "uvm_files\constraints.sv"  in line number:  8
#Found:  "soft constraint data {data inside [0:100]};"
#
#RANDOMIZATIONS
#
#Checking for:  ['randomize']  in uvm hierarchy files.
#
#"randomize"  exists in the file:  "uvm_files\constraints.sv"  in line number:  10
#Found:  "assert.randomize(txn1);"
#
#"randomize"  exists in the file:  "uvm_files\packet.sv"  in line number:  11
#Found:  "pkt.randomize() with { addr == 8;};"
#
#FACTORY METHODS
#
#Checking for:  ['uvm_component_utils', 'uvm_object_utils']  in uvm hierarchy files.
#
#"uvm_component_utils"  exists in the file:  "uvm_files\constraints.sv"  in line number:  4
#Found:  "`uvm_component_utils(txn1)"
#
#