"""
>>> say('Hello')
Hello Hello
>>> say('Hi', 5)
Hi Hi Hi Hi Hi
>>> say('cat', 3, '(=^.^=)')
cat(=^.^=)cat(=^.^=)cat
"""
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
