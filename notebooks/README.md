## spark useful methods:
myRange = spark.range(1000).toDF("number")
divisBy2 = myRange.where("number % 2 = 0")
## action
divisBy2.count()


## an example
flightData2015 = spark\
.read\
.option("inferSchema", "true")\
.option("header", "true")\
.csv("/data/flight-data/csv/2015-summary.csv")

flightData2015.take(3)

## by default spark outputs 200 shuffle partitions
spark.conf.set("spark.sql.shuffle.partitions", "5")
flightData2015.sort("count").take(2)


## RDDs

RDD (Resilient Distributed Dataset)
DAG - directed acyclic graph of instructions for lazy operations
Transformations:
- map
- filter

Actions (which trigger DAG execution):
- collect
- count
- reduce
- take

RDDs are immutable (this is just the lineage, not the data driving it)

## Data loading

