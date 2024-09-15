import pytest
import sys
import io
from butterxml.__main__ import main

def test_main_with_input_file(tmp_path, capsys):
    input_file = tmp_path / "test_input.btr"
    input_file.write_text(r"\section{Test Section}This is a test.")

    sys.argv = ["butterxml", str(input_file)]
    main()
    captured = capsys.readouterr()
    assert "<root><section>Test Section<p>This is a test.</p></section></root>" in captured.out

def test_main_with_output_file(tmp_path, capsys):
    input_file = tmp_path / "test_input.btr"
    input_file.write_text(r"\section{Test Section}This is a test.")
    output_file = tmp_path / "test_output.xml"

    sys.argv = ["butterxml", str(input_file), "-o", str(output_file)]
    main()
    captured = capsys.readouterr()
    assert f"XML output written to {output_file}" in captured.out
    
    with open(output_file, 'r') as f:
        content = f.read()
    assert "<root><section>Test Section<p>This is a test.</p></section></root>" in content

def test_main_with_nonexistent_input_file(capsys):
    sys.argv = ["butterxml", "nonexistent_file.btr"]
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "Error: Input file 'nonexistent_file.btr' not found." in captured.stderr
