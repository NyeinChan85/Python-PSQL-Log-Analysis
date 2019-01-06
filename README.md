# LOG ANALYSIS
--------------
## Description of the project
-----------------------------

This project a part of Udacity Fullstack developer Nano Degree. 
This project is designed to provide a great SQL skills practice expereince by building a SQL reporting tool interacting with a database with over a million rows, both from the command line and from the code itself. Python programming language (python3) and postgresql are used for this particular project. 


## Prerequisites
----------------

You must be familiar with the following before starting the project:

*	Python
*	PostgreSQL
*	Vagagrant
*	VirtualBox

## How to start setting up the Project
---------------------------------------

1.	Install Python3
2.	Install and Configure Vagrant and VirtualBox 
3.	Download or Clone the project from the github: 
    https://github.com/udacity/fullstack-nanodegree-vm
4.	Download and install newsdata.sql in our vagrant directory

## How to run the project
-------------------------

1.	Change the directory to **vagrant**
2.	Launch the virtual machine by following command
    **$ vagrant up**
3.  Log into vitural machine by this command
	**$ vagrant ssh**
4.	Change the directory to **/vagrant**
5.	run the following command to load the data in local database
    **psql -d news -f newsdata.sql**
6.  Use this command to see the database-> **psql -d news**
7.  Database contains 3 tables (authors, articles, and log) and to explore 
    each one, use the following commands:
    **\dt** (note: that will display a list of tables that the database contains)
    **\d table**(note: replace table with actual table name)
8.  Use the below command to run the program
    **python log.py**

## Creating the view
---------------------

A view, a virtual table based on the result-set of a postgre sql statement, is created for this project.
Create the view as follows.

*Create view popular_articles_view as select title, count(*) as views from articles join log on log.path=CONCAT('/article/',articles.slug) group by articles.author, articles.title order by views DESC;*



