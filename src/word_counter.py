#!/usr/bin/env python3

import logging
import os
from pyspark import SparkConf
from pyspark import SparkContext


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WordCounter(object):
	def __init__(self):
		pass
		conf = SparkConf().setAppName("Word Counter").setMaster("local[*]")
		sc = SparkContext.getOrCreate(conf.setMaster("local[*]"))

		textFile = sc.textFile("../README.md")
		logger.info(textFile.first())
		tokenizedFileData = textFile.flatMap(lambda line: line.split(" "))
		countPrep = tokenizedFileData.map(lambda word: (word, 1))
		counts = countPrep = countPrep.reduceByKey(lambda accumValue, newValue: accumValue + newValue)
		sortedCounts = counts.sortBy(lambda kvPair: kvPair[1], False)
		sortedCounts .saveAsTextFile("../data/ReadMeWordCountViaApp")


if __name__ == "__main__":
	logger.info("Hello")
	WordCounter()
	logger.info("Bye")
