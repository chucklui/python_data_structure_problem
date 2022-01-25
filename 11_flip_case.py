def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    phrase = list(phrase)
    for i in range(len(phrase)):
        letter = phrase[i]
        if letter.lower() == to_swap.lower() and letter.islower():
            phrase[i]= letter.upper()
        elif letter.lower() == to_swap.lower() and letter.isupper():
            phrase[i]= letter.lower()

    
    return "".join(phrase)

