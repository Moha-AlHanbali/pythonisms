"""This module is an examples demonstrating pythonic iterator features"""


# Solving the code challenge in a different way using __iter__ and __next__
# ---------------------------------------------------------------------------------

def url_sanitizer(url):
    """
    url_sanitizer is a function that replaces spaces in a url with %20.

    Arguments:
        url: str
    
    Return: modified str
    """
    string = iter(url)
    counter = 0
    output = ""
    while counter < len(url):
        char = next(string)
        if not char == " ":
            output += char

        else:
            output += "%20"

        counter += 1

    return output
      