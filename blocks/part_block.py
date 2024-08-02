from typing import List, Optional


class Part:
    """
    Represents a graphical or textual component in a UI framework.
    
    Attributes:
        size (int): Size of the part in pixels.
        part_id (int): Unique identifier for the part.
        part_type (int): Type of the part, indicating its role or function.
        flags (int): Additional flags that modify the behavior or appearance of the part.
        top (int), left (int), bottom (int), right (int): Positioning coordinates of the part.
        show_name (bool): Indicates whether the part's name should be displayed.
        hilite (bool): Indicates whether the part should be highlighted.
        auto_hilite (bool): Indicates whether highlighting should be automatically applied based on certain conditions.
        family (int): Identifier for the font family used by the part.
        style (int): Style settings for the part, such as bold or italic.
        title_width (int): Width of the title area within the part.
        icon_id (int): Identifier for an icon associated with the part.
        text_align (int): Alignment setting for the text within the part.
        text_font (int): Font settings for the text within the part.
        text_size (int): Size setting for the text within the part.
        text_style (int): Additional style settings for the text within the part.
        text_height (int): Height setting for the text within the part.
        name (str): Name of the part, typically used for identification purposes.
        part_script (str): Script or code associated with the part, allowing for dynamic behavior.
        more_flags (Optional[int]): Additional flags that can be used to further customize the part's behavior or appearance.
    """
    def __init__(self, size: int, part_id: int, part_type: int, flags: int, top: int, left: int, bottom: int, right: int, 
                 show_name: bool, hilite: bool, auto_hilite: bool, family: int, style: int, 
                 title_width: int, icon_id: int, text_align: int, text_font: int, text_size: int, 
                 text_style: int, text_height: int, name: str, part_script: str,
                 more_flags: Optional[int] = None):
        self.size = size
        self.part_id = part_id
        self.part_type = part_type
        self.flags = flags
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        self.show_name = show_name
        self.hilite = hilite
        self.auto_hilite = auto_hilite
        self.family = family
        self.style = style
        self.title_width = title_width
        self.icon_id = icon_id
        self.text_align = text_align
        self.text_font = text_font
        self.text_size = text_size
        self.text_style = text_style
        self.text_height = text_height
        self.name = name
        self.part_script = part_script
        self.more_flags = more_flags

    def __repr__(self) -> str:
        return (f"Part(size={self.size}, part_id={self.part_id}, part_type={self.part_type}, flags={self.flags}, "
                f"top={self.top}, left={self.left}, bottom={self.bottom}, right={self.right}, "
                f"show_name={self.show_name}, hilite={self.hilite}, auto_hilite={self.auto_hilite}, family={self.family}, "
                f"style={self.style}, title_width={self.title_width}, icon_id={self.icon_id}, text_align={self.text_align}, "
                f"text_font={self.text_font}, text_size={self.text_size}, text_style={self.text_style}, text_height={self.text_height}, "
                f"name='{self.name}', part_script='{self.part_script}', more_flags={self.more_flags})")

class PartContent:
    """
    Represents the content of a Part, including its size, content, and optional styling information.
    
    Attributes:
        part_id (int): Unique identifier for the part.
        content_size (int): Size of the content in pixels.
        content (str): The actual content of the part, such as text or HTML.
        styles_length (Optional[int]): Length of the styles data array.
        styles_data (Optional[str]): Serialized styles data, if any.
        text_data (Optional[str]): Serialized text data, if any.
        name (Optional[str]): Name of the content, if applicable.
        script (Optional[str]): Script or code associated with the content, if any.
    """
    
    def __init__(self, part_id: int, content_size: int, content: str, styles_length: Optional[int] = None, 
                 styles_data: Optional[str] = None, text_data: Optional[str] = None, name: Optional[str] = None, 
                 script: Optional[str] = None):
        self.part_id = part_id
        self.content_size = content_size
        self.content = content
        self.styles_length = styles_length
        self.styles_data = styles_data
        self.text_data = text_data
        self.name = name
        self.script = script

    def __repr__(self) -> str:
        return (f"PartContent(part_id={self.part_id}, content_size={self.content_size}, content='{self.content}', "
                f"styles_length={self.styles_length}, styles_data='{self.styles_data}', text_data='{self.text_data}', "
                f"name='{self.name}', script='{self.script}')")