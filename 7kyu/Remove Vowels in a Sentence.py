def disemvowel(string):
    vowel = ('a','e','i','o','u','A','E','I','O','U')
    result = ""
    for w in string:
        if w not in vowel:
            result += w
    return result
