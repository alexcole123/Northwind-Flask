from enum import Enum

class StatusCode(Enum):
    OK = 200
    BadRequest = 400
    Unauthorized = 401
    NotFound  = 404
    InternalServerError = 500
