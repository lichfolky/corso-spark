from pyspark.sql import SparkSession, Column, DataFrame
from pyspark.sql.functions import substr, substring
import requests

request = requests.get("https://www.wikipedia.com", verify=False)
spark = SparkSession.builder.appName("count-web-spark").getOrCreate()

## trasformo request.content in dataframe
## ??? df = request.content
## raggruppo le parole contando quante volte appaiono
