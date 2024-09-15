import pytest
from butterxml.__main__ import Parser, DOMNode

@pytest.fixture
def parser():
    return Parser()

def test_define_variable(parser):
    parser.define_variable('test_var', 'test_value')
    assert parser.variables['test_var'] == 'test_value'

def test_expand_variables(parser):
    parser.define_variable('name', 'Alice')
    result = parser.expand_variables('Hello, ${name}!')
    assert result == 'Hello, Alice!'

def test_define_macro(parser):
    parser.define_macro('greet', 1, 'Hello, #1!')
    assert 'greet' in parser.macros
    assert parser.macros['greet'] == (1, 'Hello, #1!')

def test_expand_macro(parser):
    parser.define_macro('greet', 1, 'Hello, #1!')
    result = parser.expand_macro('greet', ['World'])
    assert result == 'Hello, World!'

def test_parse_braces(parser):
    content, remaining = parser.parse_braces('{test content} remaining text')
    assert content == 'test content'
    assert remaining == 'remaining text'

def test_parse_command(parser):
    command, args, remaining = parser.parse_command(r'\section{Test Section} remaining text')
    assert command == 'section'
    assert args == ['Test Section']
    assert remaining == 'remaining text'

def test_parse_content(parser):
    input_text = r'\section{Test Section}\subsection{Test Subsection}Some text.'
    root = parser.parse_content(input_text)
    assert isinstance(root, DOMNode)
    assert root.tag == 'root'
    assert len(root.children) == 1
    assert root.children[0].tag == 'section'
    assert root.children[0].text == 'Test Section'
    assert len(root.children[0].children) == 2
    assert root.children[0].children[0].tag == 'subsection'
    assert root.children[0].children[0].text == 'Test Subsection'
    assert root.children[0].children[1].tag == 'p'
    assert root.children[0].children[1].text == 'Some text.'

def test_to_xml_string(parser):
    input_text = r'\section{Test Section}\subsection{Test Subsection}Some text.'
    root = parser.parse_content(input_text)
    xml_string = parser.to_xml_string(root)
    expected_xml = '<root><section>Test Section<subsection>Test Subsection</subsection><p>Some text.</p></section></root>'
    assert xml_string == expected_xml

def test_handle_include(parser, tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_include.txt"
    test_file.write_text("Included content")
    
    result = parser.handle_include(str(test_file))
    assert result == "Included content"

def test_handle_include_file_not_found(parser):
    result = parser.handle_include("non_existent_file.txt")
    assert result == "File non_existent_file.txt not found."

def test_expand_dom(parser):
    parser.define_variable('name', 'Alice')
    root = DOMNode('root')
    child = DOMNode('p', 'Hello, ${name}!')
    root.add_child(child)
    
    parser.expand_dom(root)
    assert root.children[0].text == 'Hello, Alice!'
