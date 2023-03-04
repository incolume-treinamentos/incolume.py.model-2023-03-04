import pytest
from incolume.py.model20230304 import __version__
import re
__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (__version__, True),
        )
    )
    def test_version(self, entrance, expected):
        """Validação de versionamento semântico."""
        assert bool(re.fullmatch(r"\d+(\.\d+){2}(-?\w+\.?\d+)?", entrance, re.I)) == expected
