from validate_email_address import validate_email #pip install validate_email_address
from models.role_model import RoleModel

class UserModel:

    def __init__(self, id, first_name, last_name, email, password, role_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id

    def validate_insert(self):
        if not self.first_name: return "Missing first name"
        if not self.last_name: return "Missing last name"
        if not self.password: return "Missing password"
        if not self.role_id: return "Missing role id"
        if len(self.first_name) < 2 or len(self.first_name) > 20: return "First name length must be 2 to 20 chars"
        if len(self.last_name) < 2 or len(self.last_name) > 30: return "Last name length must be 2 to 30 chars"
        if len(self.email) < 5 or len(self.email) > 100: return "Email length must be 5 to 100 chars"
        if len(self.password) < 4 or len(self.password) > 100: return "Password length must be 4 to 100 chars"
        if not validate_email(self.email): return "Email not valid"
        if self.role_id != RoleModel.Admin.value and self.role_id != RoleModel.User.value: return "Role must be User or Admin"
        return None
