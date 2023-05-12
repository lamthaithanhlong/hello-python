# Tính S(n) = x + x^2/2! + x^3/3! + … + x^n/N!
def bai17(x: int, n: int) -> float:
  sum = 0
  for i in range(1, n + 1):
    pow = power(x, i)
    exp = exponent(i)
    sum += pow / exp
  return sum


def exponent(n: int) -> float:
  exp = 1
  for i in range(1, n + 1):
    exp *= i
  return exp


def power(x: int, n: int) -> float:
  pow = 1
  for i in range(n):
    pow *= x
  return float(pow)
