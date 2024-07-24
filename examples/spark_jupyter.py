# Set the PySpark environment variables
import os

os.environ["SPARK_HOME"] = "/Users/coder2j/Apps/Spark"
os.environ["PYSPARK_DRIVER_PYTHON"] = "jupyter"
os.environ["PYSPARK_DRIVER_PYTHON_OPTS"] = "lab"
os.environ["PYSPARK_PYTHON"] = "python"

# Import PySpark
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("jupyter").getOrCreate()
# Test the setup
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
