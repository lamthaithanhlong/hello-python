# Đếm số lượng “ước số chẵn” của số nguyên dương n
def bai27(n:int)->int:
  count=0
  for i in range(1,n+1):
    if(n%i==0 and i%2==0):
      count+=1
  return count