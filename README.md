# wordle-minigame
A simple and fun wordle minigame made using Python.

## Installation
- Clone this repository
- Navigate to the project directory
- Ensure you have [Python 3+](https://www.python.org/downloads/) installed
- Open `start.bat` and enjoy.

## Adding more words
If you have a list of words seperated by something and you want to generate them into the `words.txt` correctly, you can run the `generate.bat` and enter that list of words.
By default it will only work for words seperated by a `" "`. If you want to change the filter navigate into `generate.py` with your favorite text editor and change this line to match for your filter:
```
for word in words.split(" "):
```
For example, in order to filter between ',' you can change it to this:
```
for word in words.split(","):
```
