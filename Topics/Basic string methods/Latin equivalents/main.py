name = input()


def normalize(to_normalize):
    return to_normalize.replace("é", "e").replace("ë", "e")\
        .replace("á", "a").replace("å", "a")\
        .replace("œ", "oe")\
        .replace("æ", "ae")


print(normalize(name))
