PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, name, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, name)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, name)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, name)
    elif format == JSON:
        result = format_to_json(msg, name)
    return result


def format_to_json(msg, name):
    return ('{ "name":"' + name + '", "msg":"' +
            msg + '"}')


def plain_text(msg, name):
    return name + ' ' + msg


def plain_text_upper_case(msg, name):
    return plain_text(msg.upper(), name.upper())


def plain_text_lower_case(msg, name):
    return plain_text(msg.lower(), name.lower())
