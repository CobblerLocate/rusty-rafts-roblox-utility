#include "roblox_utils.h"
#include <random>
#include <algorithm>

namespace RobloxUtils {
    std::string generateRandomName(int length) {
        const std::string chars = "abcdefghijklmnopqrstuvwxyz0123456789";
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dist(0, chars.size() - 1);

        std::string result;
        for (int i = 0; i < length; ++i) {
            result += chars[dist(gen)];
        }
        return result;
    }

    bool isValidRobloxUsername(const std::string& username) {
        if (username.empty() || username.size() > 20) return false;
        return std::all_of(username.begin(), username.end(), [](char c) {
            return isalnum(c) || c == '_';
        });
    }

    std::vector<std::string> splitString(const std::string& str, char delimiter) {
        std::vector<std::string> tokens;
        size_t start = 0;
        size_t end = str.find(delimiter);

        while (end != std::string::npos) {
            tokens.push_back(str.substr(start, end - start));
            start = end + 1;
            end = str.find(delimiter, start);
        }
        tokens.push_back(str.substr(start));
        return tokens;
    }
}