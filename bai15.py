# Tính S(n) = 1 + 1/1 + 2 + 1/ 1 + 2 + 3 + ….. + 1/ 1 + 2 + 3 + …. + N
def bai15(n: int) -> int:
  sum = 0
  for i in range(1, n + 1):
    sum += 1 / 1 + mysum(i)
  return sum


def mysum(n: int) -> int:
  sum = 0
  for i in range(0, n):
    if (i != 1):
      sum += i
  return sum
