from xml.dom import minidom

class XmlNode:
    """An XML node represents a single field in an XML document."""

    def __init__(self, dom_elem):
        """Construct an XML node from a DOM element."""
        self.elem = dom_elem
    
    @classmethod
    def make_root(cls, xml_filename):
        return cls(minidom.parse(xml_filename))

    def get_data(self):
        """Extract data from a DOM node."""
        for child in self.elem.childNodes:
            if child.nodeType == child.TEXT_NODE:
                return str(child.data)
        return None

    def get_attribute_value(self, name):
        """Returns the value of the attribute having the specified name."""
        return str(self.elem.attributes[name].value)

    def get_child(self, tag):
        """Returns the first child node having the specified tag."""
        return XmlNode(self.elem.getElementsByTagName(tag)[0])
    
    def get_children(self, tag):
        """Returns a list of child nodes having the specified tag."""
        return [XmlNode(x) for x in self.elem.getElementsByTagName(tag)]