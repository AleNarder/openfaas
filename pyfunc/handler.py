from . import helper


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    return helper.fib(5)
