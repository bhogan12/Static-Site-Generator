import re

from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter, 2)
            if len(split_node) == 1:
                new_nodes.append(node)
            elif len(split_node) == 3:
                new_nodes.append(TextNode(split_node[0], TextType.NORMAL))
                new_nodes.append(TextNode(split_node[1], text_type))
                new_nodes.extend(split_nodes_delimiter([TextNode(split_node[2], TextType.NORMAL)], delimiter, text_type))
            else:
                raise Exception("cannot split text: closing delimiter not found")
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)