import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_no_url(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        self.assertIsNone(node.url)

    def test_diff_types(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_split_nodes_delim(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, 
                         [
                          TextNode("This is text with a ", TextType.NORMAL),
                          TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.NORMAL)
                         ])

    def test_two_nodes_delim(self):
        node = TextNode("This is text with a `code block` word and then `another` one", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, 
                         [
                          TextNode("This is text with a ", TextType.NORMAL),
                          TextNode("code block", TextType.CODE),
                          TextNode(" word and then ", TextType.NORMAL),
                          TextNode("another", TextType.CODE),
                          TextNode(" one", TextType.NORMAL)
                         ])
        
    def test_split_nodes_diff_delim(self):
        node = TextNode("This is **bold text** with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, 
                         [
                          TextNode("This is ", TextType.NORMAL),
                          TextNode("bold text", TextType.BOLD),
                          TextNode(" with a ", TextType.NORMAL),
                          TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.NORMAL)
                         ])

if __name__ == "__main__":
    unittest.main()