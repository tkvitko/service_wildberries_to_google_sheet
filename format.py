def format_to_google(data):
    """Transform this dicts from API to list of lists"""

    values_to_add = []

    for item in data:
        item_values = list(item.values())
        values_to_add.append(item_values)

    return values_to_add
