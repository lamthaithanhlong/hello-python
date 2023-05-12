# Tính tích tất cả các “ước số” của số nguyên dương n
def bai22(n:int)->int:
  multiply=1
  for i in range(1,n+1):
    if(n%i==0):
      multiply*=i
  return multiply