cmake_minimum_required(VERSION 3.10)
project(rusty_rafts_roblox_utility)

set(CMAKE_CXX_STANDARD 17)

add_executable(rusty_rafts_roblox_utility
    src/main.cpp
    src/roblox_utils.cpp
    src/raft_manager.cpp
)

target_include_directories(rusty_rafts_roblox_utility PRIVATE include)
target_link_libraries(rusty_rafts_roblox_utility PRIVATE fmt)