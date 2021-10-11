from TSP_GA import TSP
import sys
import argparse
from tsplibparser import TSPLIBParser

datasets = ['ppt20.tsp.txt', 'berlin52.tsp.txt', 'eil76.tsp.txt', 'kroA100.tsp.txt', 'kroB150.tsp.txt']
sys.path.append("..")
parser = argparse.ArgumentParser(description='Use GA to find solutions for the TSP.')
for dataset in datasets:
    path = '../data/' + dataset
    # print(path)
    data = TSPLIBParser(path).parse()
    aLifeCount = data['dimension']
    tsp = TSP(data, aLifeCount)
    tsp.run(500)
