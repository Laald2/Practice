cmake_minimum_required(VERSION 3.10)
project(YourProjectName)

# Enable testing
enable_testing()

# Set the source and include directories
set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/TestCMake/src)
set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/TestCMake/include)

# Add the source and include directories
include_directories(${INCLUDE_DIR})
add_subdirectory(${SOURCE_DIR})

# Add a custom target to run all tests
add_custom_target(run_all_tests
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    COMMENT "Running all tests"
)
