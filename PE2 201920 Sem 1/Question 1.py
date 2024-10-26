def super_fib_R(term2, n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, term2]
    if n == 3:
        return [1, term2, term2+1]
    prev = super_fib_R(term2, n-1)
    return prev + [prev[-1]*2]

def super_fib_I(term2, upper):
    ans = [1]
    while True:
        next_term = -1
        if len(ans) == 1:
            next_term = term2
        elif len(ans) == 2:
            next_term = 1+term2
        else:
            next_term = ans[-1]*2
        if next_term > upper:
            break
        ans.append(next_term)
    return ans
  
def smallest_second(n):
    while n > 2 and n % 2 == 0:
        n //= 2
    return n-1