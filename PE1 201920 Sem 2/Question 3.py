from random import uniform

def distance_squared(a,b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2

def inside_circle(point, center, r):
    return distance_squared(point, center) <= r**2

def paint_area(S, C, D):
    top = (0, S/2 - D/2)
    right = (S/2 - D/2, 0)
    bottom = (0, -S/2 + D/2)
    left = (-S/2 + D/2, 0)
    m = 0
    n = 10000
    for _ in range(n):
        x = uniform(-S/2, S/2)
        y = uniform(-S/2, S/2)
        if (inside_circle((x, y), top, D/2) or
            inside_circle((x, y), right, D/2) or
            inside_circle((x, y), bottom, D/2) or
            inside_circle((x, y), left, D/2)) and not inside_circle((x, y), (0, 0), C/2):
            m += 1
    return m / n * S * S