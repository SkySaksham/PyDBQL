def table_header (raw_string) :
    header = ""
    column_width = ""

    is_column_width = False

    for i in raw_string.split(":") :
        if is_column_width:
            column_width+= i+":"
            is_column_width=False
        else :
            header += i+":"
            is_column_width = True

    return header[0:len(header)-1],column_width[0:len(column_width)-1]

def create_table(database_name,name,header,column_width) :
    with open(f"{database_name}/tables.txt",'a') as tables :
        data = [name+"\n",header+"\n",column_width+"\n"]
        tables.writelines(data)
    with open(f"{database_name}/tables/{name}.txt","w") as file :
        return

def add_entries(database_name,file_name,row) :
    with open(f"{database_name}/tables/{file_name}.txt","a") as file :
        file.writelines([row+"\n"])




