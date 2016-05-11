# spark
Set up apache spark on Amazon AWS

Open a connection to the server with using the hadoop user:
ssh -i ~/your_amazon_key.pem hadoop@ec2-XX-XX-XXX-XX.compute-1.amazonaws.com

Once connected to the Amazon machine type in the following lines in the terminal:

$ wget https://github.com/gterziysky/spark/blob/master/install_jupyter
$ chmod +x install_jupyter
$ ./install_jupyter

The installation might take a while. After it is done fire up a browser and connect to http://[ip addresses of your amazon system]:8192/. Now you are all set to run pyspark.
