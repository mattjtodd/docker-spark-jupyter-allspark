# Jupyter Spark Cluster

## Overview

This is an example project to demonstrate how to connect a Jupyter notebook to a remote spark cluster.  Typically in the all-spark notebook the clutser is embedded in the notebook and no external connections are made.  The cluster topology here allows for understanding the paralleism of sprk jobs locally.

## Getting started

* Install docker & docker compose (if needed)
* Clone the repo, run `docker-compose pull`
* Run `docker-compose up`

## Services published

* http://localhost:8080 - Jupyter Notebook
* http://localhost:5000 - Master Spark Node
* http://localhost:4040 - Spark Context
* http://localhost:8081 - Worker Node(s) loadbalanced if running in swarm mode / scaled compose

## Basic Setup

There's a sample dataset in the bind-mounted `/home/jovyan/data` path and an initial pyspark workbook in `/home/jovyan/work` to illustrate how to connect to the cluster.

## Image Lineage

* The image for the notebook are from the https://jupyter-docker-stacks.readthedocs.io/en/latest/ in this case the all-spark flavour.
* The images for the Spark nodes are handily published by a project from a couple of years ago but still maintained by Big Data Europe - https://www.big-data-europe.eu/.  The images are nbuilt from Git Repos here - https://github.com/big-data-europe and published to Docker Hub.  It's pretty easy to rebuild if you need to configure the spark boxes to add pythin libraries or even upgrade to Spark 4.5.0 if you're interested / brave!
