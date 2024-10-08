def sum_digit_square_I(n):
    ans = 0
    while n > 0:
        ans += (n % 10) ** 2
        n //= 10
    return ans

def sum_digit_square_R(n):
    if n == 0:
        return 0
    return (n % 10) ** 2 + sum_digit_square_R(n // 10)

def is_happy_number(n):
    if n == 1 or n == 7:
        return True
    if n < 10:
        return False
    return is_happy_number(sum_digit_square_I(n))

def all_happy_number(n, m):
    ans = []
    for x in range(n, m + 1):
        if is_happy_number(x):
            ans.append(x)
    return ans