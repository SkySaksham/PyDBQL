from pathlib import Path
import shutil

def create_db(name) :
    folder = Path(name)
    if folder.exists() :
        raise FileExistsError(f"DATABASE '{name}' ALREADY EXISTS !! ")
    folder.mkdir () 
    (folder/"tables").mkdir()
    (folder/"tables.txt").write_text("")
    print (f"DATABASE {name} CREATED SUCCESSFULLY !!")


def drop_db(name) :
    folder = Path(name) 

    if not folder.exists() :
        raise FileNotFoundError(f"DATABASE '{name}' DOES NOT EXIST !!")
    
    else :
        get_name = input ("CONFIRM THE NAME :")
        if get_name != name : 
            raise ValueError("NAME DID NOT MATCH !! ABORTED !!")
        
        delete = input (f"TYPE 'DELETE {name}' TO CONFIRM : ")
        if delete != f"DELETE {name}" : 
            raise ValueError ("TEXT DID NOT MATCH ! ABORTED !!")
         
        shutil.rmtree(name)
        print (f"DATABASE '{name}' DELETED SUCCESSFULLY !!")
