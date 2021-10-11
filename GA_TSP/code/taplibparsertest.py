from tsplibparser import TSPLIBParser
import sys


sys.path.append("..")
print(TSPLIBParser('../data/berlin52.tsp.txt').parse())
