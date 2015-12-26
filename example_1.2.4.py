import numpy as np
import matplotlib.pyplot as plt


def plot(x, y, a):
  plt.plot(x, y, 'ro')
  plt.axis(a)
  plt.show()


def ex_1_2_4():
  def f(x): 
    return (1 - (x-2)**2)**.5

  x_min=1
  x_max=3
  step=.001
  x_range = np.arange(x_min, x_max, step)
  y_range = [f(x) for x in x_range]
  xs = list(x_range) + list(x_range)
  ys = y_range + [-1*y for y in y_range]
  y_min = min(ys)
  y_max = max(ys)
  axis = [x_min-1, x_max+1, y_min, y_max+1]
  plot(xs, ys, axis)

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
    
ex_1_2_4()
 
