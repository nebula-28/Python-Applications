import mysql.connector as connector

class DbConnect:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='mysql',database='wordwall',auth_plugin='mysql_native_password')
        
        #CREATE TABLE QUERY
        #query='CREATE TABLE vocab( id int NOT NULL AUTO_INCREMENT,user_word varchar(50),definition varchar(2000), synonym varchar(2000), antonym varchar(2000), phonetics varchar(100), sentences varchar(5000), insert_gmt_timestamp DATETIME NOT NULL DEFAULT NOW(), PRIMARY KEY (id) );'
        
        cur=self.con.cursor()
        #cur.execute(query)
        #print('Table is CREATED successfuly')

    def insert_word(self,user_word,definition,synonym,antonym ,phonetics,sentences):
        query="INSERT INTO vocab (user_word,definition,synonym,antonym ,phonetics,sentences) values('{}','{}','{}','{}','{}','{}')".format(user_word,definition,synonym,antonym ,phonetics,sentences)
        #print(query)

        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Your word is saved to VOCAB Table")
    
    #fetch details
    def fetch_all(self):
        query='SELECT * FROM vocab'
        #print(query)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Id is ",row[0])
            print("Word is ",row[1])
            print("definition is ",row[2])
            print("synonym is ",row[3])
            print("antonym is ",row[4])
            print("phonetics is ",row[5])
            print("sentences is ",row[6])
            print("insert_gmt_timestampes is ",row[7])