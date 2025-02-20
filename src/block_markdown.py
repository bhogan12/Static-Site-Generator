from enum import Enum
from inline_markdown import *
from textnode import *
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if text[:3] == "```" and text[-3:] == "```":
        return BlockType.CODE
    
    lines = text.split("\n")
    
    is_quote = True
    for line in lines:
        if line[0] != ">":
            is_quote = False
    if is_quote:
        return BlockType.QUOTE
    
    is_unordered = True
    for line in lines:
        if line[0:2] != "* " and line[0:2] != "- ":
            is_unordered = False
    if is_unordered:
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    for i in range(len(lines)):
        if lines[i][0] != f"{i+1}" or lines[i][1:3] != ". ":
            is_ordered = False
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
        

def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    while "\n" in block_list:
        block_list.remove("\n")
    while "" in block_list:
        block_list.remove("")
    for i in range(len(block_list)):
        block_list[i] = block_list[i].strip()
    
    return block_list

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(text_node_to_html_node(node))
    return htmlnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if not line.startswith("> "):
                    raise Exception("invalid quote")
                new_lines.append(line.lstrip("> "))
            children = text_to_children("\n".join(new_lines))
            node_list.append(ParentNode("blockquote", children))
        
        elif block_type == BlockType.UNORDERED_LIST:
            list_children = tag_ulist_children(block)
            node_list.append(ParentNode("ul", list_children))

        elif block_type == BlockType.ORDERED_LIST:
            list_children = tag_olist_children(block)
            node_list.append(ParentNode("ol", list_children))

        elif block_type == BlockType.CODE:
            if not block.startswith("```") or not block.endswith("```"):
                raise Exception("invalid code")
            code_text, language_id = get_code_content(block)
            code_props = None
            if language_id != "":
                code_props = f"class=\"language-{language_id}\""
            children = text_to_children(code_text)
            inner_tag = ParentNode("code", children, code_props)
            node_list.append(ParentNode("pre", inner_tag))

        elif block_type == BlockType.HEADING:
            hash_count = get_heading_count(block)
            children = text_to_children(block[hash_count+1:])
            node_list.append(ParentNode(f"h{hash_count}", children))

        elif block_type == BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            children = text_to_children(text)
            node_list.append(ParentNode("p", children))

    return ParentNode("div", node_list)
            

def tag_ulist_children(list_text):
    lines = list_text.split("\n")
    tagged_list = []
    for line in lines:
        children = text_to_children(line[2:])
        tagged_list.append(ParentNode("li", children))
    return tagged_list

def tag_olist_children(list_text):
    lines = list_text.split("\n")
    tagged_list = []
    for line in lines:
        children = text_to_children(line[3:])
        tagged_list.append(ParentNode("li", children))
    return tagged_list

def get_code_content(code_text):
    lines = code_text.split("\n")
    language_id = ""
    if len(lines[0]) > 3:
        language_id = lines[0][3:]
    code_content = "\n".join(lines[1:-1])
    return code_content, language_id

def get_heading_count(heading_text):
    hash_count = 0
    while heading_text.startswith("#"):
        hash_count += 1
        heading_text = heading_text[1:]
    return hash_count