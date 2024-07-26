from pyspark import SparkContext

## https://spark.apache.org/docs/latest/rdd-programming-guide.html

# Create a SparkContext
spark = SparkContext("local", "test-context")

# resilient distribuited dataframe
rdd = spark.parallelize([1, 2, 3, 4, 5])

## rdd transformation (lazy)
add_rdd = rdd.map(lambda x: x + 1)

## rdd action
result = add_rdd.collect()

print("*" * 20)
print("Result: ", result)
print("*" * 20)

# Stop the SparkContext
spark.stop()
input("...press any key")
