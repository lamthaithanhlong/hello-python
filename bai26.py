# Tính tích tất cả các “ước số lẻ” của số nguyên dương n
def bai26(n: int)->int:
  multiply=1
  for i in range(1,n+1):
    if(n%i==0 and i%2!=0):
      multiply*=i
  return multiply