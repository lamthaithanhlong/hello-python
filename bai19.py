# S(n) = 1 + x + x^3/3! + x^5/5! + … + x^(2n+1)/(2n+1)!
def bai19(x:int,n:int)->float:
  sum=1
  for i in range(0,n):
    exp = exponent(2*i+1)
    pow = power(x,2*i+1)
    sum+=pow/exp
  return float(sum)

def power(x:int,n:int)->float:
  pow=1
  for i in range(0,n):
    pow*=x
  return pow

def exponent(n:int)->float:
  exp=1
  for i in range(1,n+1):
    exp*=i
  return exp