import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ayyub",
  password="",
  database="smooth_database"
)

mycursor = mydb.cursor()

# mycursor.execute("""
# INSERT INTO tenants_reviews (care_for_the_property, respect_for_neighbors, communication, payments_punctuality, comment)
# VALUES (ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), ROUND(RAND()*5), "That tenant was a human with lots of fingers");
# """)

# mydb.commit()

mycursor.execute("SELECT * from tenants_reviews")
for x in mycursor:
  print(x)