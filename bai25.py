# Tính tổng tất cả các “ước số chẵn” của số nguyên dương n
def bai25(n:int)->int:
  sum=0
  for i in range(1,n+1):
    if(n%i==0 and n%2==0):
      sum+=i
  return sum