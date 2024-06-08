from utils.dal import DAL

class AuthLogic:

    # Ctor:
    def __init__(self):
        self.dal = DAL()

    # Is email taken:
    def is_email_taken(self, email):
        sql = "SELECT EXISTS(SELECT * FROM users WHERE email = %s) AS is_taken"
        result = self.dal.get_scalar(sql, (email, ))
        return result["is_taken"] == 1

    # Add a new user:
    def add_user(self, user):
        # sql = "INSERT INTO users VALUES(DEFAULT, %s, %s, %s, %s, %s)"
        sql = "INSERT INTO users(first_name, last_name, email, password, role_id) VALUES(%s, %s, %s, %s, %s)"
        self.dal.insert(sql, (user.first_name, user.last_name, user.email, user.password, user.role_id))

    def get_user(self, email, password):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        user = self.dal.get_scalar(sql, (email, password))
        return user

    # Close connection:
    def close(self):
        self.dal.close()
