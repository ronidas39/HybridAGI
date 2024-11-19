from docling.document_converter import DocumentConverter
source = "/Users/roni/Documents/GitHub/HybridAGI/Tutorial1/sample.pdf"  # PDF path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "### Docling Technical Report[...]"


