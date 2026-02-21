#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

// 1️⃣ Demonstrating Character Array
void charArrayDemo() {
    cout << "Character Array Demo\n";

    char name[10] = "Priyal";
    cout << "Original: " << name << endl;

    // Modify character
    name[0] = 'A';
    cout << "After modification: " << name << endl;

    cout << endl;
}

// 2️⃣ Demonstrating string (STL)
void stringDemo() {
    cout << "STL string Demo\n";

    string s = "hello";
    cout << "Original: " << s << endl;

    s[0] = 'H';
    s += " world";

    cout << "After modification: " << s << endl;
    cout << endl;
}

// 3️⃣ Frequency Count using Array (Lowercase only)
void frequencyUsingArray(string s) {
    cout << "Frequency using array (lowercase only)\n";

    vector<int> freq(26, 0);

    for (char c : s) {
        if (c >= 'a' && c <= 'z')
            freq[c - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            cout << char(i + 'a') << " -> " << freq[i] << endl;
        }
    }

    cout << endl;
}

// 4️⃣ Frequency Count using unordered_map
void frequencyUsingMap(string s) {
    cout << "Frequency using unordered_map\n";

    unordered_map<char, int> freq;

    for (char c : s) {
        freq[c]++;
    }

    for (auto &pair : freq) {
        cout << pair.first << " -> " << pair.second << endl;
    }

    cout << endl;
}

int main() {

    charArrayDemo();

    stringDemo();

    string input = "abbccc";

    frequencyUsingArray(input);

    frequencyUsingMap(input);

    return 0;
}
