class BaseException(Exception):
    # Override this in your sub-class!
    status_code = None

    def __init__(self, message, status_code=None, payload=None,
                 json_encode=False):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        self.json_encode = json_encode

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class NotFoundError(BaseException):
    status_code = 404
