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
    text = "Here is a ![image [with brackets]](url) and [a link [with brackets]](url)"
    print(extract_markdown_links(text))
    print(extract_markdown_images(text))


    text1 = "Here is a ![image [with brackets]](url) and [a link [with brackets]](url)"


    print(extract_markdown_links(text1))

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(split_nodes_image([TextNode(text, TextType.NORMAL)]))
    text = "This is text with no images in it."
    print(split_nodes_image([TextNode(text, TextType.NORMAL)]))
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(split_nodes_link([TextNode(text, TextType.NORMAL)]))
    text = "This is text with no links in it."
    print(split_nodes_link([TextNode(text, TextType.NORMAL)]))
    text = "Here is a ![image [with brackets]](url) and [a link [with brackets]](url)"
    print(split_nodes_image([TextNode(text, TextType.NORMAL)]))
    print(split_nodes_link([TextNode(text, TextType.NORMAL)]))
main()