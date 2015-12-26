import numpy as np
import matplotlib.pyplot as plt


def plot(x, y, a):
  plt.plot(x, y, 'ro')
  plt.axis(a)
  plt.show()


def ex_1():
  x = [0, -3, 4, -3]
  y = [0, 1, 2 , 2] 
  axis = [-5, 5, -1, 5]
  plot(x, y, axis)

def ex_2():
  x = range(-2, 4)
  x = np.arange(-2.0, 4.0, 0.01)
  y = [3 for i in x] 
  axis = [-5, 5, -1, 5]
  plot(x, y, axis)

def ex_3():
  x_min=-5
  x_max=5
  y_min=-1
  y_max=5
  (x,y) = gen_xy(1.0, 3.0, x_min, x_max, .2)
  axis = [x_min, x_max, y_min, y_max]
  plot(x, y, axis)

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
    
assert gen_xy(1.0, 2.0, 0.0, 1.0, .5) == ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0])
ex_3()
 
