def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    su = 0
    while i < len(s):
        if s[i].isdigit():
            su += 1
        i += 1
    return su