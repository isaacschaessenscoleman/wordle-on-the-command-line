# create_wordlist.py

import pathlib
import sys
from string import ascii_letters


in_path = pathlib.Path(sys.argv[1]) # file to retrieve words from
out_path = pathlib.Path(sys.argv[2]) # file to put those retrieved words in

words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding="utf-8").split()
        if all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (len(word), word),
)
out_path.write_text("\n".join(words))