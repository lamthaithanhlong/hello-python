# Tính S(n) = 1 + 1.2 + 1.2.3 + … + 1.2.3….N
def bai11(n: int) -> int:
  sum = 0
  multiple = 1
  for i in range(1, n+1):
    multiple *= i
    sum += multiple
  return sum