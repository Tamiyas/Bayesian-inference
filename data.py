"""データ(xベクトルとyベクトル)を作る
"""
import numpy as np

class Data:
  def __init__(self, n = [3, 3], sigma = 1.0):
    self.x_vec = np.random.randint(0, 2, len(n))  # 0 or 1 のリストを作成
    self.y_vec = self.createYData(sigma, n)
    self.prob  = [[0.6, 0.1], [0.1, 0.2]]

  def createYData(self, sigma, n):
    y_vec = []
    for (idx, num) in enumerate(n):
      y_vec.extend(np.random.normal(self.x_vec[idx], sigma ** 2, num))
    return y_vec

  def getXVec(self):
    return self.x_vec

  def getYVec(self):
    return self.y_vec

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
