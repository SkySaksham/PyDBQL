from pathlib import Path
import shutil

def create_db(name,space="") :

    base_dir = (Path(__file__)).parent 
    if not (base_dir/"../db").exists() : (base_dir/"../db").mkdir()

    folder = (base_dir/f"../db/{name}")
    if folder.exists() :
        raise Exception(space+f" DATABASE '{name}' ALREADY EXISTS !! ")
    folder.mkdir () 
    (folder/"tables").mkdir()
    (folder/"tables.txt").write_text("")
    print (space+f" DATABASE {name} CREATED SUCCESSFULLY !!")

def drop_db(name,space="") :
    base_dir = (Path(__file__)).parent
    folder = (base_dir/f"../db/{name}") 

    if not folder.exists() :
        raise Exception(space+f" DATABASE '{name}' DOES NOT EXIST !!")
    
    else :
        get_name = input (space+" CONFIRM THE NAME :")
        if get_name != name : 
            raise Exception(space+" NAME DID NOT MATCH !! ABORTED !!")
        
        delete = input (space+f" TYPE 'DELETE {name}' TO CONFIRM : ")
        if delete != f"DELETE {name}" : 
            raise Exception (space+" TEXT DID NOT MATCH ! ABORTED !!")
         
        shutil.rmtree(folder)
        print (space+f" DATABASE '{name}' DELETED SUCCESSFULLY !!")

