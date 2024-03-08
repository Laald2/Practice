cmake_minimum_required(VERSION 3.10)
project(CMakeTest)

# Include directories
include_directories("Practice/TestCMake/include")

# Globbing all source files
file(GLOB_RECURSE SOURCES "Practice/TestCMake/src/*.cpp")

# Add the executable target
add_executable(CMakeTest ${SOURCES})
