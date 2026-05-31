#include "raft_manager.h"
#include <sstream>

RaftManager::RaftManager() = default;

void RaftManager::addRaft(const std::string& name, int durability) {
    rafts.push_back({name, durability});
}

int RaftManager::getRaftCount() const {
    return static_cast<int>(rafts.size());
}

std::string RaftManager::getRaftInfo(int index) const {
    if (index < 0 || index >= getRaftCount()) return "Invalid raft index";

    const auto& raft = rafts[index];
    std::ostringstream oss;
    oss << "Raft: " << raft.name << " | Durability: " << raft.durability << "%";
    return oss.str();
}