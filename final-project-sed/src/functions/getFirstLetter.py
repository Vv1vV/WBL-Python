import string

def split_letters(old_string):
    index = -1
    for i, char in enumerate(old_string):
        if char.isalpha():
            index = i
            break
    else:
        raise ValueError("No letters found") # or return old_string
    return [old_string[:index], old_string[index:]]