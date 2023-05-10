# Tính T(x, n) = x^n
def bai10(x: int,n: int) -> int:
  power = 1
  for i in range(1, n + 1):
    power*=x
  return power