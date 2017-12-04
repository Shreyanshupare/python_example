import findspark
findspark.init()
import sys
from random import random
from operator import add
import pyspark
from pyspark import SparkContext
from pyspark import SparkFiles
sc = pyspark.SparkFiles("spark://192.168.1.68:7077","pare")

file = sc.textFile("C:/home/bizruntime41/Download/spark-2.1.0-bin-hadoop2.7/README.md")
print(file.first())
#sc = pyspark.SparkContext("spark://192.168.1.68:7077",file)
##lines = sc.parallelize(["pandas", "i like pandas"])
##data = open(file,'r')
##print(data.getRootDirectory())

