class Error(Exception):
    """Base class for quoalise errors"""

    pass


class ConnectionFailed(Error):
    """Quoalise client is not able to connect to XMPP server"""

    pass


class NotAuthorized(Error):
    """Ressource access is not authorized"""

    pass


class BadRequest(Error):
    """Request cannot be processed / value error"""

    pass


class ServiceUnavailable(Error):
    """Quoalise service is not connected / is not reachable"""

    pass
