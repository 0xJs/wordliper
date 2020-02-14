# worldliper

A simple wordlist generator to generate worldlists including company name, locations, months, periods and appending years, capitalizing first letters. Basicly permutating the wordlist.

Things I still want to add:
- Append random strings
- Prepend random strings
- Append set of symbols
- Prepend set of symbols
- Use wordlist as input file

## Getting Started

Git clone https://github.com/Kadeeli/wordliper
python3 wordliper.py

### Preview

usage: wordliper.py [-h] [-c COMPANYNAME [COMPANYNAME ...]]
                    [-l LOCATIONS [LOCATIONS ...]] [-m] [-p] [-ys MINYEAR]
                    [-ye MAXYEAR] [-C] [-min MIN] [-max MAX] [-o OUTPUT]

A simple wordlist generator to generate a wordlist with years, company name,
months, periods

optional arguments:
  -h, --help                    show this help message and exit
  -c COMPANYNAME [COMPANYNAME ...], --companyname COMPANYNAME [COMPANYNAME ...]
                                used to supply a(or multiple) company name(s),
                                seperated by spaces, for the wordlist
  -l LOCATIONS [LOCATIONS ...], --locations LOCATIONS [LOCATIONS ...]
                                used to supply locations of the company, which will be
                                added to the wordlist
  -m, --months                  used to add all months of the year to the worldlist
  -p, --periods                 used to add all periods of the year to the worldlist,
                                like spring etc
  -ys MINYEAR, --minyear MINYEAR
                                used to supply the start year of the year range to be
                                appended to every word in the list
  -ye MAXYEAR, --maxyear MAXYEAR
                                used to supply the end year of the year range to be
                                appended to every word in the list
  -C, --capital                 used to capitalize every first letter in the word
  -min MIN, --min MIN           used to set the minimum password length
  -max MAX, --max MAX           used to set the maximum password length
  -o OUTPUT, --output OUTPUT
                                Directs the output to a name of your choice

### usage

Git clone https://github.com/Kadeeli/wordliper
python3 wordliper.py

## Authors

* **Jony Schats** - *Initial work* - [Kadeeli](https://github.com/Kadeeli)



