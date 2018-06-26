"""統計量を求めるクラス
"""
import numpy as np
from data import Data

class Statistics:
  def __init__(self, data):
    self.data = data

  def S_G(self):
    return 1 / self.h_G()

  def h_G(self):
    h = 0
    for x1 in range(0, 2):
      for x2 in range(0, 2):
        h += data.Pr(x1, x2) * np.exp(self.N(x1, x2))
    return h

  def N(self, x1, x2):
    w = 0
    x_vec = data.getXVec()
    y_vec = data.getYVec()
    n_list= data.getNList()
    for i in range(0, 2):
      for j in range(0, n_list[i]):
        w += (1 - 2 * y_vec[i][j] + 2 * y_vec[i][j] * x_vec[i]) / data.Pr(1, 1)
    return w

if __name__ == '__main__':
  data = Data()
  stat = Statistics(data)
  print(data.getXVec())
  print(stat.S_G())
