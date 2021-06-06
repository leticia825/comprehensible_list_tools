""" This module is an exercise of list comprehensions.
[expression for control_var in iterable_item if condition]
                                       (if is optional filtering)
"""


def all_even(lst):
    """ Return a list of even numbers occurring in the list lst,
    in the same order as they appear in lst

    Args:
        lst: list of numbers

    Returns:
        list of even numbers in order
    """

    return [num for num in lst if num % 2 == 0]


def all_not_multiple(lst, n):
    """ Return a list of the numbers in lst that are not multiples
    of n, in the same order as they appear in lst

    Args:
        lst: list of numbers
        n: value that numbers should not be a multiple of

    Returns:
        numbers that are not multiple of n
    """

    return [num for num in lst if num % n != 0]


def max_from_2_tuples(tuples):
    """ Return a 2-tuple that contains the max of the first element
    of each tuple and the max of the second element of each tuple.
    For example, max_from_2_tuples([(-1, 5), (13, 2)]) would return
    (13, 5).

    Args:
        tuples: list of 2-tuples

    Returns:
        2-tuple of (max element i, max element j)
    """
    # if tuples:
    #   first = max([tup[0] for tup in tuples])
    #   second = max([tup[1] for tup in tuples])
    #   lst = first, second
    #   return lst

    if tuples:
        return max([tup[0] for tup in tuples]), max([tup[1] for tup in tuples])


def lower_case_words(sentence):
    """ Return a list of words in sentence converted to lower case.
    Empty strings are not included in result. Words are separated
    by one or more space characters.

    Args:
        sentence: string given

    Returns:
        lower case version of sentence
    """

    sentence_list = sentence.split()
    return [s.lower() for s in sentence_list]


def baby_names(names, last_name):
    """ Return a list of "full names" containing
    all possible pairs of distinct names in names,
    with last_name appended (and a space between
    each part of the name).  For example
    baby_names(["Fred", "James"], "Smith") would
    return ["Fred James Smith", "James Fred Smith"]

    Args:
        names: non-empty list of distinct strings
        last_name: string given

    Returns:
        possible_names: list of all name combinations
    """

    return [i + " " + j + " " + last_name for i in names for j in names if i != j]





