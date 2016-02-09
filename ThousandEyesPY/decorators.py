from exceptions import *
# AuthenticationException, BadRequestException
import requests

def handleError(function):
    def handleProblems(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                raise BadRequestException()
            elif e.response.status_code == 401:
                raise AuthenticationException()
            elif e.response.status_code == 403:
                raise ForbiddentException()
            elif e.response.status_code == 404:
                raise NotFoundException()
            elif e.response.status_code == 405:
                raise MethodNotAllowedException()
            elif e.response.status_code == 406:
                raise ContentTypeException()
            elif e.response.status_code == 415:
                raise UnsupportedMediaTypeException()
            elif e.response.status_code == 429:
                raise TooManyRequestsException()
                raise UnsupportedMediaTypeException()
            elif e.response.status_code == 500:
                raise InternalThousandEyesErrorException()
            elif e.response.status_code == 503:
                raise MaintenanceModeException()
    return handleProblems
