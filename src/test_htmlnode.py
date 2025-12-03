import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "Hi this is a paragraph")
        props_html = node.props_to_html()
        expected_html = ""
        self.assertEqual(props_html, expected_html)
        node = HTMLNode(tag="<a>", props={"href": "https://google.com"})
        props_html = node.props_to_html()
        expected_html = ' href="https://google.com"'
        self.assertEqual(props_html, expected_html)

    def test_not_eq(self):
        node = HTMLNode(tag="<a>", props={"href": "https://google.com"})
        props_html = node.props_to_html()
        expected_html = ' garbage="https://google.com"'
        self.assertNotEqual(props_html, expected_html)


if __name__ == "__main__":
    unittest.main()
