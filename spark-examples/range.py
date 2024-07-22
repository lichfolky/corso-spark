# Import the necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder.appName("range").getOrCreate()

rdd = spark.sparkContext.parallelize(range(1, 100))

print("Sum: ", rdd.sum())
# Stop the SparkSession
spark.stop()
