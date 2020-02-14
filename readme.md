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

**EXAMPLE**
<addr>sudo ./wordliper.py --company kadeeli --locations netherlands --months --capital --periods --minyear 2019 --maxyear 2020 --min 8 --max 20 -o wordlist.txt</addr>

### usage

Git clone https://github.com/Kadeeli/wordliper
python3 wordliper.py

## Authors

* **Jony Schats** - *Initial work* - [Kadeeli](https://github.com/Kadeeli)



