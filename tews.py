eventid = input("What is the event id?")
country = input("What is the Country?")

file = open('eng.txt', 'w')
file.write("event = {\n")
file.write("	id = " + eventid + "\n")
file.write("	country = " + country + "\n")

file.close() 
