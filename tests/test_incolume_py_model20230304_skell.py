import re

import pytest

from incolume.py.model20230304 import skell

__author__ = '@britodfbr'


class TestCase:
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (('1', 2, 'a', 1, '3', 3), {'args': ('1', 2, 'a', 1, '3', 3)}),
            (('1', 'a', '3'), {'args': ('1', 'a', '3')}),
            ((2, 1, 3), {'args': (2, 1, 3)}),
        ),
    )
    def test_args(self, entrance, expected):
        """Validação de entrada em args."""
        assert skell.skell(*entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (
                {'a': '1', 'b': 2, 'c': 3},
                {'a': '1', 'args': (), 'b': 2, 'c': 3},
            ),
            (
                {'a': '1', 'b': 2, 'c': 3},
                {'a': '1', 'args': (), 'b': 2, 'c': 3},
            ),
        ),
    )
    def test_kwargs(self, entrance, expected):
        """Validação de entrada em kwargs."""
        assert skell.skell(**entrance) == expected
