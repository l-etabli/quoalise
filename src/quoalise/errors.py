class Error(Exception):
    """Base class for quoalise errors"""

    pass


class NotAuthorized(Error):
    pass


class ServiceUnavailable(Error):
    pass
