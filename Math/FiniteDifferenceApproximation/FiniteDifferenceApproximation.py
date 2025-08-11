import math


def fin_dif_approximation(x, f, h, n):
    """
    Approximate derivative by taking x+h and x-h and getting their average.
    x: x
    f: function
    h: step from x
    n: derivative's power (0-4)
    """
    approx_derivatives = {
        0: f(x),
        1: (f(x+h)-f(x-h))/(2*h),
        2: (f(x+h)-(2*f(x))+f(x-h))/(h**2),
        3: (f(x - 2 * h) - 2 * f(x - h) + 2 * f(x + h) - f(x + 2 * h)) / (2 * h ** 3),
        4: (f(x + 2 * h) - 4 * f(x + h) + 6 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (h ** 4)
    }
    if n in (0,1,2,3,4):
        return approx_derivatives[n]
    else:
        raise ValueError("Provide n from 0 to 4")

# x = 4.0
# f = math.sqrt
# h = 0.1
# n = 4

# x = 1.0
# f = math.sin
# h = 1e-5
# n = 1

print(fin_dif_approximation(x,f,h,n))


