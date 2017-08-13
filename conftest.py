import pytest
import textbase.textbase
from shutil import copyfile,rmtree
from os import remove,makedirs
from os.path import join,exists

TEST_FILES = ["test_1.csv","test_2.csv"]
TEST_DATA_DIRECTORY = "test_data"
TEST_DIRECTORY = "test"

@pytest.fixture(scope="session")
def get_textbase():
    
    # Remove test directory
    if exists(TEST_DIRECTORY):
        rmtree(TEST_DIRECTORY)
    
    makedirs(TEST_DIRECTORY)
    
    # Populate test directory 
    for file in TEST_FILES:
        test_file = join(TEST_DIRECTORY,file)
            
        data_file = join(TEST_DATA_DIRECTORY,file)
        
        copyfile(data_file,test_file)
    
    tb = textbase.textbase.Textbase(TEST_DIRECTORY)
    
    tb.cursor.execute("insert into test_2 values ('4','delta','4.0')")
    tb.save()
    tb.load()
    
    return tb        

@pytest.fixture(scope="session")
def get_test_directory():
    return TEST_DIRECTORY