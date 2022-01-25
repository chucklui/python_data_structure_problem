def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lower_string = phrase.lower()
    lower_string = lower_string.replace(' ','')
    lower_string = list(lower_string)
    lower_string.reverse()
    lower_string = ''.join(lower_string)
    if lower_string == phrase.lower().replace(' ',''):
        return True
    else:
        return False