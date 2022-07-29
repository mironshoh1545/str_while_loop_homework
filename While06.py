def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """ 
    con = ['a', 'e', 'i', 'o', 'u']  
    s = s.lower()
    i = 0
    su = 0
    while i < len(s):
        if not(s[i] in con) and s[i].isalpha():
            su += 1
        i += 1
    return su