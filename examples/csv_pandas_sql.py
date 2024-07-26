from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
import pandas as pd


# Crea una sessione Spark
spark = SparkSession.builder.appName("hello-spark").getOrCreate()
df_m = pd.read_csv("files/money.csv")
df_w = pd.read_csv("files/works.csv")

dfs_m = spark.createDataFrame(df_m)
dfs_w = spark.createDataFrame(df_w)

dfs_m.createGlobalTempView("money")
dfs_w.createGlobalTempView("works")

res = spark.sql(
    "select workclass,education,occupation,income from global_temp.money join global_temp.works on global_temp.money.index = global_temp.works.index"
)
exp = "income * 50"
res = res.withColumn("new_col", expr(exp)).select("new_col")
res.show()
