def is_unique(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] == seq[j]:
                print(i, j)
                return False
    return True