
pip freeze > requirements.txt
pip install -r requirements.txt

https://en.wikipedia.org/wiki/Clobbering


https://learn.microsoft.com/en-us/windows/wsl/basic-commands#set-wsl-version-to-1-or-2

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
 
 
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
