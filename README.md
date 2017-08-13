# textbase
Python class for creating a in-memory SQLite database from a directory of csv files.

A directory is specified in the initialiser for the class. A table will be created for each file in the directory with the extension ".csv". Each csv file should have a header row with column names. Column names in the database are prefixed with an underscore to avoid clashing with reserved names. Text datatype is used for all columns. Empty values in rows are treated as null values.

The class has a load and save method. Load will repopulate the database from the csv files. Save will replace the csv files with the contents of the database. As a precaution, the existing csv files are backed up to the "out" directory before this happens.

## What is the point of this?

This is to enable SQL queries to be run over a collection of CSV files without the need to learn another language/library.