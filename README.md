# tiptally

Split a restaurant bill and its tip among people, to the cent.

Python 3.12, standard library only.

## Installation

<!-- Stub from /gabe-init (CLI project type). .kdbp/DOCS.md maps pyproject.toml → this section. -->

## Usage

```
python3 -m tiptally AMOUNT PEOPLE [--tip PCT] [--weights W1,W2,...]
```

- `AMOUNT`: the bill before tip, in decimal (`120.50`). At most two decimals.
- `PEOPLE`: how many people share it.
- `--tip PCT`: tip percentage, a whole number (default 0).
- `--weights W1,W2,...`: split in proportion to whole-number weights, one per person
  (`2,1,1` makes Person 1 pay twice what each of the others pays). The number of weights
  must equal `PEOPLE`. Without it the bill is split evenly.

Example:

```
$ python3 -m tiptally 120.50 4 --tip 10
Person 1: 33.14
Person 2: 33.14
Person 3: 33.14
Person 4: 33.13
Total: 132.55 (tip 12.05)
```

Weighted:

```
$ python3 -m tiptally 100 3 --tip 10 --weights 2,1,1
Person 1: 55.00
Person 2: 27.50
Person 3: 27.50
Total: 110.00 (tip 10.00)
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
