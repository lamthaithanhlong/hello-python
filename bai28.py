# Cho số nguyên dương n. Tính tổng các ước số nhỏ hơn chính nó
def bai28(n:int)->int:
  sum=0
  for i in range(1,n+1):
    if(n%i==0 and i<n):
      sum+=i
  return sum
        
      