def sum_of_3(L, n):
    memo = set(L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            src = n - L[i] - L[j]
            if src != L[i] and src != L[j] and src in memo:
                return True
    return False