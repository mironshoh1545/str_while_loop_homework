def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return a nswer
    """
     
    i = 0
    su = 0
    while i < len(s):
        if s[i].isupper():
            su += 1
        i += 1
    return su