cmake_minimum_required(VERSION 3.10)
project(MyMQTTProject)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 14)

add_executable(MyMQTTProject main.cpp)
target_link_libraries(MyMQTTProject paho-mqtt3c)