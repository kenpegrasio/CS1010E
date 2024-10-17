def is_unique(seq):
    length = sum(1 for _ in seq)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if seq[i] == seq[j]:
                return False
            j += 1
        i += 1
    return True