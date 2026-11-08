# tiptally

Split a restaurant bill and its tip among people, to the cent.

Python 3.12, standard library only.

## Installation

<!-- Stub from /gabe-init (CLI project type). .kdbp/DOCS.md maps pyproject.toml → this section. -->

## Usage

```
python3 -m tiptally AMOUNT PEOPLE [--tip PCT]
```

- `AMOUNT`: the bill before tip, in decimal (`120.50`). At most two decimals.
- `PEOPLE`: how many people share it.
- `--tip PCT`: tip percentage, a whole number (default 0).

Example:

```
$ python3 -m tiptally 120.50 4 --tip 10
Person 1: 33.14
Person 2: 33.14
Person 3: 33.14
Person 4: 33.13
Total: 132.55 (tip 12.05)
```

The shares always add up exactly to the bill plus the tip. Cents that do not divide
evenly go to the first payers, one each. See [docs/design.md](docs/design.md).

## Commands

<!-- Stub from /gabe-init (CLI project type). .kdbp/DOCS.md maps CLI source → this section. -->

## Development

```
ruff check tiptally tests
python3 -m pytest tests -q
```
