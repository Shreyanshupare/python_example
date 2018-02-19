import findspark
findspark.init()
import sys
from random import random
from operator import add
import pyspark
from pyspark import SparkConf, SparkContext
sc = pyspark.SparkContext("spark://192.168.xx.xx:7077", "job")

lines = sc.parallelize(["pandas", "i like pandas"])
print(lines.collect())
