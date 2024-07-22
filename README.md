## Appunti per corso introduttivo a Spark

Per provare gli esercizi nella cartella `exercises`

Installare Docker, scaricandolo da qui:  


### Testiamo pyspark con docker


```
docker build . -t spark-demo 
docker run -it --rm -p 8888:8888 -p 4040:4040 --hostname localhost spark-demo
```
```
/usr/local/spark/bin/pyspark
```
