try:
    from xml.etree.cElementTree import ElementTree
except ImportError:
    from xml.etree.ElementTree import ElementTree


class _XMLTree(ElementTree):
    def __init__(self, path):
        super().__init__()
        self.parse(path)


class XMLModel:
    """
    tag： 标签名
    attrib：属性，dict类型
    text： 文本
    sub_xml： 子节点，list类型
    """

    def __init__(self, xml):
        if isinstance(xml, str):
            xml = _XMLTree(xml).getroot()
        self.__init_params(xml)

    def __init_params(self, root):
        self.tag = root.tag
        self.attrib = root.attrib
        self.text = root.text
        self.sub_xml = [self.__class__(i) for i in root]

    def to_dict(self):
        return {
            "tag": self.tag,
            "attrib": self.attrib,
            "text": self.text,
            "sub_xml": [i.to_dict() for i in self.sub_xml]
        }

