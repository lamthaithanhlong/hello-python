# Tính S(n) = x + x^2/1 + 2 + x^3/1 + 2 + 3 + … + x^n/1 + 2 + 3 + …. + N
def bai16(x: int, n: int) -> float:
  sum = 0
  for i in range(1, n + 1):
    sum += power(x, i)
  return sum


def power(x: int, n: int) -> float:
  pow = 1
  for i in range(n):
    pow *= x
  return float(pow)

