from textnode import TextNode, TextType


def is_odd(num):
    return num % 2 == 1


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        parts = node.text.split(delimiter)
        if not is_odd(len(parts)):
            raise ValueError("Invalid markdown syntax.")

        for i in range(len(parts)):
            result.append(TextNode(parts[i], text_type if is_odd(i) else TextType.TEXT))

    return result
