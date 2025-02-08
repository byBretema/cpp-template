cmake_minimum_required(VERSION 3.25)

#######################################
# PROJECT
#######################################

project(app_wrapper)

#######################################
# GLOBAL PROPERTIES
#######################################

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

#######################################
# COMPILE APP
#######################################

get_filename_component(APP_PARENT_FOLDER ${CMAKE_CURRENT_SOURCE_DIR} NAME)
include(${CMAKE_BINARY_DIR}/conandeps_legacy.cmake)
add_subdirectory(app)
