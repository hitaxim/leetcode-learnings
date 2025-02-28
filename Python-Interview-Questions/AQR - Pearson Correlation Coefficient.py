import math

def corr(x, y):
  
  def mean(x):
    return sum(x) / len(x)
    
  def stdev(x):
    m = mean(x)
    ss = sum([(i-m)**2 for i in x])
    return math.sqrt(ss/len(x))
  
  def cov(x, y):
    mean_x, mean_y = mean(x), mean(y)
    n = len(x)
    return (1/n)*sum([(x[i] - mean_x)*(y[i] - mean_y) for i in range(n)])
    
  def sqrt_var(x):
    return math.sqrt(stdev(x))
  
  res = cov(x,y) / (sqrt_var(x) * sqrt_var(y))
  return res
