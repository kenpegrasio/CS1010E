
def auspicious_number(n, bad):
    non_zero = len(bad) - (0 in bad)
    zero = 0 in bad
    return (9 - non_zero) * (10 - non_zero - zero) ** (n - 1)
    