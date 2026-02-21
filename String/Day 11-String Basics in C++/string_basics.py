# 1️⃣ Mutable Demonstration

def string_demo():
    print("Python String Demo (Immutable)")

    s = "hello"
    print("Original:", s)

    # Python strings are immutable
    # s[0] = 'H'  ❌ This will cause error

    s = "H" + s[1:]
    print("After modification:", s)
    print()


# 2️⃣ Frequency using list (lowercase only)

def frequency_using_array(s):
    print("Frequency using list (lowercase only)")

    freq = [0] * 26

    for c in s:
        if 'a' <= c <= 'z':
            freq[ord(c) - ord('a')] += 1

    for i in range(26):
        if freq[i] > 0:
            print(chr(i + ord('a')), "->", freq[i])

    print()


# 3️⃣ Frequency using dictionary

def frequency_using_dict(s):
    print("Frequency using dictionary")

    freq = {}

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    for key, value in freq.items():
        print(key, "->", value)

    print()


if __name__ == "__main__":
    string_demo()

    input_string = "abbccc"

    frequency_using_array(input_string)

    frequency_using_dict(input_string)
