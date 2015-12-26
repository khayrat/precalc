import numpy as np
import matplotlib.pyplot as plt


def plot(x, y, a):
  plt.plot(x, y, 'ro')
  plt.axis(a)
  plt.show()


def ex_1():
  def f(x): 
    r = (1 - x**2)
    return abs(r)**(1/3.0) * (1 if r > 0 else -1)

  x_min=-3
  x_max=3
  step=.0001
  x_range = np.arange(x_min, x_max, step)
  y_range = [f(x) for x in x_range]
  y_min = min(y_range)
  y_max = max(y_range)
  axis = [x_min-1, x_max+1, y_min-1, y_max+1]
  plot(x_range, y_range, axis)

# num num num num num -> ([num], [num])
# expect(gen_xy(1.0, 2.0, 0.0, 1.0, .5) == 
# ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], 
#  [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]) 
def gen_xy(y_min, y_max, x_min, x_max, step):
  y_range = np.arange(y_min, y_max+step, step)
  x_range = np.arange(x_min, x_max+step, step)
  y_dim = len(y_range)
  x = y_dim*list(x_range)
  y = []
  for i in range(y_dim):
    y += ([y_range[i] for k in x_range]) 
  return (x, y)
    
ex_1()
 
