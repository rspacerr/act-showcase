def calculate(a: int, b: int) -> int:
    """
    returns integer sum of a + b
    """
    return a + b


def calculate2(a, b, debug=False):
    """
    returns difference
    """
    if debug:
        print(f"Received a = {a}")
        print(f"Received b = {b}")
    return a - b
