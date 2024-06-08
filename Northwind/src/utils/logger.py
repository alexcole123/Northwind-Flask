from datetime import datetime
from flask import session

class Logger:
    # path to log file
    __log_file = "./logger.log"

    # save log message
    @staticmethod
    def log(message):
        #take current time
        now = datetime.now()
        #open file
        with open(Logger.__log_file, "a") as file: # "a" = Append
            #write time
            file.write(str(now) + "\n")
            #write message
            file.write(str(message) + "\n")
            #write user data if exist
            user = session.get("current_user")
            if user: file.write("User ID: " + str(user["id"]) + ", User Email: " + user["email"] + "\n")
            #if we have a user - document user details (id and email)
        
            file.write("---------------------------------\n")
    
