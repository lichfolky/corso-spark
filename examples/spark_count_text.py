from pyspark.sql import SparkSession
from pyspark.sql.functions import split
from utils import tokenize

spark = SparkSession.builder.appName("spark").getOrCreate()
textFile = spark.read.text("examples/files/tobenot.txt")
df = spark.createDataFrame(textFile)

print(textFile)

split(textFile, " ")

# Display Output
textFile.display()
