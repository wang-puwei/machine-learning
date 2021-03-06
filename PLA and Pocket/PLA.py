import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt


# 1、导入数据集
def loaddata():
    data1 = pd.read_csv("data1.csv",header = None)
    samples = data1.iloc[:,:2].values
    labels = data1.iloc[:,2].values
    return samples, labels


# 训练感知机模型
class Perceptron:
    def __init__(self, x, y, a=1):
        self.x = x
        self.y = y
        self.w = np.zeros((x.shape[1], 1))  # 初始化权重，w1,w2均为0
        self.b = 0
        self.a = 0.1  # 学习率
        self.numsamples = self.x.shape[0]
        self.numfeatures = self.x.shape[1]

    def sign(self, w, b, x):
        y = np.dot(x, w) + b
        return int(y)

    def update(self, label_i, data_i):
        tmp = label_i * self.a * data_i
        tmp = tmp.reshape(self.w.shape)
        # 更新w和b
        self.w = tmp + self.w
        self.b = self.b + label_i * self.a

    def train(self):
        isFind = False
        num = 0
        while not isFind:
            count = 0
            for i in range(self.numsamples):
                tmpY = self.sign(self.w, self.b, self.x[i, :])
                if tmpY * self.y[i] <= 0:  # 如果是一个误分类实例点
                    print('第',num,'次迭代误分类点为：', self.x[i, :], '此时的w和b为：', self.w, self.b)
                    count += 1
                    num += 1
                    self.update(self.y[i], self.x[i, :])
            if count == 0:
                print( '最终训练得到的w和b为：', self.w, self.b)
                isFind = True
        return self.w, self.b


# 画图描绘
class Picture:
    def __init__(self, data, w, b,l):
        self.b = b
        self.w = w
        plt.figure(1)
        plt.title('Perceptron Learning Algorithm', size=14)
        plt.xlabel('x0-axis', size=10)
        plt.ylabel('x1-axis', size=10)

        xData = np.linspace(0, 10, 100)
        yData = self.expression(xData)
        plt.plot(xData, yData, color='r', label='sample data')
        for i in range(0,len(l)):
            if (l[i]>0):
                plt.scatter(data[i][0], data[i][1],color='b', s=50)
            else:
                plt.scatter(data[i][0], data[i][1],color='g', s=50, marker='x')
        plt.savefig('PLA.png', dpi=75)

    def expression(self, x):
        y = (-self.b - self.w[0] * x) / self.w[1]  # 注意在此，把x0，x1当做两个坐标轴，把x1当做自变量，x2为因变量
        return y

    def Show(self):
        plt.show()


if __name__ == '__main__':
    start = time.time()
    samples, labels = loaddata()
    myperceptron = Perceptron(x=samples, y=labels)
    weights, bias = myperceptron.train()
    Picture = Picture(samples, weights, bias,labels)
    Picture.Show()
    costtime = time.time() - start
    print("Time used:", costtime)