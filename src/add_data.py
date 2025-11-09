

def table_info (raw_string) :   # "Sno:[(key)]int[(<len>)]:name:()str[<len>]:money:[(key)]float[(<len>)]"
    columns = raw_string.split(":")

    data_types = ["int","str","float"] 
    names , types , sizes , key = [],[],[],[]

    for i in range (0,len(columns),2) :
        names += [columns[i]]
        
    for i in range(1,len(columns),2) :
        chunk = columns[i]
        data = [False,"",""]
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


a="sno:int(4):Name:str(12):balance:float(1)"

try : print(table_info(a))
except Exception as e : print(e)



