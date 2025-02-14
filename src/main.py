from textnode import *
from htmlnode import *



def main():
    new_node = TextNode("This is a text node", TextType("bold"), "https://www.boot.dev")
    new_node2 = TextNode("This is a text node", TextType("bold"))
    new_node3 = TextNode("This is a text node", TextType("bold"), "https://www.boot.dev")

    print(new_node == new_node2)
    print(new_node == new_node3)
    print(new_node2)

main()