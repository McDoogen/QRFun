cmake_minimum_required(VERSION 2.8.12)

PROJECT(QRFun)
SET(CMAKE_CXX_STANDARD 11)
SET(OpenCV_DIR /usr/local/share/opencv4)

if(MSVC)
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
endif()

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

MACRO(add_example name)
	ADD_EXECUTABLE(${name} ${name}.cpp)
	TARGET_LINK_LIBRARIES(${name} ${OpenCV_LIBS} )
ENDMACRO()

add_example(main)
