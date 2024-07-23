1 
---
D: Cos'è big data?

cosa vuol dire fare analisi big data:
- Grandi dataset
???

Spark è un sistema di calcolo ditribuito per processare dati big data 

high speed e in-memory processing

- batch processing, esempio:
???
- tempo reale, esempio:
???

detto anche streaming

Spark è veloce perché distribuisce i dati in clusters e li processa in parallelo e in memory
è un modello di calcolo distribuito

Perchè usare spark:
- molto robusto, fault tolerant
- in memory processing
- librerie per l'analisi e il processing
- api per java, scala, python e R
- compatibile con vari data framework e data sources

2 
---
Origini: hadoop e google


3
---
distributed computing

anche una sola macchina con multipli thread / processi

un cluster di computers


RDD resilient ditributed dataset - immutable, non tabulare, non ha schema nè datatype vengono usati internamente

4
---
Spark sessions per mandare comandi e ricevere risultati
ogni utente avrà la sua sessione, userà il cluster isolato dagli altri utenti

spark session comunica con spark context, master node nel cluster: coordina i nodi del cluster (i worker nodes)
per usarli deve allocare le risorse usando il cluster manager: responsabilie distribuisce le risorse del cluster

ogni workernode può eseguire più task contemporaneamente, ha una cache per salvare risultati

scrivi spark in notebook


5 alcuni comandi
---
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

Architettura
---




Stage
---
parallelize?

DAG
---
lazy execution
in base alle dipendenze riorganizzazione planning ahead


Due tipi di comandi
Transformations, aggiunte su dag ma eseguite dopo con azione, non cambiano dataframe input

Actions,execute dag non crea nuovo df
df.cache() se pensiamo di rieseguire dag, salvato in worker mem

con df.collect() salviamo in master node per non pullare
