from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path('.').resolve()

APPLESCRIPT_LAUNCHER = config('APPLESCRIPT_LAUNCHER', default='osascript')
APPLESCRIPT_NAME = config('APPLESCRIPT_NAME', default='findersel.applescript')
APPLESCRIPT_PATH = PROJECT_DIR / 'scripts' / APPLESCRIPT_NAME
