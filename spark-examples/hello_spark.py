from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder.appName("hello-spark").getOrCreate()

textFile = spark.read.text("spark-examples/tobenot.md")
print("Righe sul file tobenot.txt:", textFile.count())

# Crea un dataframe
data = [("Mattia", 10), ("Arturo", 20), ("Barbara", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

"""
exec(open("spark-examples/hello_spark.py").read())
"""
