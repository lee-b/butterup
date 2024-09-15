# Variables
DOCBOOK_XML = language_reference.xml quickstart_tutorial.xml
DOCBOOK_PDF = language_reference.pdf quickstart_tutorial.pdf
DOCBOOK_HTML = language_reference.html quickstart_tutorial.html

# Source ButterXML files
BTR_FILES = language_reference.btr quickstart_tutorial.btr

# DocBook toolchain paths (customize if necessary)
DB2PDF = fopub  # Or docbook2pdf, dblatex, or xmlto pdf, depending on your setup
DB2TXT = xmlto txt  # Convert to plain text using xmlto
DB2HTML = xmlto html  # Convert to HTML using xmlto

# Targets

all: pdf html

pdf: $(DOCBOOK_PDF)

html: $(DOCBOOK_HTML)

# Convert ButterXML to DocBook XML
%.xml: %.btr
	# Assuming you have a tool butterxml_to_docbook for converting ButterXML to DocBook XML
	btr $< > $@

# Convert the XML DocBook files to PDF
%.pdf: %.xml
	$(DB2PDF) $<

# Convert the XML DocBook files to HTML
%.html: %.xml
	$(DB2HTML) $<

# Clean up generated files
clean:
	rm -f $(DOCBOOK_PDF) $(DOCBOOK_HTML) $(DOCBOOK_XML)

.PHONY: all pdf html clean
