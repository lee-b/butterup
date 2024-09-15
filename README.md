# ButterXML

**ButterXML** is ~~butter~~ better than XML 😉

ButterXML is a *lightweight*, formally defined, super-simple markup language and preprocessor inspired by LaTeX, without the xml `<starttag><subtag>...</subtag></endtag>` pain. It supports file inclusions, variables, and macros natively.  Otherwise, what you put in is what you get out, except that you write pretty, lightweight `\cmd{... \subcmd ...}` syntax, and it writes the ugly `<xmltag>... <subxmltag/> ...</xmltag>` nonsense for you, in your pipeline, so you never have to write it again.

Whether you need to generate well-known document formats like **DocBook XML** or **DITA**, or your own custom XML data files or custom XML fragments for `xsl-fo`, ButterXML will make the source code/doc writing more lightweight and more human-readable.

A few special characters and commands are used, which can be escaped. The rest of the `utf8` input is passed through to your target doc verbatim, so things like unicode characters and MathML will "just work", if your target document format support them.

## Why ButterXML?

- **LaTeX-like syntax**: Use familiar backslash commands and curly braces for structure, with support for macros, variables, and includes.
- **Flexible output**: Convert your ButterXML files into **DocBook XML**, **PDF**, **HTML**, or other formats.
- **Lightweight and readable**: Write structured documents without all the overhead of XML markup.

---

## Example: How It Works

Here's a quick taste of ButterXML in action:

### Input: ButterXML `.btr` File

```latex
\section{Welcome to ButterXML}
Writing structured documents is easy with ButterXML! Let's see a few features:

\subsection{Variables}
Define a variable using \\def:

\def{\name}{Alice}
My name is \${name}.

\subsection{Macros}
Define and expand macros just like in LaTeX:

\newcommand{\greet}[1]{Hello, \#1!}
\greet{world}

\subsection{Includes}
Include content from other files:

\#include{chapter1.btr}
```

### Output: PDF/HTML (Rendered)

```latex
Welcome to ButterXML
Writing structured documents is easy with ButterXML! Let's see a few features:

Variables
Define a variable using def:
My name is Alice.

Macros
Define and expand macros just like in LaTeX:
Hello, world

Includes
(Contents of chapter1.btr are inserted here)
```

---

## Why You'll Love ButterXML

1. **Simple LaTeX-like Syntax**: ButterXML uses lightweight syntax, so there's no need to get bogged down in verbose XML or complex tags. If you're familiar with LaTeX, you'll feel right at home!
   
2. **Macros & Variables**: Create reusable pieces of text with macros and variables for a truly modular document creation experience. 

3. **Multiple Output Formats**: Whether you need **PDF**, **HTML**, or **DocBook XML**, ButterXML makes it easy to convert your `.btr` files to the format of your choice with a few simple commands.

---

## Getting Started

### 1. Install ButterXML

You can install ButterXML using `pip` directly from the GitHub repository:

```bash
pip install git+https://github.com/yourusername/butterxml.git
```

Or, clone the repository and install it locally:

```bash
git clone https://github.com/yourusername/butterxml.git
cd butterxml
poetry install
```

### 2. Write Your First Document

Create a simple file named `document.btr`:

```latex
\section{Introduction}
ButterXML is a lightweight markup language that makes document generation a breeze!

\subsection{Features}
- LaTeX-like syntax
- Multiple output formats
- Lightweight and easy to use
```

### 3. Convert to Your Desired Format

Once you've written your `.btr` file, you can convert it to different formats like **DocBook XML**, **PDF**, or **HTML**.

#### Convert to DocBook XML

```bash
btr document.btr > document.xml
```

#### Convert to PDF

```bash
fopub document.xml
```

#### Convert to HTML

```bash
xmlto html document.xml
```

---

## Features

### Sections and Subsections

Create sections and subsections with easy-to-read commands:

```latex
\section{Main Section}
This is the main section.

\subsection{Subsection}
This is a subsection.
```

### Variables

Define and use variables:

```latex
\def{\author}{Jane Doe}
Author: \${author}
```

### Macros

Define reusable macros with parameters:

```latex
\newcommand{\greet}[1]{Hello, \#1!}
\greet{Alice}
```

### Includes

Include content from other `.btr` files:

```latex
\#include{chapter1.btr}
```

---

## Development

If you'd like to contribute to ButterXML or improve it, you can easily get started by cloning the repository and installing the dependencies:

```bash
git clone https://github.com/yourusername/butterxml.git
cd butterxml
poetry install
```

### Building the Project

To build the project and create distributable files (such as wheels), run:

```bash
poetry build
```

This will generate the distribution files under the `dist/` folder.

### Running Tests

To run the tests for the project:

```bash
poetry run pytest
```

---

## License

ButterXML is licensed under the Affero GPL version 3 License (only). See the [LICENSE](LICENSE) file for more information.

---

## Example `.btr` File

Here's a more advanced example of what you can do with ButterXML:

```latex
\section{Welcome to ButterXML}
Let me show you a few cool features.

\subsection{Variables}
You can define variables with \def:

\def{\userName}{John}
Hi, my name is \${userName}.

\subsection{Macros}
Macros allow for reusable components:

\newcommand{\intro}[1]{Welcome, \#1!}
\intro{friend}
```

After running the `btr` command, you can convert this into the output format of your choice!

```bash
btr yourfile.btr
```

---

We hope you enjoy using ButterXML to create lightweight, structured documents. Happy writing!
