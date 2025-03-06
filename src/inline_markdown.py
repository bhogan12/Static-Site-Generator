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
    # First remove all image tags
    no_images = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    # Then extract links from remaining text
    return re.findall(r'\[(.*?)\]\((.*?)\)', no_images)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        if node.text != "":
            images = extract_markdown_images(node.text)

            if len(images) == 0:
                new_nodes.append(node)
            else:
                text_to_split = node.text
                for image in images:
                    sections = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    text_to_split = sections[1]
                if text_to_split != "":
                    new_nodes.append(TextNode(text_to_split, TextType.NORMAL))
    
    return new_nodes
                                
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        if node.text != "":
            links = extract_markdown_links(node.text)

            if len(links) == 0:
                new_nodes.append(node)
            else:
                text_to_split = node.text
                for link in links:
                    sections = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    text_to_split = sections[1]
                if text_to_split != "":
                    new_nodes.append(TextNode(text_to_split, TextType.NORMAL))
    
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes