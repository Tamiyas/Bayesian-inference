"""データ(xベクトルとyベクトル)を作る
"""
import numpy as np

class Data:
  def __init__(self, n = [3, 3], sigma = 1.0):
    self.prob  = [[0.6, 0.1], [0.1, 0.2]]
    self.sigma = sigma
    self.n_list= n
    self.x_vec = self.createXData()
    self.y_vec = self.createYData()

  def createXData(self):
    random = np.random.rand()
    if 0.0 <= random and random < 0.6:
      return [0, 0]
    if 0.6 <= random and random < 0.7:
      return [0, 1]
    if 0.7 <= random and random < 0.8:
      return [1, 0]
    if 0.8 <= random and random < 1.0:
      return [1, 1]


  def createYData(self):
    y_vec = []
    for (idx, num) in enumerate(self.n_list):
      y_vec.extend([np.random.normal(self.x_vec[idx], self.sigma ** 2, num)])
    return y_vec

  def Pr(self, x1, x2):
    return self.prob[x1][x2]

  def Pr_X1(self, x1):
    """X1の周辺確率を求める
    """
    prob = 0
    for x2 in range(0, 2):
      prob += self.prob[x1][x2]
    return prob

  def Pr_X2(self, x2):
    """X2の周辺確率を求める
    """
    prob = 0
    for x1 in range(0, 2):
      prob += self.prob[x1][x2]
    return prob

if __name__ == '__main__':
  data = Data()
  y_vec = data.y_vec
  print(y_vec)
  print(y_vec[0][1])
