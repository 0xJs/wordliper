# worldliper

A simple wordlist generator to generate worldlists including company name, locations, months, periods and appending years, capitalizing first letters. Basicly permutating the wordlist.

Things I still want to add:
- Use wordlist as input file
- Use 1337 as the first 1337 character for every word in the wordlist.

## Getting Started
```
Git clone https://github.com/Kadeeli/wordliper
python3 wordliper.py
```

### Preview
```
usage: wordliper.py [-h] [-s STRINGS [STRINGS ...]] [-m] [-p]
                    [-aY YEARS [YEARS ...]] [-AS]
                    [-As ASTRINGS [ASTRINGS ...]] [-PS]
                    [-Ps PSTRINGS [PSTRINGS ...]] [-C] [-min MIN] [-max MAX]
                    [-o OUTPUT]

A simple wordlist generator to generate worldlists including custom strings
such as company name, locations, months, periods and appending years,
capitalizing first letters. Basicly permutating the wordlist.

optional arguments:
  -h, --help            show this help message and exit
  -s STRINGS [STRINGS ...], --strings STRINGS [STRINGS ...]
                        used to supply a(or multiple) strings such as company
                        name(s), locations etc, seperated by spaces to be
                        added to the wordlist
  -m, --months          used to add all months of the year to the worldlist
  -p, --periods         used to add all periods of the year to the worldlist,
                        like spring etc
  -aY YEARS [YEARS ...], --years YEARS [YEARS ...]
                        used to append a year range to every word in the
                        wordlist
  -AS, --asymbols       used to append symbols to every word in the wordlist
  -As ASTRINGS [ASTRINGS ...], --astrings ASTRINGS [ASTRINGS ...]
                        used to append strings to every word in the wordlist
                        before the symbols are applied
  -PS, --psymbols       used to prepend symbols to every word in the wordlist
  -Ps PSTRINGS [PSTRINGS ...], --pstrings PSTRINGS [PSTRINGS ...]
                        used to prepend strings to every word in the wordlist
                        before the symbols are applied
  -C, --capital         used to capitalize every first letter in the word
  -min MIN, --min MIN   used to set the minimum password length
  -max MAX, --max MAX   used to set the maximum password length
  -o OUTPUT, --output OUTPUT
                        Directs the output to a name of your choice
```

**EXAMPLE**
```
sudo ./wordliper.py -s kadeeli -m -p -aY 2019 2020 -AS -PS -C -min 8 -max 16 -o example.txt

[+] Adding months to the worldlist
[+] Adding periods to the worldlist
[+] Adding the provided strings to the worldlist
[+] Appending years to every word in the wordlist
[+] Appending symbols to every word in the wordlist
[+] Prepending symbols to every word in the wordlist
[+] Capitalizing the first letter of every word
[-] Deleting words if smaller then 8 characters and larger then 16 characters
[=] Generated 2118 words

```

## Authors

* **Jony Schats** - *Initial work* - [Kadeeli](https://github.com/Kadeeli)



