# findersel

Get selected files from [macOS Finder](https://support.apple.com/HT201732) and use them programatically within your Python program.

## Installation

```console
$ pip install findersel
```

## Usage

Select some files on Finder:

![Finder screenshot](finder-screenshot.png)

And get the selected files:

```python
>>> import findersel

>>> list(findersel.get_selected_files())
['/Users/sdelquin/findersel/LICENSE',
 '/Users/sdelquin/findersel/Makefile',
 '/Users/sdelquin/findersel/README.md',
 '/Users/sdelquin/findersel/requirements.txt',
 '/Users/sdelquin/findersel/setup.cfg',
 '/Users/sdelquin/findersel/setup.py']
```

> Note than the function returns a **generator**.

## Changelog

| 1.0.1 | 20/06/2021 |
| ----- | ---------- |

- Add documentation.

| 0.1.0 | 20/06/2021 |
| ----- | ---------- |

- Add initial code.

## License

MIT
