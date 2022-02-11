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
conda create --name spark --channel conda-forge -y python=3.8 py4j numpy pandas pyarrow openjdk=8
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
