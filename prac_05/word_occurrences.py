"""
Prac 5
"""
word_to_count = {}
text_input = input("Enter Text:")
words = text_input.split()
for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

words = list(word_to_count.keys())
words.sort()

longest_word_length = max((len(word) for word in words)) + 1
for word in words:
    print(f"{word:{longest_word_length}}: {word_to_count[word]}")
