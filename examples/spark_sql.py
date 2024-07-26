from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder.appName("hello-spark").getOrCreate()

# Crea un dataframe
data = [("Mattia", 10), ("Arturo", 20), ("Barbara", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

df.createGlobalTempView("test")
res = spark.sql("select * from global_temp.test where Name != 'Arturo'")
res.show()
