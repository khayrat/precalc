import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from math import pi


def plot(x, y, a):
  plt.plot(x, y, 'ro')
  plt.axis(a)
  plt.show()

def prepare_plot(xs, ys):
  x_min = min(xs)
  x_max = max(xs)
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

def ex_f(f, x_min=-10, x_max=10, excl=[], x_mirror=False, y_mirror=False, origin_mirror=False, step=0.01):
  xs = list(np.arange(x_min, x_max, step))
  xs = [x for x in xs if x not in excl]
  ys = [f(x) for x in xs]

  if x_mirror:
    xs = xs + xs
    ys = ys + [-y for y in ys]

  if y_mirror:
    xs = xs + [-x for x in xs] 
    ys = ys + ys

  if origin_mirror:
    xs = xs + [-x for x in xs] 
    ys = ys + [-y for y in ys]

  prepare_plot(xs, ys)

##########################################################
# Exercises
##########################################################

def ex_1():
  ps = [(-3,9), (-2,4), (-1,1), (0,0), (1,1), (2,4), (3,9)]
  xs = [x for x,y in ps]
  ys = [y for x,y in ps]
  step=.001
  prepare_plot(xs, ys, step)

def ex_2():
  ps = [(-2,0), (-1,1), (-1,-1), (0,2), (0,-2), (1,3), (1,-3)]
  xs = [x for x,y in ps]
  ys = [y for x,y in ps]
  step=.001

def ex_3():
  xs = [0, -1, 1, -2, 2]
  ys = [2*x for x in xs]
  prepare_plot(xs, ys)

def ex_4():
  ys = range(1,7)
  ys = ys + [-1*y for y in ys]
  xs = [6./y for y in ys]
  prepare_plot(xs, ys)

def ex_5():
  xs = range(0,2+1)
  xs = list(set(xs + [-1*x for x in xs]))
  print xs
  ys = [4-x**2 for x in xs]
  prepare_plot(xs, ys)

def ex_6():
  ys = [0, 1, 4, 9]
  xs = [sqrt(y) for y in ys]
  prepare_plot(xs, ys)

def ex_7():
  step=.01
  xs = np.arange(-4, 4, step)
  ys = [-2 for x in xs]
  prepare_plot(xs, ys)

def ex_8():
  step=.01
  xs = np.arange(-10, 4, step)
  ys = [3 for x in xs]
  prepare_plot(xs, ys)

def ex_9():
  step=.01
  ys = np.arange(1, 10, step)
  xs = [1 for y in ys]
  prepare_plot(xs, ys)

def ex_10():
  step=.01
  ys = np.arange(-10, 5, step)
  xs = [2 for y in ys]
  prepare_plot(xs, ys)

def ex_11():
  step=.01
  ys = np.arange(-3, 4, step)
  xs = [-2 for y in ys]
  prepare_plot(xs, ys)

def ex_12():
  step=.01
  ys = np.arange(-4, 3, step)
  xs = [-3 for y in ys]
  prepare_plot(xs, ys)

def ex_13():
  step=.01
  xs = np.arange(-2, 3, step)
  ys = [2 for x in xs]
  prepare_plot(xs, ys)

def ex_14():
  step=.01
  xs = np.arange(-4, 4, step)
  ys = [-3 for x in xs]
  prepare_plot(xs, ys)

def ex_15():
  step=.5
  # num num num num num -> ([num], [num])
  # expect(gen_xy(1.0, 2.0, 0.0, 1.0, .5) == 
  # ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], 
  #  [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]) 
  x_min=-2
  x_max=10
  y_min=-10
  y_max=10
  (xs, ys) = gen_xy(y_min, y_max, x_min, x_max, step)
  prepare_plot(xs, ys)

def ex_16():
  step=.5
  # num num num num num -> ([num], [num])
  # expect(gen_xy(1.0, 2.0, 0.0, 1.0, .5) == 
  # ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], 
  #  [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]) 
  x_min=-5
  x_max=3
  y_min=-10
  y_max=10
  (xs, ys) = gen_xy(y_min, y_max, x_min, x_max, step)
  prepare_plot(xs, ys)

def ex_17():
  step=.5
  # num num num num num -> ([num], [num])
  # expect(gen_xy(1.0, 2.0, 0.0, 1.0, .5) == 
  # ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], 
  #  [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]) 
  x_min=-10
  x_max=10
  y_min=-10
  y_max=4
  (xs, ys) = gen_xy(y_min, y_max, x_min, x_max, step)
  prepare_plot(xs, ys)

def ex_18():
  step=.5
  # num num num num num -> ([num], [num])
  # expect(gen_xy(1.0, 2.0, 0.0, 1.0, .5) == 
  # ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], 
  #  [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]) 
  x_min=-10
  x_max=3
  y_min=-10
  y_max=2
  (xs, ys) = gen_xy(y_min, y_max, x_min, x_max, step)
  prepare_plot(xs, ys)

def ex_19():
  step=.1
  # num num num num num -> ([num], [num])
  # expect(gen_xy(1.0, 2.0, 0.0, 1.0, .5) == 
  # ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], 
  #  [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]) 
  x_min=0
  x_max=10
  y_min=-10
  y_max=4
  (xs, ys) = gen_xy(y_min, y_max, x_min, x_max, step)
  prepare_plot(xs, ys)

def ex_20():
  step=.1
  # num num num num num -> ([num], [num])
  # expect(gen_xy(1.0, 2.0, 0.0, 1.0, .5) == 
  # ([0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0], 
  #  [1.0, 1.0, 1.0, 1.5, 1.5, 1.5, 2.0, 2.0, 2.0]) 
  x_min=-sqrt(2)
  x_max=2/3.
  y_min=pi
  y_max=9/2.
  (xs, ys) = gen_xy(y_min, y_max, x_min, x_max, step)
  prepare_plot(xs, ys)

def first():
  ex_19()
  ex_20()

#for e in es:
#  e()

##########################
# second
##########################

def ex_41():
  def f(x):
    return x**2 + 1

  step=.01
  xs = np.arange(-4, 4, step)
  ys = [f(x) for x in xs]

  prepare_plot(xs, ys)

def ex_42():
  def f(x):
    return x**2 - 2*x -8 

  step=.01
  xs = np.arange(-10, 10, step)
  ys = [f(x) for x in xs]

  prepare_plot(xs, ys)

def ex_43():
  def f(x):
    return x**3 - x

  step=.01
  xs = np.arange(-10, 10, step)
  ys = [f(x) for x in xs]

  prepare_plot(xs, ys)

def ex_44():
  def f(x):
    return (x**3)/4. - 3*x

  step=.01
  xs = np.arange(-10, 10, step)
  ys = [f(x) for x in xs]

  prepare_plot(xs, ys)

def ex_44_1():
  def f(x):
    return (x**3)/4. - 3*x

  ex_f(f)

def ex_45():
  def f(x):
    return sqrt(x-2)

  ex_f(f, x_min=2)

def ex_46():
  def f(x):
    return 2 * sqrt(x+4) -2

  ex_f(f, x_min=-4)

def ex_47():
  def f(x):
    return 3 * x - 7

  ex_f(f)

def ex_48():
  def f(x):
    return (3/2.) * x - 5

  ex_f(f)

def ex_49():
  def f(x):
    return sqrt(16 - (x + 2)**2)

  ex_f(f, x_min=-6, x_max=2, x_mirror=True)

def ex_50():
  def f(x):
    return sqrt(x**2 - 1)

  ex_f(f, x_min=1, x_max=4, x_mirror=True, y_mirror=True)

def ex_51():
  def f(x):
    return 3/2. * sqrt(4 + x**2)

  ex_f(f, x_mirror=True, y_mirror=True)

def ex_52():
  def f(x):
    return -4.0/x**3

  step=.2
  ex_f(f, x_min=-2, x_max=0, excl=[0], origin_mirror=True, step=step)

def second():
  ex_52()

second() 
