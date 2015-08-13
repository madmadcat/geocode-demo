import csv
import sys

data = [
    ("And Now For Something Completely Different", 1971, "Ian MacNaughton"),
    ("Monty Python And The Holy Grail", 1975, "Terry Gilliam, Terry Jones"),
    ("Monty Python's Life Of Brian", 1979, "Terry Jones"),
    ("Monty Python Live At The Hollywood Bowl", 1982, "Terry Hughes"),
    ("Monty Python's The Meaning Of Life", 1983, "Terry Jones")
]

writer = csv.writer(sys.stdout)

for item in data:
    writer.writerow(item)
