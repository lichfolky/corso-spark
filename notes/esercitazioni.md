## Importiamo un csv
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction?resource=download
```
# read csv, all columns will be of type string
df = spark.read.option('header','true').csv('heart.csv')
# tell pyspark the type of the columns - saves time on large dataset. there are other ways to do this, but that's my favorite
schema = 'Age INTEGER, Sex STRING, ChestPainType STRING'
df = spark.read.csv('/Users/mreznik/heart.csv', schema=schema, header=True)
# let PySpark infer the schemadf = spark.read.csv('/Users/mreznik/heart.csv', inferSchema=True, header=True)
# replace nulls with other value at reading time
df = spark.read.csv('/Users/mreznik/heart.csv', nullValue='NA')
# save data
df.write.format("csv").save("heart_save.csv")
# if you want to overwrite the file
df.write.format("csv").mode("overwrite").save("heart_save.csv")
```

## Cambia minuscole in maiuscolo

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html
```
from pyspark.sql.functions import initcap

# Convert the first character to uppercase
df = df.withColumn("name", initcap(df["name"]))

df.show()
```

## Conta parole lunghezza


```
from pyspark.sql import functions as F
data = [("john",), ("alice",), ("bob",)]
df = spark.createDataFrame(data, ["name"])
df = df.withColumn('word_length', F.length(df.name))
df.show()
```

## Import file pandas

Importiamo da https://archive.ics.uci.edu/
e convertiamo panda in spark_df

```
# convert PySpark DataFrame to Pandas DataFrame
pd_df = df.toPandas()
# convert it back
spark_df = spark.createDataFrame(pd_df)
```


### Conta per lavoro

df.groupBy("job").count().show()

# evaluate a string expression into command
from pyspark.sql.functions import expr
exp = 'age + 0.2 * AgeFixed'
df.withColumn('new_col', expr(exp)).select('new_col').show(3)

### regressione lineare in?
https://www.youtube.com/watch?v=cZS5xYYIPzk


Usando beautiful soup (https://beautiful-soup-4.readthedocs.io/en/latest/) e il modulo request, ottenere la lista di elementi html di un sito web (tipo wikipedia) e trasformarli in dataframe, poi estrarre il link dell'elemento htlm usando le funzioni di spark (https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html)