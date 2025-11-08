def draw_table (table,size) :

    def table_edge (size) :
        border = ""
        for i in size : border += f"+-{'-'*i}-+" 
        print (border)

    def row_string(row,size,i) :
        if (len(str(row[i])) <= size[i]) :
            return  str(row[i])+" "*(size[i]-len(str(row[i])))
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

