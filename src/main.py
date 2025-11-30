from textnode import *

def main():
    node = TextNode("this is some anchor text", TextType.LINK, "https://boot.dev")
    print(node)

if __name__ == "__main__":
    main()