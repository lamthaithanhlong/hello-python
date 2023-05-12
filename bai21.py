# Tính tổng tất cả các “ ước số” của số nguyên dương n
def bai21(n:int)->int:
  sum=0
  list=[]
  for i in range(1,n+1):
    if(n%i==0):
      sum+=i
  return sum
    
      