from pyspark.sql import SparkSession
from pyspark.sql.functions import split
from operator import add

spark = SparkSession.builder.appName("WordCount").getOrCreate()

lines = spark.read.text("files/tobenot.txt").rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(add)
output = counts.collect()
for word, count in output:
    print("%s: %i" % (word, count))

spark.stop()
