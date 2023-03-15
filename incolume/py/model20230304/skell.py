"""Skell structure."""

import logging
import typing


def skell(
    *args: typing.Tuple, **kwargs: typing.Dict
) -> typing.Dict[str, typing.Any]:
    """Esqueleto de função.
    args:
        args: Argumentos.
        kwargs: Argumentos chaveados.
    
    returns:
        Um dicionário com os argumentos de entrada.
    
    Examples:
        >>> skell(1, 2, 3)
        {'args': (1, 2, 3)}

        >>> skell(a=1, b=2, c=3)
        {'args': (), 'a': 1, 'b': 2, 'c': 3}
    """
    result = {'args': args, **kwargs}
    logging.debug(result)
    logging.info(f'Args: {bool(args)}, kwargs: {bool(kwargs)}')
    return result


def run():
    """Run this."""
    skell(1, 2, 3, a=7)


if __name__ == '__main__':
    run()
