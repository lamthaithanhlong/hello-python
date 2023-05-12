# Tìm ước số lẻ lớn nhất của số nguyên dương n. Ví dụ n = 100 ước lẻ lớn nhất là 25
def bai29(n:int)->int:
  return max(uocso(n))

def uocso(n:int)->int:
  result=[]
  for i in range(1,n+1):
    if(n%i==0 and i%2!=0):
      result.append(i)
  return result

def max(list:list)->int:
  max=0
  for i in range(len(list)):
    if(list[i]>max):
      max=list[i]
  return max