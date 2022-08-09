
def count_vowels(word):
    vowels = 'aeiou'
    result = 0
    for vowel in vowels:
        result += word.count(vowel)
    return result

print(count_vowels('apple'))