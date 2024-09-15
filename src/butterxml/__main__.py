import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Union


class DOMNode:
    """A node in the document DOM tree."""
    def __init__(self, tag: str, text: str = '', children: Optional[List['DOMNode']] = None):
        self.tag = tag
        self.text = text
        self.children = children or []

    def add_child(self, child: 'DOMNode'):
        self.children.append(child)

    def __repr__(self):
        return f"DOMNode(tag='{self.tag}', text='{self.text}', children={len(self.children)})"


class Parser:
    def __init__(self):
        """Initialize the parser with macro, variable storage, and escaping."""
        self.macros: Dict[str, Union[str, Tuple[int, str]]] = {}
        self.variables: Dict[str, str] = {}
        self.escaped_chars = {'\\': '\\', '{': '{', '}': '}', '#': '#', '$': '$'}

    def define_macro(self, name: str, params: Optional[int], expansion: str):
        """Define a macro with optional parameters."""
        self.macros[name] = (params, expansion) if params is not None else expansion

    def define_variable(self, name: str, value: str):
        """Define a variable."""
        self.variables[name] = value

    def expand_variables(self, text: str) -> str:
        """Expand any variables or macros in the given text."""
        # Expand variables in the format ${var}
        text = re.sub(r'\$\{([a-zA-Z0-9_]+)\}', lambda match: self.variables.get(match.group(1), match.group(0)), text)

        # Expand macros in the format ${macro}[arg1, arg2]
        def macro_expansion(match):
            macro_name = match.group(1)
            args = match.group(2).split(',') if match.group(2) else []
            return self.expand_macro(macro_name, [arg.strip() for arg in args])

        text = re.sub(r'\$\{([a-zA-Z0-9_]+)\}\[(.*?)\]', macro_expansion, text)
        return text

    def expand_macro(self, macro_name: str, args: Optional[List[str]] = None) -> str:
        """Expand a macro with optional arguments."""
        if macro_name not in self.macros:
            return f"\\{macro_name}"  # Return the raw macro call if not defined

        macro = self.macros[macro_name]

        if isinstance(macro, tuple):
            # Macro with parameters
            param_count, expansion = macro
            if args and len(args) == param_count:
                for i, arg in enumerate(args, 1):
                    expansion = expansion.replace(f"#{i}", arg)
                return self.expand_variables(expansion)  # Expand variables within the macro
            else:
                return f"\\{macro_name}"  # Return raw if argument count mismatch
        else:
            # Macro without parameters
            return self.expand_variables(macro)

    def parse_braces(self, text: str) -> Tuple[str, str]:
        """Parse the content between balanced braces."""
        brace_depth = 0
        parsed_content = []
        i = 0

        while i < len(text):
            char = text[i]
            if char == '{':
                brace_depth += 1
                if brace_depth > 1:
                    parsed_content.append(char)
            elif char == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    # Return content inside braces and remaining text
                    return ''.join(parsed_content), text[i+1:].strip()
                parsed_content.append(char)
            else:
                if char == '\\' and i + 1 < len(text) and text[i + 1] in self.escaped_chars:
                    # Handle escaping special characters
                    parsed_content.append(self.escaped_chars[text[i + 1]])
                    i += 1  # Skip the escaped character
                else:
                    parsed_content.append(char)
            i += 1

        return ''.join(parsed_content), ''

    def parse_command(self, text: str) -> Tuple[str, List[str], str]:
        """Parse a LaTeX-style command with arguments from the input."""
        command_match = re.match(r"\\([a-zA-Z]+)", text)
        if command_match:
            command = command_match.group(1)
            remaining_text = text[command_match.end():].strip()

            args = []
            while remaining_text.startswith('{'):
                arg, remaining_text = self.parse_braces(remaining_text)
                args.append(arg)

            return command, args, remaining_text

        return '', [], text

    def parse_content(self, text: str) -> DOMNode:
        """Parse the input content based on braces and commands, and return the root of the DOM tree."""
        root = DOMNode('root')  # Root element of the DOM tree
        current_node = root

        while text:
            if text.startswith('\\'):
                # Handle commands
                command, args, text = self.parse_command(text)

                # Handle special commands like \#comment and \#include
                if command.startswith("#"):
                    if command == "#comment":
                        # Skip comment nodes
                        pass
                    elif command == "#include":
                        filename = args[0]
                        include_content = self.handle_include(filename)
                        current_node.add_child(DOMNode('include', include_content))
                    continue

                if command in self.macros:
                    expanded_macro = self.expand_macro(command, args)
                    current_node.add_child(DOMNode('p', expanded_macro))
                else:
                    # Handle section/subsection commands as new nodes
                    if command in ["section", "subsection", "subsubsection"]:
                        new_node = DOMNode(command, args[0])
                        current_node.add_child(new_node)
                        current_node = new_node  # Move down to new section
                    else:
                        current_node.add_child(DOMNode('p', f"\\{command} " + ' '.join(args)))
            else:
                # Handle plain text before next command
                if '{' in text:
                    text_block, text = self.parse_braces(text)
                else:
                    text_block, text = text, ''
                text_block = self.expand_variables(text_block)
                current_node.add_child(DOMNode('p', text_block))

        return root

    def handle_include(self, filename: str) -> str:
        """Handle the inclusion of an external file."""
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"File {filename} not found."

    def expand_dom(self, node: DOMNode) -> None:
        """Recursively expand macros, variables, and includes in the DOM."""
        for child in node.children:
            if child.tag == 'p':
                child.text = self.expand_variables(child.text)  # Expand variables in text nodes
            elif child.tag == 'include':
                include_content = child.text
                included_node = self.parse_content(include_content)
                node.add_child(included_node)  # Add included content as a child
            else:
                self.expand_dom(child)  # Recursively expand other nodes

    def to_xml_element(self, node: DOMNode) -> ET.Element:
        """Convert a DOMNode to an XML element."""
        element = ET.Element(node.tag)
        element.text = node.text.strip() if node.text else None
        for child in node.children:
            element.append(self.to_xml_element(child))
        return element

    def to_xml_string(self, root: DOMNode) -> str:
        """Convert the DOM tree to an XML string."""
        xml_root = self.to_xml_element(root)
        return ET.tostring(xml_root, encoding="unicode", method="xml")


# Example input with macros, variables, comments, and include
sile_input = r"""
\newcommand{\greet}[1]{Hello, #1!}
\def{\name}{Alice}

# Single-line comment that should be ignored
\#comment{This is a multi-line comment that will not be in the output.}

\section{Introduction}
This is the introduction paragraph, written by \${name}.

\subsection{Greeting}
Here is a greeting: \${greet}[Bob].

\#include{other_file.txt}
"""

# Initialize the parser
parser = Parser()

# Parse the input and build the DOM
dom_root = parser.parse_content(sile_input)

# Expand macros, variables, and includes in the DOM
parser.expand_dom(dom_root)

# Output the XML string
xml_output = parser.to_xml_string(dom_root)

# Print the XML output
print(xml_output)
