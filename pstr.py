NULL = ''


def split(string: str):
    """
    Takes one argument; splits a string into a list of characters

    :return: List of characters
    """
    return [char for char in string]


def replace(old: str, new: str, visual = False):
    """
    Takes three arguments; replaces the strings fed.
    Argument visual is optional, usage will affect preformance.

    :return: New string
    """

    # Split
    old = split(old)
    new = split(new)

    index = 0

    modelList = []

    if old == new:
        raise Exception('String args. fed are the same')

    # Length of old str is greater
    if len(old) > len(new):

        # Appends modelList by the difference of the two lengths of the lists
        for x in range(len(old) - len(new)):
            modelList.append(NULL)

        # Appends corresponding list
        for x in modelList:
            new.append(NULL)

    # Length of new str is greater
    elif len(old) < len(new):

        # Appends modelList by the difference of the two lengths of the lists
        for x in range(len(new) - len(old)):
            modelList.append(NULL)

        # Appends corresponding list
        for x in modelList:
            old.append(NULL)

    # Length is the same
    else:
        pass

    # Replace items in list left to right
    for char in old:

        # If char is the same then skip a space
        if old[index] == new[index]:
            index += 1

        else:
            old[index] = new[index]
            index += 1
            if visual:  # For demonstrating how replace function works
                print(old)

    # Map to string and return
    repStr = ''.join(map(str, old))

    return repStr


def wSplit(line: str):
    """
    Takes one argument; returns a list of words

    :return: List of words in given string
    """

    index = 0
    srch = split(line)
    condenser = []
    finList = []

    for char in srch:
        if srch[index] == ' ':

            # Map condenser to string
            strItem = ''.join(map(str, condenser))

            # Remove space
            rev = strItem.replace(' ', '')

            # Append final list and reset condenser
            finList.append(rev)
            condenser = []
            index += 1

        else:
            condenser.append(srch[index])
            index += 1

    # Condenses last word in line
    strItem = ''.join(map(str, condenser))

    # Remove space
    rev = strItem.replace(' ', '')

    # Append final list and reset condenser
    finList.append(rev)
    condenser = []
    index += 1

    return finList


def sReplace(line: str, query: str, rep: str):
    """
    Takes three arguments; returns revised string

    :return: Revised string
    """

    # Split line, and define vars
    index = 0
    scan = wSplit(line)
    inl = False

    # Stops an infinite loop problem
    if query == rep:
        raise Exception('Cannot replace item')

    # Replaces query with replacement
    for word in scan:
        if query == scan[index]:
            repQ = replace(scan[index], rep)
            scan[index] = repQ
            inl = True
        else:
            index += 1

    # If the item is not in the list
    if not inl:
        raise Exception('String is not in line')

    # Reset index
    index = 0

    # Adds a space to the string to return it to its original state
    for item in scan:

        # If it is the last item in the list, break loop
        if index == len(scan) - 1:
            break
        scan[index] += ' '
        index += 1

    # Condense list and return string
    final = ''.join(map(str, scan))
    return final
