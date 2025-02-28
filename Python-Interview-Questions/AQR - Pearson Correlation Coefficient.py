import math

def mean(x):
	return sum(x)/len(x)
	
def sd(x):
  m = mean(x)
  ss = sum((i-m) ** 2 for i in x)
  return math.sqrt(ss / len(x))

def corr(x, y):
  x_m = mean(x)
  y_m = mean(y)
  xy_d = [] # product of de-meaned X and Y, for covariance calc
  for i in range(len(x)):
    x_d = x[i] - x_m
    y_d = y[i] - y_m
    xy_d.append(x_d * y_d) # add product of X_i and Y_i 
  return mean(xy_d) / (sd(x) * sd(y)) # from formula above

"""
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
"""
