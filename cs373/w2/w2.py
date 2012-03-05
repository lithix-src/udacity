import math as m

def f(x, mu, sigma_sq):
    temp = ((x - mu)**2)/sigma_sq
    temp = m.exp(-.5 * temp)

    # normalization
    temp = 1/m.sqrt(2 * m.pi * sigma_sq) * temp
    return temp

print f(8., 10., 4.)
