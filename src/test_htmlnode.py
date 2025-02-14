import unittest

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




if __name__ == "__main__":
    unittest.main()