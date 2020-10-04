def duplicate_count(text):
    myset = set()
    for t in text.lower():
        if text.lower().count(t) != 1:
            myset.add(t)
    return len(myset)
