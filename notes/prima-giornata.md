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




5
---


Architettura
---




Stage
---
parallelize?