from werkzeug.http import HTTP_STATUS_CODES


def is_informational(code):
  return code >= 100 and code <= 199


def is_success(code):
  return code >= 200 and code <= 299


def is_redirect(code):
  return code >= 300 and code <= 399


def is_client_error(code):
  return code >= 400 and code <= 499


def is_server_error(code):
  return code >= 500 and code <= 599

def get_status(code):
  if is_success(code):
    return 'success'
  elif is_client_error(code):
    return 'client_error'
  elif is_server_error(code):
    return 'server_error'
  elif is_redirect(code):
    return 'redirect'
  elif is_informational(code):
    return 'informational'

def get_message(code):
  ''' Maps an HTTP status code to the textual status
  '''
  return HTTP_STATUS_CODES.get(code, '')


CONTINUE = 100
SWITCHING_PROTOCOLS = 101
OK = 200
CREATED = 201
ACCEPTED = 202
NON_AUTHORITATIVE_INFORMATION = 203
NO_CONTENT = 204
RESET_CONTENT = 205
PARTIAL_CONTENT = 206
MULTI_STATUS = 207
MULTIPLE_CHOICES = 300
MOVED_PERMANENTLY = 301
FOUND = 302
SEE_OTHER = 303
NOT_MODIFIED = 304
USE_PROXY = 305
RESERVED = 306
TEMPORARY_REDIRECT = 307
PERMANENT_REDIRECT = 308
BAD_REQUEST = 400
UNAUTHORIZED = 401
PAYMENT_REQUIRED = 402
FORBIDDEN = 403
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
NOT_ACCEPTABLE = 406
PROXY_AUTHENTICATION_REQUIRED = 407
REQUEST_TIMEOUT = 408
CONFLICT = 409
GONE = 410
LENGTH_REQUIRED = 411
PRECONDITION_FAILED = 412
REQUEST_ENTITY_TOO_LARGE = 413
REQUEST_URI_TOO_LONG = 414
UNSUPPORTED_MEDIA_TYPE = 415
REQUESTED_RANGE_NOT_SATISFIABLE = 416
EXPECTATION_FAILED = 417
UNPROCESSABLE_ENTITY = 422
PRECONDITION_REQUIRED = 428
TOO_MANY_REQUESTS = 429
REQUEST_HEADER_FIELDS_TOO_LARGE = 431
CONNECTION_CLOSED_WITHOUT_RESPONSE = 444
INTERNAL_SERVER_ERROR = 500
NOT_IMPLEMENTED = 501
BAD_GATEWAY = 502
SERVICE_UNAVAILABLE = 503
GATEWAY_TIMEOUT = 504
HTTP_VERSION_NOT_SUPPORTED = 505
LOOP_DETECTED = 508
NOT_EXTENDED = 510
NETWORK_AUTHENTICATION_REQUIRED = 511
