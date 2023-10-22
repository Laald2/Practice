# pylint: disable-all
import os
import subprocess
import argparse

#currently still using manual built cmake
#not installed

# Define the C++ compiler and compilation flags
compiler = "g++"
flags = ["-std=c++11", "-o"]

def compile_cpp(source_directory, clean_compile):
    '''
    Compile all c++ files in project
    '''
    # Get a list of all C++ files in the source directory
    cpp_files = [f for f in os.listdir(source_directory) if f.endswith(".cpp")]

    for cpp_file in cpp_files:
        source_file = os.path.join(source_directory, cpp_file)
        output_name = os.path.splitext(cpp_file)[0]
        # Use the filename (without extension) as the output name

        # Construct the compilation command
        compile_command = [compiler] + [source_file] + flags + [output_name]

        # Add the clean option if requested
        if clean_compile:
            compile_command.append("-c")

        # Run the compilation command
        try:
            subprocess.run(compile_command, check=True)
            print(f"Compiled {cpp_file} successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error compiling {cpp_file}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile C++ files in a project.")
    parser.add_argument("--clean", action="store_true", help="Perform a clean compile")

    args = parser.parse_args()

    source_directory = os.getcwd()  # Get the current working directory as the source directory
    compile_cpp(source_directory, args.clean)
