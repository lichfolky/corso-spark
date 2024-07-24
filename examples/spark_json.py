from pyspark.sql import SparkSession

# per semi structured data
# Crea una sessione Spark
spark = SparkSession.builder.appName("json-spark").getOrCreate()

## None è propriamente un json, https://jsonlines.org/examples/
df = spark.read.json("files/logs.json")
print("SCHEMA:")
df.printSchema()
df.where("age > 21").select("name.first").show()
