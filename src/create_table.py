from pathlib import Path


def convert(x) : #(["",""],["",""],[,,],[]) --> [" "," "," "] , for writelines()
        res = []
        for i in x :
            element = ""
            if i == x[-1] : pass
            if i != x[-1] :
                for j in i :
                        element+=str(j)
                        if j != i[-1] : element += ":"
                        else : element+="\n"
                res.append(element)
        return res


def create_table(database_name,name,data) : 

    # data --> ([],[],[],[]) , right out of table_info() in add_data.py
    key = data [3]

    table_data = [f"{name}"] 
    
    for i in key :
        if i != "" :      
            table_data[0]+= ":"
            table_data[0]+=i
            if i == key[-1] : table_data[0] += "\n"
        elif len(key)==1 or i == key[-1]: table_data[0] += "\n"

    table_data += convert(data)

    print(table_data)
    base_direc = Path(__file__).parent
    path = (base_direc/f"../db/{database_name}")


    with open(path/"tables.txt","a") as tables :
        tables.writelines(table_data)
    with open(path/f"tables/{name}.txt","w") as file :
        pass
  