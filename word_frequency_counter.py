def most_frequent_word(text):
    words = text.lower().split()

    freq = {}
    # Count the frequency of each word
    for word in words:
        freq[word] = freq.get(word,0)+1
    max_count= max(freq.values())

    c= []
    # Find the words with the maximum frequency
    for word in freq:
        if freq[word] == max_count:
            c.append(word)

    return min(c)

print(most_frequent_word("the cat and the dog and the bird"))
print(most_frequent_word("apple banana apple cherry banana"))
print(most_frequent_word("Hello world hello"))
print(most_frequent_word("one"))



