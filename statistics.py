"""統計量を求めるクラス
"""
import numpy as np
from data import Data

class SG:
  def __init__(self, data):
    self.data = data

  def statistics(self):
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

class ST:
  def __init__(self, data):
    self.data = data

  def statistics(self):
    return 1 / self.h_T()

  def h_T(self):
    return 1 + self.data.Pr(0, 0) * np.exp(self.N()) / self.data.Pr(1, 1)

  def N(self):
    y_vec = self.data.getYVec()
    w = 0
    for i in range(0, 2):
      for j in range(0, 3):
        w += (1 - 2 * y_vec[i][j]) / 2
    return w


class SP:
  def __init__(self, data):
    self.data = data

  def statistics(self):
    return 1 / (self.PrX1GivenY1() * self.PrX2GivenY2())

  def PrX1GivenY1(self):
    n_list = self.data.getNList()
    return 1 + (self.data.Pr_X1(0) / self.data.Pr_X1(1)) * np.exp(self.N(n_list, 0))

  def PrX2GivenY2(self):
    n_list = self.data.getNList()
    return 1 + (self.data.Pr(1, 0) / self.data.Pr(1, 1)) * np.exp(self.N(n_list, 1))

  def N(self, n_list, idx):
    w = 0
    y_vec = self.data.getYVec()
    for j in range(n_list[idx]):
      w += (1 - 2 * y_vec[idx][j]) / 2
    return w

if __name__ == '__main__':
  data = Data()

  print(data.getXVec())
  print(data.getYVec())

  stat = SG(data)
  print(stat.statistics())

  stat = ST(data)
  print(stat.statistics())

  stat = SP(data)
  print(stat.statistics())
