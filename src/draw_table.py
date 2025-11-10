from pathlib import Path
import add_data as ad  

def draw_table (table,size) :

    def table_edge (size) :
        border = ""
        for i in size : border += f"+-{'-'*int(i)}-+" 
        print (border)

    def row_string(row,size,i) :
        if (len(str(row[i])) <= int(size[i])) :
            return  str(row[i])+" "*(int(size[i])-len(str(row[i])))
        else :
            return str(row[i])[0:size[i]]
        
    for i in range (len(table)) :
        row = table[i]
        table_edge(size)
        for j in range (len(row)) :
            data = row_string(row,size,j)
            print ("| " + data + " |",end="")
        print ()
    table_edge(size)

def fetch_rows(database_name,table_name,column=None,entry=None) :

    path = (Path(__file__).parent)

    name_n_key,row_head,datatypes,width = ad.fetch_table_info(database_name,table_name)


    def data_type_conversion (list_data,data_types) :
        for index,row in enumerate(list_data) :
            for i in range(len(row)) :
                if data_types[i] == "int" : list_data[index][i] =  int(list_data[index][i])
                elif data_types[i] == "float" : list_data[index][i] =  float(list_data[index][i])


    if (column==None) or (entry == None) :
        table=[]
        with open(path/f"../db/{database_name}/tables/{table_name}.txt") as file :
            for line in file :
                line=line.replace("\n","")
                row = line.split(":")
                table.append(row)
        data_type_conversion(table,datatypes)
        return row_head,table,width
        
    index = row_head.index(column)
    data = [] 
    with open(path/f"../db/{database_name}/tables/{table_name}.txt") as file :
        for line in file :
            line = line.replace("\n","")
            row_list = line.split(":")
            if row_list[index] == entry :
                data.append(row_list)
    data_type_conversion(data,datatypes)
    return row_head , data , width


'''head , data , width = fetch_rows("hello","user","sno","3")

a = [['sno', 'Name', 'balance'], [1, 'Saksham', 121.3], [2, 'user2', 1221.0], [3, 'Saksham', 90.0], [4, 'user2', 1221.0]]
draw_table([head]+data,width) '''

def draw(database_name,table_name,column=None,entry=None) :
    head , data , width = fetch_rows(database_name,table_name,column=None,entry=None)
    draw_table([head]+data,width)

#draw("hello","user")