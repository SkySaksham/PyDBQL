from pathlib import Path
from src.encrypt_decrypt import encryption , decryption


def table_info (raw_string) :   # "Sno:[(key)]int[(<len>)]:name:()str[<len>]:money:[(key)]float[(<len>)]"
    columns = raw_string.split(":")

    #data_types = ["int","str","float"] 
    names , types , sizes , key = [],[],[],[]

    for i in range (0,len(columns),2) :
        names += [columns[i]]
        
    for i in range(1,len(columns),2) :
        chunk = columns[i]
        data = [False,"",14]
        if chunk.count("(") != chunk.count(")") : 
                raise Exception(f"INVALID SYNTAX '{chunk}' : CLOSE BRACKETS PROPERLY !! ")
        flag = chunk.count("(")

        if flag == 0 :
            if chunk in ["str","float","int"] : 
                data[1]=chunk
                data[2] = 14 
            
            else : raise Exception(f"INVALID SYNTAX '{chunk}' : DATA TYPE NOT DEFINED")
                
        elif flag == 1 :
            if chunk[0] != "(" :
                if chunk[0:3] in ["str","int"] :
                    data[1]=chunk[0:3] 
                    chunk = chunk[4:len(chunk)-1]
                    if chunk.isnumeric() :data[2] = int(chunk)
                    else : raise Exception (f"INVALID SYNTAX '{columns[i]}'")
                            
                elif chunk[0:5] == "float" :
                        data[1]=chunk[0:5] 
                        chunk = chunk[6:len(chunk)-1]
                        if chunk.isnumeric() :data[2] = int(chunk)
                        else : raise Exception (f"INVALID SYNTAX '{columns[i]}'")
                                   
            else :
                k = chunk.index(")")
                chunk = chunk[k+1 ::]
                data[0]= True

                if chunk in ["str","int","float"] :
                                data[1] = chunk
                                data[2] = 14
                else : raise Exception(f"INVALID SYNTAX '{chunk}' : DATA TYPE NOT DEFINED")

        elif flag == 2 :
            k = chunk.index(")")
            chunk = chunk[k+1 ::]
            data[0]= True

            if chunk[0:3] in ["str","int"] :
                data[1]=chunk[0:3] 
                chunk = chunk[4:len(chunk)-1]
                if chunk.isnumeric() :data[2] = int(chunk)
                else : raise Exception (f"INVALID SYNTAX '{columns[i]}'")
                            
            elif chunk[0:5] == "float" :
                data[1]=chunk[0:3] 
                chunk = chunk[4:len(chunk)-1]
                if chunk.isnumeric() :data[2] = int(chunk)
                else : raise Exception (f"INVALID SYNTAX '{columns[i]}'")

            else : raise Exception (f"INVALID SYNTAX '{columns[i]}'")

        else : raise Exception (f"INVALID SYNTAX '{columns[i]}'")
        if data[0] : key+=[names[int((i-1)/2)]] 
        types += [data[1]]
        sizes += [data[2]]
            
    return names , types , sizes , key


def fetch_table_info(database_name,file_name) :
    base_direc = (Path(__file__).parent)
    data = []
    with open(base_direc/f"../db/{database_name}/tables.txt") as table_info :
        flag = False 
        for index,line in enumerate(table_info,start=1) :
            line = line.strip()
            line = decryption(line)
            if (index%4) == 1 :
                if flag : break
                content = line.split(":")
                if content[0] != file_name : continue
                data.append(content)
                flag = True
            elif flag :
                content = line.split(":")
                data.append(content)
    if data == [] : raise Exception (f"NO TABLE NAMED '{file_name}' IS PRESENT !!")
    return data

def entry_validation(database_name, file_name, x):
    table_inf = fetch_table_info(database_name, file_name)
    key = table_inf[0][1::]
    size = len(table_inf[1])
    name = table_inf[1]
    datatype = table_inf[2]

    path = (Path(__file__).parent) / f"../db/{database_name}/tables/{file_name}.txt"

    if key != []:
        indexes = []
        keys = []
        for i in key:
            indexes.append(name.index(i))
            keys.append(set())

        with open(path) as data:
            for line in data:
                line = line.strip()
                line = decryption(line)
                if not line:
                    continue
                content = line.split(":")
                for i in range(len(indexes)):
                    keys[i].add(content[indexes[i]])

    for entry in x:
        print (entry)
        entry = entry.split(":")
        if len(entry) != size:
            raise Exception(f"INVALID SYNTAX !! '{entry}' MISMATCHED NUMBER OF COLUMNS")

        # Check datatype validity
        for j in range(size):
            if datatype[j] == "int":
                if not entry[j].lstrip("-").isdigit():
                    print(entry[j].lstrip("-"))
                    raise Exception(f"INVALID DATA TYPE !! COLUMN '{name[j]}' EXPECTS INT")
            elif datatype[j] == "float":
                try:
                    float(entry[j])
                except:
                    raise Exception(f"INVALID DATA TYPE !! COLUMN '{name[j]}' EXPECTS FLOAT")
            elif datatype[j] == "str":
                if not isinstance(entry[j], str):
                    raise Exception(f"INVALID DATA TYPE !! COLUMN '{name[j]}' EXPECTS STRING")

        # Check for duplicate keys
        for k in range(len(key)):
            value = entry[indexes[k]]
            if value in keys[k]:
                raise Exception(f"DUPLICATE KEY FOUND !! VALUE '{value}' FOR KEY '{key[k]}' ALREADY EXISTS")
            keys[k].add(value)

def add_entries(database_name,file_name,row) :

    entry_validation(database_name,file_name,row)
    base_direc = (Path(__file__).parent)
    for i in range(len(row)) : row[i]= encryption(row[i]) + "\n"

    #rows ---> [" "," "]

    with open(base_direc/f"../db/{database_name}/tables/{file_name}.txt","a") as file :
        file.writelines(row)


