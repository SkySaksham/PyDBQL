import add_data as ad
import drop_and_create_db as db
import create_table as ct



#db.create_db("hello2")
table = "user"
a="sno :(key)int(4) :Name:()str(12) :balance :float"
entry = ["3:Saksham:90","4:user2:1221"]


#data=ad.table_info(a)
#db.create_db("hello")
#ct.create_table("hello",table,data)
try : ad.add_entries("hello",table,entry)
except Exception as e : print (e)


