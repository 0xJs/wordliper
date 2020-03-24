# worldliper

A simple wordlist generator to generate worldlists including company name, locations, months, periods and appending years, capitalizing first letters. Basicly permutating the wordlist.

Things I still want to add:
- Use leetspeak as the first leetspeak character for every word in the wordlist.

## Getting Started
```
Git clone https://github.com/Kadeeli/wordliper
python3 wordliper.py
```

### Preview
```
kadeeli@Pentest:/opt/wordliper$ ./wordliper.py 

usage: wordliper.py [-h] [-f FILE] [-s STRINGS [STRINGS ...]] [-m] [-se]
                    [-dutch] [-aY YEARS [YEARS ...]] [-AS]
                    [-As ASTRINGS [ASTRINGS ...]] [-PS]
                    [-Ps PSTRINGS [PSTRINGS ...]] [-C] [-min MIN] [-max MAX]
                    [-minc] [-o OUTPUT]

A simple wordlist generator to generate worldlists including custom strings
such as company name, locations, months, periods and appending years,
capitalizing first letters. Basicly permutating the wordlist.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  used to supply a wordlist file as input, every word
                        has to be a newline
  -s STRINGS [STRINGS ...], --strings STRINGS [STRINGS ...]
                        used to supply a(or multiple) strings such as company
                        name(s), locations etc. to be added to the wordlist.
                        These need to be seperated by spaces
  -m, --months          used to add all months of the year to the worldlist
  -se, --seasons        used to add all season to the wordlist
  -dutch, --dutch       used to translate months and seasons to dutch
  -aY YEARS [YEARS ...], --years YEARS [YEARS ...]
                        used to append a range of years to every word in the
                        wordlist, seperated by spaces for example 2018 2020
  -AS, --asymbols       used to append symbols to every word in the wordlist,
                        the list of symbols can be edited in the code
  -As ASTRINGS [ASTRINGS ...], --astrings ASTRINGS [ASTRINGS ...]
                        used to append strings to every word in the wordlist
                        before the symbols are applied
  -PS, --psymbols       used to prepend symbols to every word in the wordlist,
                        the list of symbols can be edited in the code
  -Ps PSTRINGS [PSTRINGS ...], --pstrings PSTRINGS [PSTRINGS ...]
                        used to prepend strings to every word in the wordlist
                        before the symbols are applied
  -C, --capital         used to capitalize every first letter in the word
  -min MIN, --min MIN   used to set the minimum password length of the
                        outputted passwords
  -max MAX, --max MAX   used to set the maximum password length of the
                        outputted passwords
  -minc, --minc         Set password requirement to have atleast a capital
                        letter, removes every word that does not
  -o OUTPUT, --output OUTPUT
                        Directs the output to a name of your choice
```

**EXAMPLE**
```
kadeeli@Pentest:/opt/wordliper$ sudo ./wordliper.py -f shortwordlist.txt -m -se -dutch -aY 2019 2020 -AS -C --min 6 --max 16 -minc -o newwordlist.txt

[+] Translating months and seasons to dutch variants
[+] Adding words from shortwordlist.txt to the wordlist
[+] Adding months to the worldlist
[+] Adding seasons to the worldlist
[+] Appending years to every word in the wordlist
[+] Appending symbols to every word in the wordlist
[+] Capitalizing the first letter of every word
[-] Deleting words if smaller then 6 characters and larger then 16 characters
[-] Deleting words that do not contain a capital character
[=] Generated 702 words

--output example--
kadeeli@Pentest:/opt/wordliper$ tail -n 10 newwordlist.txt 

kadeeli@Pentest:/opt/wordliper$ tail -n 10 newwordlist.txt 
Zomer2020.
Zomer2020/
Zomer2020123
Zomer20201234
Zomer2020?
Zomer2020@
Zomer2020_
Zomer?
Zomer@
Zomer_

```

## Authors

* **Jony Schats** - *Initial work* - [Kadeeli](https://github.com/Kadeeli)



