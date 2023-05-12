# Tính S(n) = 1 + x^2/2! + x^4/4! + … + x^2n/(2n)!
def bai18(x: int, n: int) -> float:
  sum = 0
  for i in range(0, n):
    exp = exponent(2 * i)
    pow = power(x, 2 * i)
    sum += pow / exp
  return sum


def power(x: int, n: int) -> float:
  pow = 1
  for i in range(0, n):
    pow *= x
  return pow


def exponent(n: int) -> float:
  exp = 1
  for i in range(1, n + 1):
    exp *= i
  return exp
