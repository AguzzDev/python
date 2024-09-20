def list_filtered(l, text, condition):
    return list(filter(lambda l: l[text] == condition, l))
