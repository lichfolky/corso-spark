from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder.appName("hello-spark").getOrCreate()

textFile = spark.read.text("README.md")

print()
print("Righe sul file REAMDE.md:", textFile.count())
print()

# Crea un dataframe
data = [("Mattia", 10), ("Arturo", 20), ("Barbara", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
