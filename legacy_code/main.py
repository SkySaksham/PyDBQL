def get_content (database_name,filename) :
    table = []
    with open(f"{database_name}/tables/{filename}.txt","r") as data :
        for line in data :
            line=line.replace("\n","")
            row = line.split(":")
            table.append(row)
    return table

def get_table_info(database_name,table_name) :

    rowhead_size = [["Row Head"],["Size"]]

    with open(f"{database_name}/tables.txt") as table_data :
        flag = 0 
        for line in table_data :
            line = line.replace("\n","")
            
            if line == table_name :
                flag = 1

            elif flag == 1 :
                rowhead_size[0]=line.split(":")
                flag = 2

            elif flag == 2 :
                rowhead_size[1]=list(map(int,line.split(":")))
                break
    return rowhead_size

def get_blank_row(size) :
    row = [""]*len(size)
    return row

def draw_table (table,size) :

    def table_edge (size) :
        border = ""
        for i in size : border += f"+-{'-'*i}-+" 
        print (border)

    def row_string(row,size,i) :
        if (len(row[i]) <= size[i]) :
            return  row[i]+" "*(size[i]-len(row[i]))
        else :
            return row[i][0:size[i]]
        
    for i in range (len(table)) :
        row = table[i]
        table_edge(size)
        for j in range (len(row)) :
            data = row_string(row,size,j)
            print ("| " + data + " |",end="")
        print ()
    table_edge(size)

def get_data(database_name,file_name) :
    head_size = get_table_info(database_name,file_name)
    table = [head_size[0]] + get_content(database_name,file_name)
    return table,head_size[1]

def get_rows(database_name,table_name,column=None,entry=None) :

    if (column==None) or (entry == None) :
        return get_data (database_name,table_name)
    

    row_head , width = get_table_info (database_name,table_name)
    index = row_head.index(column)
    data = [] 
    with open(f"{database_name}/tables/{table_name}.txt") as file :
        for line in file :
            line = line.replace("\n","")
            row_list = line.split(":")
            if row_list[index] == entry :
                data.append(row_list)
    return [row_head] + data , width

table,width = get_rows("Sky","users","Sex","M")
