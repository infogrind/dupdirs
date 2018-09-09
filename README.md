# dupdir - Find duplicates in different directories

## Installation

### Manual

Clone this repository and put the file `dupdirs` into a location of your
preference (it should be on your path).

### Using Homebrew

On OS X you can install the script via [Homebrew](https://brew.sh/), from my
personal tap:

```sh
brew tap infogrind/homebrew-tap  # If not already done
brew install dupdirs
```


## Usage

```sh
Usage: dupdirs <dir1> <dir2>

Prints all those directories from <dir1> that are also present in <dir2>. That
is, a directory of the same name is present in <dir2>.

Options:
    -f  Enable fuzzy string comparison
    -m  Minimum score for fuzzy search (only relevant if -f is given)
    -h  Show this help
```


## Requirements

The script requires the `fuzzywuzzy` Python package to be installed. If you use
Homebrew to install it, this dependency is automatically installed.
