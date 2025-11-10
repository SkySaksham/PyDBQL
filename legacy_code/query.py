# Attempts to make a query Language

# commands so far

# current commands
# checkout:<database_name>
# checkout 
# drop:database:<database_name>
# drop:<database_name>
# show:database


import os
import legacy_code.main as mp
import legacy_code.create_db as cd


command = ["checkout","get","create","drop","show"]
command_2nd = ["database"]



database = None
space = "        "

def get_database() :
    folders = [["",f,""] for f in os.listdir() if os.path.isdir(f) and f not in ["__pycache__",".git"]]
    width = 8
    for i in range (len(folders)) :
        folders[i][0] = str(i+1)
        if len(folders[i][1]) > width : width = len(folders[i][1]) 
        if folders[i][1] == database : folders[i][2] = "TRUE" 
    
    width_list = [4,width,8]

    #print (width_list)
    
    table = [["S.no","Database","Selected"]] + folders

    mp.draw_table(table,width_list)


    


def initiate(name) :
    global database
    database = name
    print (f"{space} SELECTED DATABASE : {name} ")
    print ()

def check_db (database) : 
    if database == None : print (space,"NO DATABASE SELECTED !!")
    else : print (space,f"YOU ARE ON DATABASE : '{database}'")
    print()

def get_table(name) :
    if database == None : print (space,"NO DATABSE SELECTED YET !! ABORTED !!")
    else :
        table,width = mp.get_rows(database,name)
        mp.draw_table(table,width)


def parser(query_string) :
    query = query_string.split(":")

    if query [0] == command [0] :
        if len(query) == 1 : check_db(database)
        else : initiate(query[1])
    if query [0] == command [1] :
        get_table(query[1])
    if query [0] == command [2] :
        if query[1] == command_2nd[0] :
            try : cd.create_db(query[2],space)
            except Exception as e : print(e)
    if query [0] == command [3] :
        if query[1] == command_2nd[0] :
            try : cd.drop_db(query[2],space)
            except Exception as e : print(e)
    if query [0] == command [4] :
        if query[1] == command_2nd[0] : get_database()


while True :
    print ()
    query = input("PyDBQL>> ")
    parser(query)
