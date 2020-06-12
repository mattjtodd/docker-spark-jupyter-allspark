import random
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf


def inside(p):
    x, y = random.random(), random.random()
    return x * x + y * y < 1


if __name__ == "__main__":
    print("Instantiate the Spark Context")
    conf = SparkConf() \
        .setMaster('spark://spark-master:7077') \
        .setAppName('spark-pi')
    sc = SparkContext(conf=conf)

    num_samples = 1000
    count = sc.parallelize(range(0, num_samples)) \
        .filter(inside) \
        .count()

    print("Pi is roughly %f" % (4.0 * count / num_samples))
    sc.stop()


