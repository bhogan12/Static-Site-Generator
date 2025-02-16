from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node2):
        return (self.text == node2.text 
                and self.text_type == node2.text_type
                and self.url == node2.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("invalid text node type")


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