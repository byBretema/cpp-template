cmake_minimum_required(VERSION 3.25)

#######################################
# PROJECT
#######################################

project(${APP_PARENT_FOLDER})

#######################################
# BUILD TYPE: Debug as default
#######################################

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()

#######################################
# OUTPUT
#######################################

if (NOT MSVC)
    set(EXTRA_FOLDER ${CMAKE_BUILD_TYPE})
else()
    set(EXTRA_FOLDER "")
endif()
#TODO: #set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/lib/${EXTRA_FOLDER})
#TODO: #set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/lib/${EXTRA_FOLDER})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/bin/${EXTRA_FOLDER})

#######################################
# TARGET
#######################################

# Sources  (Check: https://blog.conan.io/2019/09/02/Deterministic-builds-with-C-C++.html)
file(GLOB_RECURSE SRCS ${PROJECT_SOURCE_DIR} *.c *.cc *.cpp)
file(GLOB_RECURSE HDRS ${PROJECT_SOURCE_DIR} *.h *.hh *.hpp)  # Header files to help some IDEs
add_executable(${PROJECT_NAME} ${SRCS} ${HDRS})

# Properties
set_target_properties(${PROJECT_NAME}
    PROPERTIES
        CMAKE_CXX_EXTENSIONS OFF
        CMAKE_CXX_VISIBILITY_PRESET hidden
        CMAKE_VISIBILITY_INLINES_HIDDEN ON
        CMAKE_EXPORT_COMPILE_COMMANDS ON
)

# Includes
target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR})

# Dependencies  (Check: https://docs.conan.io/2/reference/tools/cmake/cmakedeps.html#generated-files)
target_link_libraries(${PROJECT_NAME} ${CONANDEPS_LEGACY})
