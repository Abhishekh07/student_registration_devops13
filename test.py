import os
from html.parser import HTMLParser

class HTMLTestParser(HTMLParser):

    def __init__(self):
        super().__init__()

    self.html_found = False
    self.title_found = False
    self.form_found = False
    self.submit_found = False
    self.email_found = False
    self.course_found = False
    self.required_fields = 0

def handle_starttag(self, tag, attrs):

    attributes = dict(attrs)

    if tag == "html":
        self.html_found = True

    elif tag == "title":
        self.title_found = True

    elif tag == "form":
        self.form_found = True

    elif tag == "button":
        if attributes.get("type") == "submit":
            self.submit_found = True

    elif tag == "input":
        input_type = attributes.get("type", "text")

        if input_type == "email":
            self.email_found = True

        if "required" in attributes:
            self.required_fields += 1

    elif tag == "select":
        if attributes.get("id") == "course":
            self.course_found = True


def test_file_exists():
    assert os.path.exists("index.html"), "index.html file does not exist"
print("PASS: index.html exists")

def test_html_structure():

    with open("index.html", "r", encoding="utf-8") as file:
        html = file.read()

parser = HTMLTestParser()
parser.feed(html)

assert parser.html_found, "<html> tag is missing"
print("PASS: HTML tag found")

assert parser.title_found, "<title> tag is missing"
print("PASS: Title found")

assert parser.form_found, "<form> tag is missing"
print("PASS: Registration form found")

assert parser.email_found, "Email input is missing"
print("PASS: Email field found")

assert parser.course_found, "Course selection is missing"
print("PASS: Course field found")

assert parser.required_fields >= 5, "Required fields are missing"
print("PASS: Required fields found")

assert parser.submit_found, "Submit button is missing"
print("PASS: Submit button found")


if name == "main":

    print("======================================")
print(" Student Registration HTML Test")
print("======================================")

test_file_exists()
test_html_structure()

print("======================================")
print(" ALL TESTS PASSED")
print("======================================")