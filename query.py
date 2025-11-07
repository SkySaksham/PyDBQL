# Attempts to make a query Language


# current commands
# checkout:<database name>
# checkout 


database = None
space = "        "

def initiate(name) :
    global database
    database = name
    print (f"{space} SELECTED DATABASE : {name} ")
    print ()

def check_db (database) : 
    if database == None : print (space,"NO DATABASE SELECTED !!")
    else : print (space,f"YOU ARE ON DATABASE : '{database}'")
    print()

def parser(query_string) :
    query = query_string.split(":")
    command = ["checkout"]

    if query [0] == command [0] :
        if len(query) == 1 : check_db(database)
        else : initiate(query[1])

while True :
    print ()
    query = input("PyDBQL>> ")
    parser(query)