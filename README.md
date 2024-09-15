# ButterUp

**ButterUp** is ~~butter~~ better than XML 😉

ButterUp is a *lightweight*, formally defined, super-simple markup language and preprocessor inspired by LaTeX, for both documents and data.  It's ideal as a frontend preprocessor for DocBook and DITA, or any XML/XSLT/XSL-FO pipeline, but can also just make writing XML data files or XHTML documents more pleasant.

## Why ButterUp?

- **LaTeX-like syntax**: Use familiar backslash commands and curly braces for structure, with support for macros, variables, and includes.
- **Flexible output**: Convert your ButterUp files into **DocBook XML**, **PDF**, **HTML**, or other formats.
- **Lightweight and readable**: Write structured documents without all the overhead of XML markup.
- A deliberately limited set of powerful preprocessor features: variables, macros, and includes.

---

## Example: How It Works

Here's a quick taste of ButterUp in action:

### Input: ButterUp `.btr` File

```latex
\section{Welcome to ButterUp}
Writing structured documents is easy with ButterUp! Let's see a few features:

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
Welcome to ButterUp
Writing structured documents is easy with ButterUp! Let's see a few features:

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

## Why You'll Love ButterUp

1. **Simple LaTeX-like Syntax**: ButterUp uses lightweight syntax, so there's no need to get bogged down in verbose XML or complex tags. If you're familiar with LaTeX, you'll feel right at home!
   
2. **Macros & Variables**: Create reusable pieces of text with macros and variables for a truly modular document creation experience. 

3. **Multiple Output Formats**: Whether you need **PDF**, **HTML**, or **DocBook XML**, ButterUp makes it easy to convert your `.btr` files to the format of your choice with a few simple commands.

---

## Getting Started

### 1. Install ButterUp

You can install ButterUp using `pip` directly from the GitHub repository:

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
ButterUp is a lightweight markup language that makes document generation a breeze!

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

If you'd like to contribute to ButterUp or improve it, you can easily get started by cloning the repository and installing the dependencies:

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

ButterUp is licensed under the Affero GPL version 3 License (only). See the [LICENSE](LICENSE) file for more information.

---

## Example `.btr` File

Here's a more advanced example of what you can do with ButterUp:

```latex
\section{Welcome to ButterUp}
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

We hope you enjoy using ButterUp to create lightweight, structured documents. Happy writing!
