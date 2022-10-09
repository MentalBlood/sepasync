# Sepasync

Fast. Stubborn. Tool for downloading entries from Stanford Encyclopedia of Philosophy

See also [bandasync](https://github.com/MentalBlood/bandasync)

## Installation

```bash
pip install git+https://github.com/MentalBlood/sepasync
```

## Usage

To get help:

```bash
python -m sepasync -h
```

Tool will not download entry if it already exists

### Entry:

```bash
python -m sepasync https://plato.stanford.edu/entries/some_entry
```

### All entries:

```bash
python -m sepasync https://plato.stanford.edu/published.html
```

### Tasks

```bash
python -m sepasync -f <path_to_json>
```

JSON should be like:

```json
{
    "D:/some/path": [
        "https://plato.stanford.edu/entries/some_entry/",
        "https://plato.stanford.edu/entries/some_other_entry/"
    ],
    "D:/some/other/path": [
        "https://plato.stanford.edu/entries/one_more_entry/"
    ]
}
```

## Bugs

No known, if you found one please report [here](https://github.com/MentalBlood/sepasync/issues)