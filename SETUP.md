## Install JDK 
https://www.oracle.com/java/technologies/downloads/

## Install spark

https://spark.apache.org/downloads.html

estrai, poi sposta cartella dove vuoi, rinominandola

## Installa in env

python -m venv .pyspark-env

activate it:
**Windows**
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
Linux and MacOS venv activation

Set-ExecutionPolicy Unrestricted -Scope Process

**Linux and MacOS**

source myvenv/bin/activate

## WIN env variables PATH 
https://phoenixnap.com/kb/install-spark-on-windows-10

variabili di ambiente
Path 

SPARK_HOME C:\Spark
%SPARK_HOME%\bin

### PySpark

Install with 'pip'

pip install pyspark
pip install findspark
pip install jupyterlab

pyspark
Use the official Docker image

docker run -it --rm spark:python3 /opt/spark/bin/pyspark

### Scala

https://get-coursier.io/docs/cli-installation

sbt
~run

https://docs.scala-lang.org/scala3/book/introduction.html
https://docs.scala-lang.org/tour/tour-of-scala.html

### Spark

https://spark.apache.org/downloads.html
