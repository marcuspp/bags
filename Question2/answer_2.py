

def create_list_from_argument(argument):
    if not argument:
        return []

    try:
        return list(argument)
    except TypeError:
        return list(str(argument))
