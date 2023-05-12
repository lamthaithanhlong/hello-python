# Cho số nguyên dương n. Kiểm tra xem n có phải là số hoàn thiện hay không
def bai30(n:int)->int:
  if(tonguocso(n)==n):
    return 1
  return 0

def tonguocso(n:int)->int:
  sum=0
  for i in range(1,n+1):
    if(n%i==0 and i!=n):
      sum+=i
  return sum
        