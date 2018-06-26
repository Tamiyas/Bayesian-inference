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
        h += self.data.Pr(x1, x2) * np.exp(self.N(x1, x2))
    return h

  def N(self, x1, x2):
    w = 0
    x_vec = [x1, x2]
    y_vec = self.data.getYVec()
    n_list= self.data.getNList()
    for i in range(0, 2):
      for j in range(0, n_list[i]):
        w += (1 - 2 * y_vec[i][j] + 2 * y_vec[i][j] * x_vec[i] - x_vec[i] ** 2) / self.data.Pr(1, 1)
    return w

  def S_T(self):
    return 1 / self.h_T()

  def h_T(self):
    return 1 + self.data.Pr(0, 0) * np.exp(self.SN()) / self.data.Pr(1, 1)

  def SN(self):
    y_vec = self.data.getYVec()
    w = 0
    for i in range(0, 2):
      for j in range(0, 3):
        w += (1 - 2 * y_vec[i][j]) / 2
    return w

if __name__ == '__main__':
  data = Data()
  stat = Statistics(data)
  print(data.getXVec())
  print(stat.S_G())
  print(stat.S_T())
