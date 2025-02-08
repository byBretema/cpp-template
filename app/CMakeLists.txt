cmake_minimum_required(VERSION 3.25)

# Project
project(${APP_PARENT_FOLDER})

# Build as Debug by default
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()

# Output
if (NOT MSVC)
    set(EXTRA_FOLDER ${CMAKE_BUILD_TYPE})
else()
    set(EXTRA_FOLDER "")
endif()
#set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/lib/${EXTRA_FOLDER})
#set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/lib/${EXTRA_FOLDER})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/bin/${EXTRA_FOLDER})

# Target
add_executable(${PROJECT_NAME}

    Utils/base.hpp
    Utils/args.hpp
    Utils/args.cpp

    main.cpp
)

set_target_properties(${PROJECT_NAME}
    PROPERTIES
        CMAKE_CXX_EXTENSIONS OFF
        CMAKE_CXX_VISIBILITY_PRESET hidden
        CMAKE_VISIBILITY_INLINES_HIDDEN ON
        CMAKE_EXPORT_COMPILE_COMMANDS ON
)

target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_20)
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_LIST_DIR}/Vendor)  # 3rd party no-conan libs

# Dependencies  (https://docs.conan.io/2/reference/tools/cmake/cmakedeps.html#generated-files)
target_link_libraries(${PROJECT_NAME} ${CONANDEPS_LEGACY})
