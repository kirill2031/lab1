def remove_duplicates(s):

    return ''.join(sorted(set(s), key=s.index))