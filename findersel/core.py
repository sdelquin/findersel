import subprocess

from findersel import settings


def get_selected_files():
    cmd = f'{settings.APPLESCRIPT_LAUNCHER} {settings.APPLESCRIPT_PATH}'
    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    yield from output.decode('utf-8').strip().split('\n')
