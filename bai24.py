# Liệt kê tất cả các “ước số lẻ” của số nguyên dương n
def bai24(n:int)->list:
  list=[]
  for i in range(1,n+1):
    if(n%i==0 and i%2!=0):
      list.append(i)
  return list