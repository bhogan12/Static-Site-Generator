import unittest

from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = ("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item")
        blocks = markdown_to_blocks(text)
        expected = ["# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertListEqual(blocks, expected)

    def test_to_blocks_whitespace(self):
        text = "# This is a heading\n\n This line has whitespace at the start\n\nThis one at the end "
        blocks = markdown_to_blocks(text)
        expected = ["# This is a heading",
                    "This line has whitespace at the start",
                    "This one at the end"
        ]
        self.assertListEqual(blocks, expected)

    def test_to_blocks_extra_lines(self):
        text = "# This is a heading\n\n\n\n\nThis is a paragraph\n\n\nAnd another"
        blocks = markdown_to_blocks(text)
        expected = ["# This is a heading",
                    "This is a paragraph",
                    "And another"
        ]
        self.assertListEqual(blocks, expected)

    def test_block_to_block_type(self):
        paragraph = "hello\nhow are you?"
        heading = "#### heading text"
        code = "```code.execute()```"
        quote = ">this is a quote\n>this is also a quote"
        unordered = "* list item one\n- list item two"
        ordered = "1. list item one\n2. list item two\n3. list item three"

        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(heading), BlockType.HEADING)
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(unordered), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(ordered), BlockType.ORDERED_LIST)
    
    #def test_markdown_to_html(self):
        #md = "# Header\n\nParagraph\n\n- List item\n- List item\n\n[link](somewhere)\n\n![image](something)\n\n**bold**\n\n*italics*"
        