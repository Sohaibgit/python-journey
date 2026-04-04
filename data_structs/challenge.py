"""
Challenge:
Write a function that takes a list of strings and returns a dictionary where keys are the first letter and values are lists of
words starting with that letter. (This tests list comprehensions, dicts, and the defaultdict pattern.)
"""

import pprint
import json

# Approach 1
def group_by_first_letter(words):
    result = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)

    return result


words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
result = group_by_first_letter(words)
# print(json.dumps(result, indent=4))
# pprint.pprint(group_by_first_letter(words))


# Approach 2
def group_by_first_letter_2(words):
    first_letters = {word[0].lower() for word in words}
    print(f"first_letters: {first_letters}")

    # it is like for each individual letter in a set, compare all words first letter. If it is found add that word to a list against that letter in dict
    return {
        letter: [word for word in words if word[0] == letter]
        for letter in first_letters
    }

print(json.dumps(group_by_first_letter_2(words), indent=4))