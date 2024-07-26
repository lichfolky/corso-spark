from pyspark.sql import SparkSession, Column, DataFrame
from pyspark.sql.functions import *
import requests

request = requests.get("https://www.wikipedia.com", verify=False)
spark = SparkSession.builder.appName("count-web-spark").getOrCreate()


## trasformo request.content in dataframe
words = str(request.content).split()


tuples = [(word, 1) for word in words]
print(tuples)
df = spark.createDataFrame(tuples, ["word", "count"])

## raggruppo le parole contando quante volte appaiono
df = df.groupby("word").agg(sum("count").alias("count")).sort(col("count").desc())

df.show(100)
