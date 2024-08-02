# !blocks.py
"""
This module defines classes for handling blocks in a storage system.
"""

from collections import deque
from typing import List

class BlockType:
    """
    Enum-like class representing different types of blocks.
    
    Each attribute represents a unique type of block.
    """
    STAK = 'STAK'
    MAST = 'MAST'
    LIST = 'LIST'
    PAGE = 'PAGE'
    BKGD = 'BKGD'
    CARD = 'CARD'
    BMAP = 'BMAP'
    FREE = 'FREE'
    STBL = 'STBL'
    FTBL = 'FTBL'
    PRNT = 'PRNT'
    PRST = 'PRST'
    PRFT = 'PRFT'
    TAIL = 'TAIL'

class Block:
    """
    Represents a block in a storage system.
    
    Attributes:
        block_size (int): Size of the block in bytes.
        block_type (str): Type of the block (e.g., STAK, MAST).
        block_id (int): Unique identifier for the block.
        data (bytes): Data stored in the block.
    """
    def __init__(self, block_size: int, block_type: str, block_id: int, data: bytes) -> None:
        """
        Initializes a new instance of the Block class.
        
        Args:
            block_size (int): Size of the block in bytes.
            block_type (str): Type of the block (e.g., STAK, MAST).
            block_id (int): Unique identifier for the block.
            data (bytes): Data stored in the block.
        """
        self.block_size = block_size
        self.block_type = block_type
        self.block_id = block_id
        self.data = data
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Block object.
        
        Returns:
            str: String representation of the Block object including its size, type, ID, and data length.
        """
        return (f"Block(block_size={self.block_size}, block_type='{self.block_type}', "
                f"block_id={self.block_id}, data_length={len(self.data)})")
