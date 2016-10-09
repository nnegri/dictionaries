"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

from collections import Counter

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # Use list comprehension to create a list of words in the phrase
    # Use Counter to create a collection of words, and a number representing
    # how many times the word appears in the phrase. dict() then converts
    # the Counter to a dictionary.
    return dict(Counter([word for word in phrase.split()]))


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Create a dictionary of melons and corresponding prices
    melon_data = {
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25,
    }

    # If the melon_name is one of the keys in the dictionary, return its price
    if melon_name in melon_data.keys():
        return melon_data.get(melon_name)
    # If it is not, return "No price found"
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    # Create an empty dictionary
    word_lengths = {}

    for word in words:
        # If the word length is not yet in the dictionary, create the key
        # and a corresponding empty list value
        word_lengths[len(word)] = word_lengths.get(len(word), [])
        # If the word length is already a key in the dictionary, append the
        # word to the corresponding list value
        word_lengths[len(word)].append(word)
        # Sort each list value alphabetically
        word_lengths[len(word)] = sorted(word_lengths[len(word)])

    # Return list of length: word pairs, sorted by ascending length of words
    return sorted(word_lengths.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # Create dictionary of English-to-Pirate translations
    pirate_translations = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    # Created empty list for translated words
    translated = []
    # For each word in the phrase, append the corresponding pirate translation
    # If there is no translation, append the word itself
    for word in phrase.split():
        translated.append(pirate_translations.get(word, word))
    # Return the list as a string, separated by spaces
    return " ".join(translated)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # Create empty dictionary
    name_info = {}
    # For each name in the list of names, create a key of the first letter, 
    # and corresponding list value of the name.
    # If the key already exists, append the name to the corresponding list.  
    for name in names:
        first_letter = name[0]
        name_info[first_letter] = name_info.get(first_letter, [])
        name_info[first_letter].append(name)

    # Remove the first name from the list value of the first letter key
    first_letter = names[0][0]
    name_info[first_letter].remove((name_info.get(first_letter))[0])

    # Add the first name to the name_list, which will be returned at the end of 
    # the function. The first letter of the next name will be the last letter
    # of the name just added to the list.
    name_list = [names[0]]
    first_letter = names[0][-1]

    while True:
        # Use .get to get the list of names that start with the first_letter
        next_name_list = name_info.get(first_letter)
        
        if next_name_list:
            # If there are still names in the list, use the first one in the 
            # list as your next name.
            next_name = next_name_list[0]
            # Append the name to the name_list
            name_list.append(next_name)
            # Remove the name from the list in the dictionary value
            name_info[first_letter].remove((name_info.get(first_letter))[0])
            # The first letter of the next name will be the last letter
            # of the name just added to the list.
            first_letter = next_name[-1]
        # If there are no more names corresponding to the first_letter key,
        # break the loop.
        else:
            break

    return name_list

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
