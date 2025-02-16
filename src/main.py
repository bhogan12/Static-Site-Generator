from textnode import *
from htmlnode import *
from inline_markdown import *



def main():
    new_node = TextNode("This is a text node", TextType("bold"), "https://www.boot.dev")
    new_node2 = TextNode("This is a text node", TextType("bold"))
    new_node3 = TextNode("This is a text node", TextType("bold"), "https://www.boot.dev")

    print(new_node == new_node2)
    print(new_node == new_node3)
    print(new_node2)
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))

main()