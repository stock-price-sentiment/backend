# import all the tables into this file 




try:
  db.create_all()
  print("Connected to database!")
except:
  print("Unable to connect to database!")