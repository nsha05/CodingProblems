given_word = input()

new_word = ""

storage = {
    "a": "a",
    "b": "bac",
    "c": "cad",
    "d": "def",
    "e": "e",
    "f": "feg",
    "g": "geh",
    "h": "hij",
    "i": "i",
    "j": "jik",
    "k": "kil",
    "l": "lim",
    "m": "mon",
    "n": "nop",
    "o": "o",
    "p": "poq",
    "q": "qor",
    "r": "ros",
    "s": "sut",
    "t": "tuv",
    "u": "u",
    "v": "vuw",
    "w": "wux",
    "x": "xuy",
    "y": "yuz",
    "z": "zuz",
}

for i in range(len(given_word)):
    new_word += storage[given_word[i]]
print(new_word)