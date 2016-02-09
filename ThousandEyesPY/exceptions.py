class AuthenticationException(Exception):
    """Authentication Exception for ThousandEyes"""
    def __str__(self):
        return "ThousandEyes Reports Bad Authentication"


class BadRequestException(Exception):
    """ThousandEyes Reports Malformatted request"""
    def __str__(self):
        return "ThousandEyes Reports Malformatted request"

class ForbiddentException(Exception):
    """ThousandEyes Reports Insufficient permissions to execute request (ie, any POST method as a regular user), Check ownership and permissions"""
    def __str__(self):
        return "ThousandEyes Reports Insufficient permissions to execute request (ie, any POST method as a regular user), Check ownership and permissions"

class NotFoundException(Exception):
    """ThousandEyes Reports This endpoint is Attempting to access an endpoint that does not exis"""
    def __str__(self):
        return "ThousandEyes Reports This endpoint is Attempting to access an endpoint that does not exist"

class MethodNotAllowedException(Exception):
    """ThousandEyes Reports This request is not accepting the type of request initiated"""
    def __str__(self):
        return "ThousandEyes Reports This request is not accepting the type of request initiated"

class ContentTypeException(Exception):
    """Content type does not match the Accept header of the request"""
    def __str__(self):
        return "Content type does not match the Accept header of the request"

class UnsupportedMediaTypeException(Exception):
    """Attempting to POST data in incorrect format"""
    def __str__(self):
        return "Attempting to POST data in incorrect format"

class TooManyRequestsException(Exception):
    """You have exceeded the max number of requests per 1-minute period"""
    def __str__(self):
        return "You have exceeded the max number of requests per 1-minute period"

class InternalThousandEyesErrorException(Exception):
    """ThousandEyes is experiencing difficulties, please wait or contact support"""
    def __str__(self):
        return "ThousandEyes is experiencing difficulties, please wait or contact support"

class MaintenanceModeException(Exception):
    """ThousandEyes API is Undergoing maintenance, try again late"""
    def __str__(self):
        return "ThousandEyes API is Undergoing maintenance, try again later"
