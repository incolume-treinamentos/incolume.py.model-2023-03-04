from pathlib import Path
from tomli import load
import logging

versionfile = Path(__file__).parent / 'version.txt'
configfile = Path(__file__).parents[3] / 'pyproject.toml'

logging.debug(f'{versionfile.is_file()=}, {configfile.is_file()=}')
with configfile.open('rb') as file:
    logging.debug((version := load(file)['tool']['poetry']['version']))
    versionfile.write_text(f'{version}\n')

__version__ = versionfile.read_text().strip()

if __name__ == '__main__':  # pragma: no cover
    print(__version__)
