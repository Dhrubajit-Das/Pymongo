import os
import platform
from pymongo import MongoClient

#connecting to mongodb in local system to store data
try: 
    conn = MongoClient() 
    print("Database Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

    
# connecting to database 
db = conn.database 
  
# Created collection names: students_data 
collection = db.students_data

#function to store data in db
def store_in_db(idd,name):
    db.collection.insert_one({"ID": idd, "Name": name } )
    
#function to search data using "ID"
def search_all_in_db(idd):
    find_student = db.collection.find_one({"ID": idd})
    return find_student
        
#function to count total data in db
def count_all_in_db():
    total_entries = db.collection. estimated_document_count()
    return total_entries

#function to remove data from db using "ID"
def remove_from_db(idd):
    db.collection.remove({ "ID" : idd })
    

#function to restart program
def restart_program():
    restart = input("Would you like to restart this program <y/n>?  ")
    if restart == "yes" or restart == "y":
        main()
        restart_program()
    elif restart == "n" or restart == "no":
        print ("Program terminating. Goodbye.")
        quit()
    

#main function to manage evrything
def main():
    #Printing options For This Program
    print(""" 

                                        Enter 1 : To View Student's List 
                                        Enter 2 : To Add New Student 
                                        Enter 3 : To Search Student 
                                        Enter 4 : To Remove Student 
                                        Enter 5 : QUIT
        
        """)

    try: #Using Exceptions For Validation
        userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User1
        
    except ValueError:
        exit("\nHy! That's Not A Number") #Error Message
    else:
        print("\n") #Print New Line

        
    #Checking Using Option  
    if(userInput == 1): #This Option Will Print List Of Students  
        total_students = count_all_in_db()
        
        if total_students > 0:
            print("Number of Students in the database: {}".format(total_students))
                                
        else:
            print("No Students in the Database.")
               
        
                                
    elif(userInput == 2): #This Option Will Add New Student In The db
        newid = int(input("Enter Student ID: "))
        
        find_item = db.collection.find( { "ID": newid } ).count()
        
        if find_item > 0: 
            print("\nThis Student ID Already In The Database")
              
        else:   
            newStd = input("Enter New Student: ")
            store_in_db(newid, newStd)
            print("\n=> New Student ID {} Successfully Add \n".format(newid))
             
        
        
                
    #This Option Will Search Student From The database....           
    elif(userInput == 3): 
        srcStd = int(input("Enter Student ID To Search: "))
        
        find_item = search_all_in_db(srcStd)
        
        if find_item: 
            print("\n=> Record Found Of Student {}".format(find_item))

        else:
            print("\n=> No Record Found Of Student")
        
        

    #this option will detele data from db.....
    elif(userInput == 4): 
        rmStd = int(input("Enter Student ID To Remove: "))
        
        find_item = db.collection.find( { "ID": rmStd } ).count()
        print(find_item)
        
        if find_item == 1:
            print("\n=> Student ID {} Successfully Deleted \n".format(rmStd))
            remove_from_db(rmStd)
            
        else:
            print("\n=> No Record Found of This Student")
            
        restart_program()
        
    elif(userInput == 5):
        print ("Program terminating. Goodbye.")
        quit()
    
    #this will look for other keys entry....
    elif(userInput < 1 or userInput > 5): 
        print("Please Enter Valid Option between 1 & 4...")  
        main()
        
    
                        

main()            
restart_program()