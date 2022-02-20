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

## Creating RDDs

```python
# from memory
nums = sc.parallelize([1,2,3,4])
# from file on the local file system, or on S3 or HDFS via s3n://, hdfs://
sc.textFile("file:///path/to/file") # os simply "/path/to/file" on Linux
# from Hive
hiveCtx = HiveContext(sc)
rows = hiveCtx.sql("SELECT name, age FROM users")
```

RDDs can also be created from:
- JDBC
- Cassandra
- HBase
- Elasticsearch
- JSON
- CSV
- sequence files
- object fies
- or other various compressed formats, such as Apache Parquet, Apache Avro, etc.

Methods for loading

1. Loading from memory
    - sc.parallelize(seq, numSlices), if ran locally, numSlices defaults to number of cores
    - sc.makeRDD() - 
    - sc.range()
1. Loading from file
    - sc.wholeTextFiles(path)
    - sc.sequenceFile()
    - sc.hadoopFile()
    - sc.newAPIHadoopFile() - for newAPI methods
    - sc.hadoopRDD()

## Transforming RDDs

Methods:
- map
- flatmap
- filter
- distinct
- sample
- union, intersection, subtract, cartesian

### Map example
```python
rdd = sc.parallelize([1, 2, 3, 4])
rdd.map(lambda x: x * x).collect()
# yields [1, 4, 9, 16]
```

## RDD Actions

- collect
- count
- countByValue
- take
- top
- reduce
- ...

