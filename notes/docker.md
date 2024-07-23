## Setup Spark

### installa estensioni:
- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

### Installa Docker

Attiva opzione:
"Add the *.docker.internal names to the host's /etc/hosts file (Requires password)"

### pySpark con Docker 
L'immagine docker ufficiale di spark con pyspark:
```
docker run -it -p 4040:4040 --hostname localhost --rm spark:python3 /opt/spark/bin/pyspark
```

### pySpark e jupyter con Docker

```
docker run -it --rm -p 8888:8888 --hostname localhost jupyter/pyspark-notebook
```

### Per usare gli esercizi con pySpark e jupyter
```
docker build . -t spark-demo 
docker run -it --rm -p 8888:8888 -p 4040:4040 --hostname localhost spark-demo
```
```
/usr/local/spark/bin/pyspark
```

https://docs.docker.com/reference/dockerfile/

## Comandi utili docker

### Attaccare shell  del container

```
docker ps

docker exec -it <mycontainer> bash
```


### Caricare file sul e dal container

```
docker cp src/. container_id:/target
docker cp container_id:/src/. target
```

### To create/change a root password in a running container

```
docker exec -itu 0 {container} passwd
```

### Set environment variables

You use ARG for settings that are only relevant when the image is being built, and aren't needed by containers which you run from the image. You can use ENV for environment variables to use during the build and in containers.

ES
```
ARG BUILD=test
ENV RUN_TIME=123
```
Es. for spark-docker:
https://github.com/apache/spark-docker/blob/master/OVERVIEW.md#environment-variable