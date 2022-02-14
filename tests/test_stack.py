import pytest
from src.stack import Stack


@pytest.mark.parametrize('data', [('()', True),
                                  ('(()', False),
                                  ('{}', True),
                                  ('[]', True),
                                  ('[({})]', True),
                                  ('[({})]]', False)
                                  ])
def test_1(data):
    item, expected = data
    symbol_pairs = {'(': ')',
                    '[': ']',
                    '{': '}'}

    openers = symbol_pairs.keys()

    stack = Stack()
    index = 0
    while index < len(item):
        symbol = item[index]
        if symbol in openers:
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False
            else:
                top_item = stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index += 1
    assert stack.is_empty() == expected
