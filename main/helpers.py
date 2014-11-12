def remove_non_ascii(paragraph):
    return "".join(i for i in paragraph if ord(i)<128)
