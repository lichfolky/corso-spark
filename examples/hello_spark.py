from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder.appName("hello-spark").getOrCreate()

# Legge un file di testo
textFile = spark.read.text("files/tobenot.txt")
print("Righe sul file tobenot.txt:", textFile.count())
