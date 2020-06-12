# Jupyter Spark Cluster

## Overview

This is an example project to demonstrate how to connect a Jupyter notebook to a remote spark cluster.  Typically in the all-spark notebook the clutser is embedded in the notebook and no external connections are made.  The cluster topology here allows for understanding the paralleism of spark jobs locally.

## Getting started

* Install docker & docker compose (if needed)
* Clone the repo, run `docker-compose pull`
* Run `docker-compose up`

## Services published

* http://localhost:8888 - Jupyter Notebook
* http://localhost:5000 - Master Spark Node
* http://localhost:4040 - Spark Context
* http://localhost:8081 - Worker Node(s) loadbalanced if running in swarm mode / scaled compose

## Basic Setup

There's a sample dataset in the bind-mounted `/home/jovyan/data` path and an initial pyspark workbook in `/home/jovyan/work` to illustrate how to connect to the cluster. <br>
You will also be able to see a small python script `calc-pi.py` available on the `home/jovyan/script` volume in the master node.
This can be used to submit a job to the cluster as below: <br>

## Basic job execution

Once the docker containers are up and running, you can execute the following to submit a job to your local cluster: <br>
`docker-compose exec spark-master /spark/bin/spark-submit --conf spark.pyspark.python=python3 /home/jovyan/script/calc-pi.py` <br>
This runs the spark submit command on the spark-master service. <br>
If you navigate to the spark master node `http://localhost:5000` you should be able to see a completed application visible in the UI. <br>

## Image Lineage

* The image for the notebook are from the https://jupyter-docker-stacks.readthedocs.io/en/latest/ in this case the all-spark flavour.
* The images for the Spark nodes are handily published by a project from a couple of years ago but still maintained by Big Data Europe - https://www.big-data-europe.eu/.  The images are built from Git Repos here - https://github.com/big-data-europe and published to Docker Hub.  It's pretty easy to rebuild if you need to configure the spark boxes to add pythin libraries or even upgrade to Spark 4.5.0 if you're interested / brave!
