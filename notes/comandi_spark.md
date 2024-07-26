https://spark.apache.org/docs/latest/rdd-programming-guide.html



https://spark.apache.org/docs/3.5.1/sql-getting-started.html


df.head(3)
pd_df = df.toPandas()
df.select('Age').show(3)
df.select(['Age','Sex']).show(3)
df.count()
df.printSchema()
df.dtypes

# cast a column from one type to other
from pyspark.sql.types import FloatType
df = df.withColumn("Age",df.Age.cast(FloatType()))
df = df.withColumn("RestingBP",df.Age.cast(FloatType()))

df.select(['Age','RestingBP']).describe().show()
df.withColumnRenamed('Age','age').select('age').show(1)
df.filter('age > 18')
df.filter('age > 18').show()

# add another condition ('&' means and, '|' means or)
df.filter((df['age'] > 18) | (df['ChestPainType'] == 'ATA'))

# take every record where the 'ChestPainType' is NOT 'ATA'
df.filter(~(df['ChestPainType'] == 'ATA'))


df1.where(col("life_stage").isin(["teenager", "adult"])).show()

# Add a column to a Spark DataFrame
from pyspark.sql.functions import col, when

df1 = df.withColumn(
    "life_stage",
    when(col("age") < 13, "child")
    .when(col("age").between(13, 19), "teenager")
    .otherwise("adult"),
)

# evaluate a string expression into command
from pyspark.sql.functions import expr
exp = 'age + 0.2 * AgeFixed'
df.withColumn('new_col', expr(exp)).select('new_col').show(3)

# group by age
disease_by_age = df.groupby('age').mean().select(['age','avg(HeartDisease)'])

# run an SQL query on the data
df.createOrReplaceTempView("df") # tell PySpark how the table will be called in the SQL query
spark.sql("""SELECT sex from df""").show(2)

# we also choose columns using SQL sytnx, with a command that combins '.select()' and '.sql()'
df.selectExpr("age >= 40 as older", "age").show(2)

---

# predict 'RestingBP' using linear regression
from pyspark.ml.regression import LinearRegression
model = LinearRegression(featuresCol='Fvec', labelCol='MaxHR')
model = model.fit(trainset)
print(model.coefficients)
print(model.intercept)


Usando `LinearRegression` stimiamo  
from pyspark.ml.regression import LinearRegression
model = LinearRegression(featuresCol='Fvec', labelCol='MaxHR')
model = model.fit(trainset)

https://archive.ics.uci.edu/dataset/20/census+income



```
df.printschema()
df.dtypes
```
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/data_types.html
```
# cast a column from one type to other
from pyspark.sql.types import FloatType
df = df.withColumn("Price",df.Age.cast(FloatType()))
```
```
df.drop("Age)
df.withColumnRenamed('Age','age')

df.select(['Age','Sex']).show(3)
df.select(['Age','Sex']).describe().show()

df.filter("age>2")
# add another condition ('&' means and, '|' means or)
df.filter((df['age'] > 18) | (df['ChestPainType'] == 'ATA'))
# take every record where the 'ChestPainType' is NOT 'ATA'
df.filter(~(df['ChestPainType'] == 'ATA'))

df.groupby("age")

functions ha max, min e avg

pivot

df.groupby("age").pivot("sex").count()
```

UNION 

spark = SparkSession.builder.getOrCreate()

columns = ['id', 'dogs', 'cats']
vals = [(1, 2, 0), (2, 0, 1)]

df = spark.createDataFrame(vals, columns)

newRow = spark.createDataFrame([(4,5,7)], columns)
appended = df.union(newRow)
appended.show()