#include "roblox_utils.h"
#include <cassert>

void testGenerateRandomName() {
    std::string name = RobloxUtils::generateRandomName(10);
    assert(name.size() == 10);
    assert(RobloxUtils::isValidRobloxUsername(name));
}

void testIsValidRobloxUsername() {
    assert(RobloxUtils::isValidRobloxUsername("Player123"));
    assert(!RobloxUtils::isValidRobloxUsername("Player@123"));
    assert(!RobloxUtils::isValidRobloxUsername(""));
}

void testSplitString() {
    auto parts = RobloxUtils::splitString("a,b,c", ',');
    assert(parts.size() == 3);
    assert(parts[0] == "a");
    assert(parts[1] == "b");
    assert(parts[2] == "c");
}

int main() {
    testGenerateRandomName();
    testIsValidRobloxUsername();
    testSplitString();
    return 0;
}