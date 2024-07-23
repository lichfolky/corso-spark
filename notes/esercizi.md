## Importiamo un csv
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction?resource=download

**read csv, all columns will be of type string**
df = spark.read.option('header','true').csv('heart.csv')
**tell pyspark the type of the columns - saves time on large dataset. there are other ways to do this, but that's my favorite**
schema = 'Age INTEGER, Sex STRING, ChestPainType STRING'
df = spark.read.csv('/Users/mreznik/heart.csv', schema=schema, header=True)
**let PySpark infer the schema**
df = spark.read.csv('/Users/mreznik/heart.csv', inferSchema=True, header=True)
**replace nulls with other value at reading time**
df = spark.read.csv('/Users/mreznik/heart.csv', nullValue='NA')
**save data**
df.write.format("csv").save("heart_save.csv")
**if you want to overwrite the file**
df.write.format("csv").mode("overwrite").save("heart_save.csv")



## Import file pandas

Importiamo da https://archive.ics.uci.edu/
e convertiamo panda in spark_df
**convert PySpark DataFrame to Pandas DataFrame**
pd_df = df.toPandas()
**convert it back**
spark_df = spark.createDataFrame(pd_df)