from itertools import groupby

def statistics(iterable):
    """
    Given a list of dicts, this function prints statistics
    about dicts keys accurances
    """
    # Collecting all possible keys
    all_keys = set()
    for item in iterable:
        all_keys.update(item.keys())

    total_items = float(len(iterable))

    def group_for_key(key):
        keyfunc = lambda x: x.get(key)
        iterable.sort(key=keyfunc)

        grouped_by_percentage = []

        for k, g in groupby(iterable, keyfunc):
            size = len(list(g))
            grouped_by_percentage.append((size / total_items * 100, k))

        grouped_by_percentage.sort(reverse=True, key=lambda x: x[0])
        return grouped_by_percentage

    for key in all_keys:
        grouped = group_for_key(key)

        print '*** Occurance of key: %s ***' % key
        print

        if len(grouped) > 10:
            grouped = grouped[:10]

        for item in grouped:
            print '%% %5.2f - %s' % (item[0], item[1])

        print
        print
