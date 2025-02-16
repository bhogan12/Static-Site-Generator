import unittest

from textnode import *
from inline_markdown import *

class TestInlineMarkdown(unittest.TestCase):
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
        
    def test_extract_markdown_images(self):
        result = extract_markdown_images(
            "This is text with ![an image](https://i.imgur.come/zrrmMNO.png) inside it"
        )
        self.assertListEqual([("an image", "https://i.imgur.come/zrrmMNO.png")], result)
    
    def test_extract_markdown_links(self):
        result = extract_markdown_links(
            "This is text with [a link](https://www.google.com) inside it"
        )
        self.assertListEqual([("a link", "https://www.google.com")], result)

if __name__ == "__main__":
    unittest.main()