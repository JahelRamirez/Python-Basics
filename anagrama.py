def is_anagrama(FirstWord, SecondWord):
    """
    This function allows the user to know if tow words are anagrams

    Args:
        FirstWord (String): First word
        SecondWord (String): Second word

    Returns:
        Boolean: It returns True or False
    """
    if FirstWord == SecondWord[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    is_anagrama('amor', 'roma')
