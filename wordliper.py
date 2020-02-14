#!/usr/bin/python3
#Writen by Jony Schats - Kadeeli - www.jonyschats.nl / https://github.com/Kadeeli
#Can probably be more efficient, but I can't code so it does its job :D
import argparse

##ARGUMENTS##
parser = argparse.ArgumentParser(description='A simple wordlist generator to generate worldlists including company name, locations, months, periods and appending years, capitalizing first letters. Basicly permutating the wordlist.')
parser.add_argument('-c', '--companyname', nargs='+', action='store', type=str, default=[], 
                    help='used to supply a(or multiple) company name(s), seperated by spaces, for the wordlist')
parser.add_argument('-l', '--locations', nargs='+', action='store', type=str, default=[],
                    help='used to supply locations of the company, which will be added to the wordlist')
parser.add_argument('-m', '--months', action='store_true', 
                    help='used to add all months of the year to the worldlist')
parser.add_argument('-p', '--periods', action='store_true',
                    help='used to add all periods of the year to the worldlist, like spring etc')
parser.add_argument('-ys', '--minyear', action='store', type=int, 
                    help='used to supply the start year of the year range to be appended to every word in the list')
parser.add_argument('-ye', '--maxyear', action='store', type=int,
                    help='used to supply the end year of the year range to be appended to every word in the list')
parser.add_argument('-C', '--capital', action='store_true', 
                    help='used to capitalize every first letter in the word')
parser.add_argument('-min', '--min', action='store', type=int,
                    help='used to set the minimum password length')
parser.add_argument('-max', '--max', action='store', type=int,
                    help='used to set the maximum password length')
parser.add_argument("-o", "--output", action='store', 
                    type=argparse.FileType('w'), dest='output',
                    help="Directs the output to a name of your choice")
args = parser.parse_args()

##VARIABLES, LISTS etc##
#List of dutch months used for the wordlist
months = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli',
          'augustus', 'september', 'october', 'november', 'december']
periods = ['lente', 'zomer', 'herfst', 'winter']
wordlist = []
newwordlist = []

##MAKING THE WORDLIST##
if args.months:
    print("[+] Adding months to the worldlist")
    wordlist.extend(months)

if args.months:
    print("[+] Adding periods to the worldlist")
    wordlist.extend(periods)

if args.companyname != []:
    print("[+] Adding company names to the worldlist")
    wordlist.extend(args.companyname)

if args.locations != []:
    print("[+] Adding locations to the worldlist")
    wordlist.extend(args.locations)

if args.minyear and args.maxyear:
    print("[+] Adding years to every word in the wordlist")
    for i in range(args.minyear, args.maxyear+1):
        yearwordlist = [x + str(i) for x in wordlist]
        newwordlist.extend(yearwordlist)
    wordlist.extend(newwordlist)

if args.capital:
    print("[+] Capitalizing the first letter of every word")
    newwordlist = [words.capitalize() for words in wordlist]
    wordlist.extend(newwordlist)

if args.min and args.max:
    print("[-] Deleting words if smaller then", args.min, "characters and larger then", args.max,"characters")
    for word in wordlist:
        if (len(word) < args.min) or (len(word) > args.max): wordlist.remove(word)

if args.output:
    output_file = args.output
    output_file.write('\n'.join(str(word) for word in wordlist))
else:
    print(*wordlist, sep = "\n") 
