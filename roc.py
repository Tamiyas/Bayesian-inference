"""ROC曲線
"""

from data import Data
from statistics import SG
from statistics import ST
from statistics import SP
import matplotlib.pyplot as plt

class ROC:
  def __init__(self, method = 'SG'):
    self.method = method

  def buildStat(self, data):
    if self.method == 'SG':
      return SG(data)
    if self.method == 'ST':
      return ST(data)
    if self.method == 'SP':
      return SP(data)
    return SG(data)

  def plotCurve(self):
    FPR_list = []
    CDR_list = []
    for theta in range(0, 100):
      thresh = theta * 0.01
      n_FP  = 0
      n_CD  = 0
      n_x11 = 0

      for alpha in range(0, 100000):
        stat = self.buildStat(Data())
        self.recognition(stat, thresh, n_FP, n_CD, n_x11)
      FPR_list.append(self.FPR(n_FP, n_x11))
      CDR_list.append(self.CDR(n_FP, n_x11))
    plt.plot(FPR_list, CDR_list)
    plt.show()


  def recognition(self, stat, thresh, n_FP, n_CD, n_x11):
    result = stat.statistics() > thresh
    x_vec = stat.getData().getXVec()
    if x_vec == [1, 1]:
      n_x11 += 1
      n_CD  += 1 if result == True else 0
    else:
      n_FP += 1 if result == True else 0

  def FPR(self, n_FP, n_x11):
    return n_FP / n_x11

  def CDR(self, n_CD, n_x11):
    return n_CD / n_x11

if __name__ == '__main__':
  curve = ROC('SG')
  curve.plotCurve()
