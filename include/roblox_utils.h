#pragma once
#include <string>
#include <vector>

namespace RobloxUtils {
    std::string generateRandomName(int length);
    bool isValidRobloxUsername(const std::string& username);
    std::vector<std::string> splitString(const std::string& str, char delimiter);
}