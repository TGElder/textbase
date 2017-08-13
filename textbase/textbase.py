import sqlite3
import csv
from os import listdir,makedirs,remove
from os.path import isfile,join,exists
from shutil import copyfile

class Textbase:

    BACKUP_DIRECTORY = "old"
    
    database = None
    cursor = None    
    directory = None
    tables = None
    headers = {}
    
    def __init__(self,directory):
            
        self.database = sqlite3.connect(":memory:")
        self.cursor = self.database.cursor();
        self.directory = directory
        self.tables = []
        self.columns = {}

        for file in listdir(directory):

            if isfile(join(directory,file)) and file.endswith(".csv"):
                
                table = file[:-4]
                self.tables.append(table)
                
                csv_file = open(join(directory,file), 'r')
                csv_reader = csv.reader(csv_file)
                
                header = next(csv_reader)
                
                self.headers[table] = header
            
                csv_file.close()

                field_string = ""
                delimiter = ""
                
                for field in header:
                    field_string += delimiter + "_"+field + " text"
                    delimiter = ","
                
                    
                query = "create table "+table
                query += " ("+field_string+")"
                
                self.cursor.execute(query)
                  
        self.load()
    
    def load(self):
        for table in self.tables:
            query = "delete from "+table
            self.cursor.execute(query)
            
            csv_file = open(join(self.directory,table+".csv"), 'r')
            csv_reader = csv.reader(csv_file)
            
            # Skip header
            next(csv_reader)
            
            header = self.headers[table]
      
            for row in csv_reader:
                field_string = ""
                delimiter = ""
                
                values = []
                
                for f in range(0,len(header)):
                    
                    if f>=len(row):
                        value = None
                    else:
                        if not row[f]:
                            value = None
                        else:
                            value = row[f]

                    
                        
                    values.append(value)
                                            
                    field_string += delimiter + "?"
                    delimiter = ","
                    
                query = "insert into "+table+" values "
                query += "("+field_string+")"


                self.cursor.execute(query,tuple(values))
   
                
            csv_file.close()

    def save(self):
        
        if not exists(join(self.directory,self.BACKUP_DIRECTORY)):
            makedirs(join(self.directory,self.BACKUP_DIRECTORY))
        
        for table in self.tables:
            
            file = join(self.directory,table+".csv")
            old = join(self.directory,self.BACKUP_DIRECTORY,table+".csv")
            
            if exists(old):
                remove(old)
                
            copyfile(file,old)
            
            csv_file = open(file, "w", newline='')
            csv_writer = csv.writer(csv_file)

            self.cursor.execute("select * from "+table)
            
            columns = [column[0][1:] for column in self.cursor.description]
            
            csv_writer.writerow(columns)
            
            rows = self.cursor.fetchall()
  
            csv_writer.writerows(rows)
            
            csv_file.close()