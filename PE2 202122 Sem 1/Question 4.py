def child_DNA(d):
    ans = 1
    while d > 0:
        ans *= d % 10
        d //= 10
    return ans

def parent_mutated_DNA(d):
    src = child_DNA(d)
    digit = []
    while src >= 10:
        for x in range(9, 1, -1):
            if src % x == 0:
                digit.append(x)
                src //= x
                break
    digit.append(src)
    digit.sort()
    ans = 0
    for x in digit:
        ans = ans * 10 + x
    return ans


def isMartian(d):
    while True:
        can = False
        for x in range(2, 10):
            if d % x == 0:
                d //= x
                can = True
                break
        if not can:
            break
    if d >= 10:
        return False
    return True