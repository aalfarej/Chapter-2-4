P = 10000
r = .08
n = 12
t = float(input("how many years? "))

A = P * ( (1 + r/n) ** (n*t) )
print(A)
