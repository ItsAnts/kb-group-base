words: list[str] = ["apple", "kiwi", "banana", "cherry"]

for i in range(1, len(words)):
    key = words[i]
    j = i - 1

    while j >= 0 and len(words[j]) > len(key):
        words[j + 1] = words[j]
        j -= 1
    words[j + 1] = key

print(words)
