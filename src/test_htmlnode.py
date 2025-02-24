import unittest

from textnode import *
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        html1 = HTMLNode()
        self.assertIsNone(html1.value)
    
    def test_propsToHtml(self):
        html1 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target" : "_blank"})
        self.assertEqual(html1.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_emptyProps(self):
        html1 = HTMLNode()
        self.assertEqual(html1.props_to_html(), "")

    def test_implementError(self):
        html1 = HTMLNode()
        self.assertRaises(NotImplementedError)

    def test_normalTexttoHTML(self):
        text1 = TextNode("hello", TextType.NORMAL)
        leaf1= LeafNode(None, "hello")
        self.assertEqual(
            text_node_to_html_node(text1).to_html(), leaf1.to_html())

    def test_boldTexttoHTML(self):
        text1 = TextNode("hello", TextType.BOLD)
        leaf1= LeafNode("b", "hello")
        self.assertEqual(
            text_node_to_html_node(text1).to_html(), leaf1.to_html())

    def test_italicTexttoHTML(self):
        text1 = TextNode("hello", TextType.ITALIC)
        leaf1= LeafNode("i", "hello")
        self.assertEqual(
            text_node_to_html_node(text1).to_html(), leaf1.to_html())
        
    def test_codeTexttoHTML(self):
        text1 = TextNode("hello", TextType.CODE)
        leaf1= LeafNode("code", "hello")
        self.assertEqual(
            text_node_to_html_node(text1).to_html(), leaf1.to_html())

    def test_linkTexttoHTML(self):
        text1 = TextNode("hello", TextType.LINK, "https://www.google.com")
        leaf1= LeafNode("a", "hello", {"href": "https://www.google.com"})
        self.assertEqual(
            text_node_to_html_node(text1).to_html(), leaf1.to_html())
        
    def test_imageTexttoHTML(self):
        text1 = TextNode("hello", TextType.IMAGE, "https://www.google.com")
        leaf1= LeafNode("img", "", {"src": "https://www.google.com", "alt": "hello"})
        self.assertEqual(
            text_node_to_html_node(text1).to_html(), leaf1.to_html())
        
        


class TestLeafNode(unittest.TestCase):
    def test_init(self):
        leaf = LeafNode("p", "poop")
        self.assertEqual(leaf.tag, "p")
        self.assertEqual(leaf.value, "poop")

    def test_toHtml(self):
        leaf1 = LeafNode("a", "pull my finger", {"href": "https://www.google.com"})
        self.assertEqual(leaf1.to_html(), "<a href=\"https://www.google.com\">pull my finger</a>")


class TestParentNode(unittest.TestCase):
    def test_toHtml(self):
        node1 = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(node1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


        node2= ParentNode("p",
            [
                LeafNode("a", "link", {"href": "https://www.google.com"}),
                node1
            ]
        )
        self.assertEqual(node2.to_html(), "<p><a href=\"https://www.google.com\">link</a><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")

        
if __name__ == "__main__":
    unittest.main()