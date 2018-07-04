"""ROC曲線
"""

from data import Data
from statistics import SG
from statistics import ST
from statistics import SP
import matplotlib.pyplot as plt
from tqdm import tqdm

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

  def plotCurve(self, c = 'blue', l = 'Data'):
    FPR_list = []
    CDR_list = []
    n = {}
    for theta in tqdm(range(0, 101)):
      thresh = theta * 0.01
      n['x11']  = 0
      n['!x11'] = 0
      n['FP']   = 0
      n['CD']   = 0

      for alpha in tqdm(range(0, 100000)):
        stat = self.buildStat(Data())
        self.recognition(stat, thresh, n)
      FPR_list.append(self.FPR(n))
      CDR_list.append(self.CDR(n))
    plt.plot(FPR_list, CDR_list, color = c, lw = 0.8, label = l)
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.legend(loc="lower right")
    plt.savefig('ROC_curve.pdf')

  def plotCurveAll(self):
    method_list = ['SG', 'ST', 'SP']
    color_list  = ['black', 'tomato', 'deepskyblue']
    for idx, method in enumerate(method_list):
      self.method = method
      self.plotCurve(c = color_list[idx], l = method)

    plt.show()

  def recognition(self, stat, thresh, n):
    result = stat.statistics() > thresh
    x_vec = stat.data.x_vec
    if x_vec == [1, 1]:
      n['x11'] += 1
      n['CD']  += 1 if result == True else 0
    else:
      n['!x11'] += 1
      n['FP'] += 1 if result == True else 0

  def FPR(self, n):
    return n['FP'] / n['!x11']

  def CDR(self, n):
    return n['CD'] / n['x11']

if __name__ == '__main__':
  curve = ROC('SG')
  curve.plotCurveAll()
