def reverse_words(text):
    result = [letter[::-1] for letter in text.split(" ")]
    return " ".join(result)
