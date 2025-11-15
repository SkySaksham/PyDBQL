# Attempts to make a query Language

# commands so far

# checkout :<database_name>
# checkout 
# drop :database :<database_name>
# drop :<database_name>
# show :database
# get :<table_name>
# get :<table_name :where :<column_name> :is :<entry>

import sys
from pathlib import Path
import os

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parent.parent))


from src import add_data as ad
from src import create_table as ct
from src import draw_table as dt
from src import drop_and_create_db as cd


command = ["checkout","get","create","drop","show"]
command_2nd = ["database","table"]



database = None
all_tables = []
space = "        "

def get_database() :
    base_dir = Path(__file__).parent / "../db"
    folders = [["", f, ""] for f in os.listdir(base_dir) if (base_dir / f).is_dir()]
    width = 8
    for i in range (len(folders)) :
        folders[i][0] = str(i+1)
        if len(folders[i][1]) > width : width = len(folders[i][1]) 
        if folders[i][1] == database : folders[i][2] = "TRUE" 
    
    width_list = [4,width,8]

    #print (width_list)
    
    table = [["S.no","Database","Selected"]] + folders

    dt.draw_table(table,width_list)


def get_all_tables(database) :

    all_tables = []

    base_direc = (Path(__file__).parent)
    with open(base_direc/f"../db/{database}/tables.txt") as metadata :
        for index,line in enumerate(metadata,start=1) :
            if index%4 == 1 : 
                line.strip("\n")
                all_tables.append(line.split(":")[0])
    
    return all_tables

#print(get_all_tables("hello"))



def show_table(x) :
    if database == None : print (space,"NO DATABASE SELECTED !!")
    else :
        size = [6,14]
        data = [["Sno.","Table"]]
        for i,j in enumerate(x,start=1) :
            data.append([str(i),j])
    dt.draw_table(data,size)

def initiate(name) :
    global database
    global all_tables
    database = name
    all_tables=get_all_tables(database)

    
    print (f"{space} SELECTED DATABASE : {name} ")
    #print ()

def check_db (database) : 
    if database == None : print (space,"NO DATABASE SELECTED !!")
    else : print (space,f"YOU ARE ON DATABASE : '{database}'")
    #print()

def get_table(name,column=None,entry=None) :
    if database == None : print (space,"NO DATABSE SELECTED YET !! ABORTED !!")
    else :
        dt.draw(database,name,column,entry)

def add_table(database,table_name,table_data_raw_string) :
    global all_tables
    if database == None : print (space,"NO DATABSE SELECTED YET !! ABORTED !!")
    elif table_name in all_tables : raise Exception (f"TABLE '{table_name}' IS ALREADY PRESENT IN '{database}'")
    else :
        all_tables+=[table_name]
        raw_table_data = table_data_raw_string[1:-1]

        data = ad.table_info(raw_table_data)
        ct.create_table(database,table_name,data)


def parser(query_string) :
    query = query_string.split(" :")

    if query [0] == command [0] :
        if len(query) == 1 : check_db(database)
        else : initiate(query[1])
    elif query [0] == command [1] :
        try :
            if len(query) == 1 : raise Exception("TABLE NOT SELECTED")
            else : 
                if len(query) == 2 : dt.draw(database,query[1])
                elif (len(query) == 6) and query[2] == "where" and query[4]=="is" : dt.draw(database,query[1],query[3],query[5])
                else : raise Exception(f"INVALID SYNTAX :: '{query_string}'")

        except Exception as e : print(e)
    elif query [0] == command [2] :
        if query[1] == command_2nd[0] :
            try : cd.create_db(query[2],space)
            except Exception as e : print(e)
        elif query[1] == command_2nd[1] :
            if len(query)==4 :
                table_name=query[2]
                add_table(database,table_name,query[3])
                print(space,f"Table {table_name} CREATED SUCCESFULLY !!")
            else :raise Exception(f"INVALID SYNTAX :: '{query_string}'")
        else :raise Exception(f"INVALID SYNTAX :: '{query_string}'")
    
    elif query [0] == command [3] :
        if query[1] == command_2nd[0] :
            try : cd.drop_db(query[2],space)
            except Exception as e : print(e)
        else :raise Exception(f"INVALID SYNTAX :: '{query_string}'")

    elif query [0] == command [4] :
        if query[1] == command_2nd[0]+"s" : get_database()
        elif query[1] == command_2nd[1]+"s": show_table(all_tables)
        else :raise Exception(f"INVALID SYNTAX :: '{query_string}'")

    else : raise Exception(f"INVALID SYNTAX :: '{query_string}'")

def run() :
    while True :
        print ()
        query = input("PyDBQL>> ")
        try : parser(query)
        except Exception as e : print(e)

