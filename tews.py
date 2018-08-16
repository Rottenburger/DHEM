textname = input("What is the Name?")
eventid = input("What is the event id?")
country = input("What is the Country?")

file = open(textname + '.txt', 'w')
file.write("event = {\n")
file.write("	id = " + eventid + "\n")
file.write("	country = " + country + "\n")

file.close() 
