"""Test Huffman coding"""

from huffman import Encoding

import pytest


def test_minimal() -> None:
    """You will want to test more than this..."""
    x = "aabacabaaa"
    enc = Encoding(x)
    assert x == enc.decode(enc.encode(x))

def make_enc(): 
    "Make different Encoding()"
    enc1 = Encoding("aabacabaaa")
    enc2 = Encoding("eabcdaabadaecbadacbacabaeadbacaedbaaecd")
    enc3 = Encoding("aaab")
    return enc1, enc2, enc3

def test_tree_building() -> None: 
    enc1, enc2, enc3 = make_enc()
    assert str(enc1.tree) == "Node(count=10, left=Leaf(letter='a', count=7), right=Node(count=3," \
        " left=Leaf(letter='b', count=2), right=Leaf(letter='c', count=1)))"
    
    assert str(enc2.tree) == "Node(count=39, left=Node(count=24, left=Node(count=13, left=Leaf(letter='b', count=7),"\
        " right=Leaf(letter='c', count=6)), right=Node(count=11, left=Leaf(letter='d', count=6),"\
            " right=Leaf(letter='e', count=5))), right=Leaf(letter='a', count=15))"
    
    assert str(enc3.tree) == "Node(count=4, left=Leaf(letter='a', count=3), right=Leaf(letter='b', count=1))"

def test_alphabet() -> None:
    enc1, enc2, enc3 = make_enc()
    assert str(enc1.alphabet) == "{'a': '0', 'b': '10', 'c': '11'}"
    assert str(enc2.alphabet) == "{'b': '000', 'c': '001', 'd': '010', 'e': '011', 'a': '1'}"   
    assert str(enc3.alphabet) == "{'a': '0', 'b': '1'}"

def test_encoding() -> None: 
    enc1, enc2, enc3 = make_enc()
    assert enc1.encode("aabacabaaa") == "0010011010000"
    assert enc1.encode("ccc") == "111111"
    assert enc1.encode("abcaaabcabbbbbcca") == "0101100010110101010101011110"
    assert enc2.encode("eabcdaabada") == "01110000010101100010101"
    assert enc2.encode("aabacabaaa") == "1100010011000111"
    assert enc2.encode("eeeeabc") == "0110110110111000001"
    assert enc3.encode("aaab") == "0001"
    assert enc3.encode("aabaabaaa") == "001001000"
    assert enc3.encode("abababab") == "01010101"

def test_decoding() -> None: 
    enc1, enc2, enc3 = make_enc()
    assert enc1.decode("01011") == "abc"
    assert enc1.decode("11100110") == "cbaca"
    assert enc1.decode("1111111000010") == "cccbaaab"
    assert enc2.decode("0000010100111") == "bcdea"
    assert enc2.decode("111000010011000") == "aaabdeb"
    assert enc2.decode("1011010001000") == "aedcb"
    assert enc3.decode("01") == "ab"
    assert enc3.decode("00000000000001") == "aaaaaaaaaaaaab"
    assert enc3.decode("0101010101") == "ababababab"

def test_decoding_encoding() -> None: 
    enc1, enc2, enc3 = make_enc()
    assert enc1.decode(enc1.encode("aabacabaaa")) == "aabacabaaa"
    assert enc2.decode(enc2.encode("eabcdaabadaecbadacbacabaeadbacaedbaaecd")) == "eabcdaabadaecbadacbacabaeadbacaedbaaecd"
    assert enc3.decode(enc3.encode("aaab")) == "aaab"

def test_errors() -> None: 
    enc1, enc2, enc3 = make_enc()

    with pytest.raises(KeyError):
        enc1.encode("abcde")
    
    enc = Encoding("a")
    with pytest.raises(AttributeError):
        enc.decode("00")
    
    with pytest.raises(TypeError):
        enc1.decode(00)
    
