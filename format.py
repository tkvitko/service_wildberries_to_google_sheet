def format_to_google(data):
    # Преобразование списка словарей, полученного из API, в список списков
    values_to_add = []

    for item in data:
        item_values = list(item.values())
        values_to_add.append(item_values)

    return values_to_add
