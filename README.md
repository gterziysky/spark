# spark
Set up apache spark on Amazon AWS

Open a connection to the server using the hadoop user:
ssh -i ~/your_amazon_key.pem hadoop@ec2-XX-XX-XXX-XX.compute-1.amazonaws.com

Once connected to the Amazon machine type in the following lines in the terminal:

wget https://github.com/gterziysky/spark/blob/master/install_jupyter
chmod +x install_jupyter
./install_jupyter

The installation might take a while. After it is done fire up a browser and connect to http://[ip addresses of your amazon system]:8192/. Now you are all set to run pyspark.

## Install via conda

Possibly useful SO answer w.r.t. Spark env vars [How to import pyspark in anaconda](https://stackoverflow.com/questions/33814005/how-to-import-pyspark-in-anaconda#answer-33814715).

```shell
conda create --name spark --channel conda-forge -y python=3.8 py4j numpy pandas pyarrow openjdk=8 notebook
```

The current version of pyspark available on conda-forge for linux x64 is 2.4.0.

So to install the latest version (as of now 3.2.1) use:
```shell
pip install pyspark
```

or download it from [spark.apache.org](spark.apache.org) and set the env variables in your `~/.bashrc`:

```shell
export SPARK_HOME="/home/successful/spark-3.2.1-bin-hadoop3.2"
export PATH="$SPARK_HOME/bin:$PATH"
```

To remove the conda env simply:

```shell
conda env remove -n spark
```

To run a jupyter notebook on the server running spark do:

```shell
jupyter notebook --no-browser --port 1234
```

Open up a secure tunnel to the notebook server on your local machine:

```shell
# if you do not wish to start the ssh in the background, simply remove the -f option
ssh -i ~/.ssh/id_rsa -fNL 1234:localhost:1234 user@notebook_server
```

Then, go to your preferred browser of choice and type in localhost:1234 to open up jupyter notebook on the server (input the session token you got when starting up the jupyter notebook process on the server).

Finally, from within jupyter notebook, initiate a spark context by:

```python
import pyspark as ps
from pyspark import SparkContext
from pyspark import SparkConf

sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))
```

## Logging level

Navigate to the spark config folder:

```shell
# Note that the path to where you've installed spark may differ
cd ~/spark-3.2.1-bin-hadoop3.2/conf/
```

Make a copy of the log4j.properties.template file:
```shell
cp log4j.properties.template log4j.properties
```

Open the newly created `log4j.properties` file and set the logging level for the following properties from `INFO` or `WARN` to `ERROR`:

```shell
log4j.rootCategory
log4j.logger.org.apache.spark.repl.Main
log4j.logger.org.sparkproject.jetty
log4j.logger.org.apache.spark.repl.SparkIMain$exprTyper
log4j.logger.org.apache.spark.repl.SparkILoop$SparkILoopInterpreter
```

## Send 

The following code is from the "Running Production Applications" section of "Chapter 3. A tour of Spark's toolset" from the [Spark: The Definitive Guide: Big Data Processing Made Simple](https://analyticsdata24.files.wordpress.com/2020/02/spark-the-definitive-guide40www.bigdatabugs.com_.pdf) book:

```shell
# submit Python application to cluster
./bin/spark-submit \
  --master local \
  ./examples/src/main/python/pi.py 10
```