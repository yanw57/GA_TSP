# -*- encoding: utf-8 -*-

import math
from GA import GA
import matplotlib.pyplot as plt


class TSP(object):
    def __init__(self, data):
        self.initCitys(data)
        self.lifeCount = 200
        self.ga = GA(aCrossRate=0.7,
                     aMutationRate=0.02,
                     aLifeCount=self.lifeCount,
                     aGeneLength=len(self.citys),
                     aMatchFun=self.matchFun())

    def initCitys(self, data):
        self.citys = []
        for node in data['node_coord_section']:
            self.citys.append((node['x'], node['y'], node['id']))

    # order是遍历所有城市的一组序列，如[1,2,3,7,6,5,4,8……]
    # distance就是计算这样走要走多长的路
    def distance(self, order):
        distance = 0.0
        # i从-1到32,-1是倒数第一个
        for i in range(-1, len(self.citys) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        return distance

    # 适应度函数，因为我们要从种群中挑选距离最短的，作为最优解，所以（1/距离）最长的就是我们要求的
    def matchFun(self):
        return lambda life: 1.0 / self.distance(life.gene)

    def run(self, n=0):
        bestfitness = []
        avgfitness = []
        worstfitness = []
        generation = n
        while n > 0:
            self.ga.next()
            bestdistance = self.distance(self.ga.best.gene)
            worstdistance = self.distance(self.ga.worst.gene)
            bestfitness.append(1.0 / bestdistance)
            worstfitness.append(1.0 / worstdistance)
            avg = self.ga.bounds / self.lifeCount
            avgfitness.append(avg)
            # print(("%d : %f") % (self.ga.generation, distance))
            # print(self.ga.best.gene)
            n -= 1
        # print("经过%d次迭代，最优解距离为：%f" % (self.ga.generation, distance))
        # print("遍历城市顺序为：")
        # # print "遍历城市顺序为：", self.ga.best.gene
        # # 打印出我们挑选出的这个序列中
        # for i in self.ga.best.gene:
        #     print(self.citys[i][2])

        # 数据图
        x = []
        y = []
        for i in range(len(self.citys)):
            coords = self.citys[i]
            x.append(coords[0])
            y.append(coords[1])
        plt.scatter(x, y, marker='o', facecolor='none', color='red', s=40)
        plt.title('GA_TSP_' + str(len(self.citys)))

        plt.show()

        # 最优解图示
        best_x = []
        best_y = []
        for i in self.ga.best.gene:
            best_x.append(self.citys[i][0])
            best_y.append(self.citys[i][1])
        plt.scatter(best_x, best_y, marker='o', facecolor='none', color='red', s=40)
        plt.plot(best_x, best_y)
        plt.title('GA_TSP_' + str(len(self.citys)))

        plt.show()

        # 适应度值随迭代次数变化图
        plt.plot(range(generation), bestfitness, 'r-', label="Maximum bestfitness")
        plt.plot(range(generation), avgfitness, 'g-', label="average bestfitness")
        plt.plot(range(generation), worstfitness, 'b-', label="Minimum bestfitness")
        plt.legend(loc="upper left")
        plt.xlabel('generation')
        plt.ylabel('BestFitness')
        plt.title('GA_TSP_' + str(len(self.citys)))

        plt.show()
