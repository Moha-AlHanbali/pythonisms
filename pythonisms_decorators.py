"""This module is an examples demonstrating pythonic decorators features"""


# Solving the code challenge in a different way using decorators and wrappers
# ---------------------------------------------------------------------------------

from functools import wraps

def url_sanitizer_wrap(func):

  @wraps(func)

  def wrapper(*args, **kwargs):
    """
    url_sanitizer_wrap wraps functions to replce spaces with %20.
    """
    output =  func(*args, **kwargs)

    for char in range(len(output)):
        if output[char] == " ":
            output = output[:char] + "%20" + output[char+1:] 

    return output

  return wrapper


@url_sanitizer_wrap
def sanitize(url):
  """ 
  sanitize sanitizes given urls

  Arugments:
    url: str

  Return: modified str
  """

  return url