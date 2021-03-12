import  datetime
current_date = datetime.datetime.now()
s_date = current_date.strftime("%d-%m-%Y %H:%M:%S")
f = open("my1.log","a")
f.write(s_date+": my data\n")
f.close()
