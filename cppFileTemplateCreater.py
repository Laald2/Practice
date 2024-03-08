'''
This python scripts is used to quickly write a .cpp and .h 
for a class of your choice and namespace of your choice and your choice location
only includes the default
'''


import argparse
import os

def ParseArguments():
    parser = argparse.ArgumentParser(description='Process File name')
    parser.add_argument('-f','--file',
                        help='enter a file base name to be created')
    parser.add_argument('-n','--namespace',
                        help='for c++ files there are namespace enter what your namespace is')
    parser.add_argument('-l','--location',
                        help='set where to create this file')
    parser.add_argument('-s', '--seperate', action='store_true',
                        help='use to seperate header and cpp files with include and src directories')
    args = parser.parse_args()
    return args

def WriteDefaultHeader(file, file_name, tab):
    '''
    Write the default of the header file
    '''
    if tab:
        file_name.write("\tclass " + file + "\n\t{\n")
        file_name.write("\t\t" + file +"() = default;\n")
        file_name.write("\t\t~" + file + "() = default;\n")
        file_name.write("\t\t" + file + "(const " + file + "& other) = delete;\n")
        file_name.write("\t\t" + file + "& operator=(const " + file + "& other) = delete;\n")
        file_name.write("\t};")
    else:
        file_name.write("class " + file + "\n{\n")
        file_name.write("\t" + file +"() = default;\n")
        file_name.write("\t~" + file + "() = default;\n")
        file_name.write("\t" + file + "(const " + file + "& other) = delete;\n")
        file_name.write("\t" + file + "& operator=(const " + file + "& other) = delete;\n")
        file_name.write("};")

def CreateHeaderFile(file, args):
    '''
    creating header file
    '''
    print("creating header file")
    file_path = file
    if args.location:
        if args.seperate:
            if (not os.path.exists(args.location)):
                os.makedirs(args.location)
            if (not os.path.exists(os.path.join(args.location, 'include'))):
                os.makedirs(os.path.join(args.location, 'include'))
            file_path = os.path.join(args.location, 'include', file)
        else:
            file_path = os.path.join(args.location, file)

    with open(os.path.join(file_path + '.h'), 'w') as file_name:
        # Write content to the file
        if args.namespace != None:
            file_name.write("namespace "+ args.namespace + "\n{\n")
            WriteDefaultHeader(file, file_name, True)
            file_name.write("\n}")
        else:
            WriteDefaultHeader(file, file_name, False)
    return 0


def WriteCPPConstructor(file, file_name, tab):
    '''
    write the constructor of a cpp file
    '''
    if tab:
        file_name.write("\t" + file + "::" + file +"()\n")
        file_name.write("\t{}")
    else:
        file_name.write(file + "::" + file +"()\n")
        file_name.write("{}")

def CreateCPPFile(file, args):
    '''
    creating cpp file
    '''
    print("creating cpp file")
    file_path = file
    if args.location:
        if args.seperate:
            if (not os.path.exists(args.location)):
                os.makedirs(args.location)
            if (not os.path.exists(os.path.join(args.location, 'src'))):
                os.makedirs(os.path.join(args.location, 'src'))
            file_path = os.path.join(args.location, 'src', file)
        else:
            file_path = os.path.join(args.location, file)
    with open(os.path.join(file_path + '.cpp'), 'w') as file_name:
        # Write content to the file
        file_name.write('#include "' + file + '.h"\n')
        if args.namespace != None:
            file_name.write("namespace "+ args.namespace + "\n{\n")
            WriteCPPConstructor(file, file_name, True)
            file_name.write("\n}")
        else:
            WriteCPPConstructor(file, file_name, False)
    return 0


def Main(args):
    file_name = args.file
    return_code = 0
    return_code += CreateCPPFile(file_name, args)
    return_code += CreateHeaderFile(file_name, args)
    if return_code == 0:
        print("############ NOTE ##################")
        print("Successfully created " +  file_name + " add CMakeLists.txt or anything else")
        print("Necessary to run your new file")
        print("####################################")

if __name__ == '__main__':
    ARGUMENTS = ParseArguments()
    Main(ARGUMENTS)