#include <iostream>
#include "roblox_utils.h"
#include "raft_manager.h"

int main() {
    std::cout << "Rusty Rafts Roblox Utility\n";

    RaftManager manager;
    manager.addRaft("Oak Raft", 85);
    manager.addRaft("Pine Raft", 60);

    std::cout << "Total rafts: " << manager.getRaftCount() << "\n";
    for (int i = 0; i < manager.getRaftCount(); ++i) {
        std::cout << manager.getRaftInfo(i) << "\n";
    }

    std::string randomName = RobloxUtils::generateRandomName(8);
    std::cout << "Generated name: " << randomName << "\n";

    return 0;
}