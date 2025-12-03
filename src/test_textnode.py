import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("hi there", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("different text", TextType.LINK, "https://thecoolestdev.dev")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
