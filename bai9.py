# Bài 9: Tính T(n) = 1 x 2 x 3…x N
def bai9(n: int)->int:
  sum=1
  for i in range(1,n+1):
    sum*=i
  return sum