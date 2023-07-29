import re

import pytest

from incolume.py.model20230304 import __version__

__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (__version__, True),
            ('1.0.0-alpha.0', True),
            ('111.110.110-alpha.111', True),
            ('1.0.0-a.999', True),
            ('1.0.0.alpha.0', False),
            ('1.0', False),
            ('1', False),
        ),
    )
    def test_version(self, entrance, expected):
        """Validação de versionamento semântico."""
        assert (
            bool(re.fullmatch(r'\d+(\.\d+){2}(-?\w+\.?\d+)?', entrance, re.I))
            == expected
        )
