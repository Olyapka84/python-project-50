def build_plain_output(diff, path=""):
    result = []

    for item in diff:
        key = item['key']
        type_ = item['type']
        full_path = f"{path}.{key}" if path else key

        match type_:
            case 'nested':
                children = build_plain_output(item['children'], full_path)
                result.append(children)
            case 'added':
                result.append(f"Property '{full_path}' was added with value: "
                              f"{stringify_plain_value(item['value'])}")
            case 'removed':
                result.append(f"Property '{full_path}' was removed")
            case 'changed':
                result.append(f"Property '{full_path}' was updated. "
                              f"From {stringify_plain_value(item['old_value'])} "
                              f"to {stringify_plain_value(item['new_value'])}")

    return '\n'.join(result)


def stringify_plain_value(value):
    match value:
        case dict():
            return "[complex value]"
        case None:
            return "null"
        case bool():
            return str(value).lower()
        case _:
            return f"'{value}'"
