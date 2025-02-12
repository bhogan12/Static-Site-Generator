import unittest

from textnode import TextNode, TextType


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

    def test_diff_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "http://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()