#pragma once
#include <string>
#include <vector>

class RaftManager {
public:
    RaftManager();
    void addRaft(const std::string& name, int durability);
    int getRaftCount() const;
    std::string getRaftInfo(int index) const;

private:
    struct Raft {
        std::string name;
        int durability;
    };
    std::vector<Raft> rafts;
};