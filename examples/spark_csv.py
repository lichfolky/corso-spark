from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder.appName("csv-spark").getOrCreate()
df = spark.read.option("header", True).csv("files/dati.csv")
df.show()

## Definisco uno schema string
schema = "Age INTEGER, Name STRING"
df = spark.read.csv("files/dati.csv", schema=schema, header=True)
df.show()
