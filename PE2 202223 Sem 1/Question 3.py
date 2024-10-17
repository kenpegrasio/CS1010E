def min_no_of_turns(L):
    numbers = list(L)
    numbers.sort()
    cur = dict()
    for number in numbers:
        if (number-1) in cur and cur[number-1] > 0:
            cur[number-1] -=1
        if number in cur:
            cur[number] += 1
        else:
            cur[number] = 1
    return sum(x for x in cur.values())