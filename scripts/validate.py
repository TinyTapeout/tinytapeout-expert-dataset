from lxml import etree
import sys

try:
    # Parse and validate XML
    tree = etree.parse("data/dataset.xml")

    # Count facts (assuming facts are elements named "fact")
    fact_count = len(tree.findall(".//fact"))

    # Create markdown output
    output = f"""
## XML Validation Results
    
✅ XML file is valid
    
### Statistics

- Total number of facts: **{fact_count}**
"""

    print(output)

except etree.XMLSyntaxError as e:
    print(f"## XML Validation Results\n\n❌ XML Syntax Error:\n```\n{str(e)}\n```")
    sys.exit(1)
except FileNotFoundError:
    print("## XML Validation Results\n\n❌ Error: data/dataset.xml file not found")
    sys.exit(1)
