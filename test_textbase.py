from os.path import join,exists
from os.path import join,exists

def test_row_count(get_textbase):
    cursor = get_textbase.cursor
    
    cursor.execute("select count(*) from test_1")
    
    assert(cursor.fetchone()[0] == 3)
    
def test_value(get_textbase):
    cursor = get_textbase.cursor
    
    cursor.execute("select _column_b from test_1 where _column_a == '2'")
    
    assert(cursor.fetchone()[0] == "bravo")
       
def test_null_at_end(get_textbase):
    cursor = get_textbase.cursor
    
    cursor.execute("select _column_c from test_1 where _column_a == '1'")
        
    assert(cursor.fetchone()[0] is None)        
       
def test_null(get_textbase):
    cursor = get_textbase.cursor
    
    cursor.execute("select _column_b from test_1 where _column_a == '3'")
    
    assert(cursor.fetchone()[0] is None)        
    
def test_insert(get_textbase):
    cursor = get_textbase.cursor
    
    cursor.execute("select _column_b from test_2 where _column_a == '4'")
    
    assert(cursor.fetchone()[0] == "delta")   
    
def test_backup(get_textbase, get_test_directory):
    assert(exists(join(get_test_directory,get_textbase.BACKUP_DIRECTORY,"test_1.csv")))
    