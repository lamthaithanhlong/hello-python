# Liệt kê tất cả các “ước số” của số nguyên dương n
def bai20(n:int)->list:
  list=[]
  for i in range(1,n+1):
    if(n%i==0):
      list.append(i)
  return list