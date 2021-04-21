from typing import Optional, Union
try:
    from xml.etree.cElementTree import ElementTree, Element, SubElement
except (ModuleNotFoundError, ImportError):
    from xml.etree.ElementTree import ElementTree, Element, SubElement
from xy.exception import XYError
from xy.stdlib_overwrite.list import List
from xy.stdlib_overwrite.dict import Dict
from . import FileModel


class XMLObject:
    """
    tag： 标签名
    attrib： 属性，dict类型
    text： 文本
    tail： 元素相关联的附加属性，与格式缩进有关
    children： 子节点，list类型
    """
    def __init__(self, root: Union[Element, dict]):
        if isinstance(root, Element):
            self._init_element(root)
        elif isinstance(root, dict):
            self._init_dict(root)
        else:
            raise XYError("XMLObject 不接受 {} 类型".format(type(root)))

    def __str__(self):
        return f"{{tag: {self.tag}, attrib: {self.attrib}, text: {self.text}, tail: {self.tail}, children: {self.children}}}"

    def _init_element(self, root: Element):
        self.tag = root.tag
        self.attrib = root.attrib
        self.text = root.text
        self.tail = root.tail
        self.children = List(self.__class__(i) for i in root)

    def _init_dict(self, root: dict):
        self.tag = root["tag"]
        self.attrib = root.get("attrib", {})
        self.text = root.get("text")
        self.tail = root.get("tail")
        self.children = List(self.__class__(i) for i in root["children"])

    def to_dict(self) -> Dict:
        return Dict(
            tag=self.tag,
            attrib=self.attrib,
            text=self.text,
            tail=self.tail,
            children=List(i.to_dict() for i in self.children)
        )

    def to_element(self) -> Element:
        def add_element(parent, object):
            element = SubElement(parent, object.tag, object.attrib)
            element.text = object.text
            element.tail = object.tail
            for child in object.children:
                add_element(element, child)
        element = Element(self.tag, self.attrib)
        element.text = self.text
        element.tail = self.tail
        for child in self.children:
            add_element(element, child)
        return element


class XMLModel(FileModel):
    def __init__(self, xml_path: str, read_content: bool = False, read_data: bool = False):
        super().__init__(xml_path, read_content, read_data)

    def read_data(self, *args, **kwargs) -> XMLObject:
        self.data = XMLObject(ElementTree(file=self.path).getroot())
        return self.data

    def write_data(self, code_type: str = "utf-8", xml_declaration: Optional[bool] = True) -> XMLObject:
        element_tree = ElementTree(element=self.data.to_element())
        element_tree.write(self.path, encoding=code_type, xml_declaration=xml_declaration)
        return self.data

