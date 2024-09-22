#!/usr/bin/env python3

import csv
import sys

map = {
  "Amy Imai Elementary": {
    "Grass 7v7": "Imai Sm",
    "Grass 9v9": "Imai Lg",
  },
  "Bubb Elementary": {
     "Grass (9v9)": "Bubb",
  },
  "Christa McAuliffe Elementary School": {
    "Field": "McAuliffe",
  },
  "Congress Springs Park": {
    "CSP 7v7 #1": "Congress 1",
  },
  "Del Monte Park": {
    "Field 1A 9v9": "Del Monte 1A",
    "Field 1B 9v9": "Del Monte 1B",
  },
  "Eaton Elementary": {
    "": "Eaton",
    "Grass": "Eaton",
  },
  "Greer Park Sports Complex": {
    "Field 2": "Greer 2",
    "Field 5": "Greer 5",
  },
  "Kennedy Middle School": {
    "Hyannisport": "Kennedy",
  },
  "Lincoln Elementary": {
    "1A": "Lincoln 1A",
    "1B": "Lincoln 1B",
  },
  "Manzanita Park": {
    "Soccer Field #1": "Manzanita",
  },
  "Miller Middle School": {
    "West": "Miller",
  },
  "Panama Park": {
    "U10": "Panana",
  },
  "Peers Park": {
    "10U": "Peers",
  },
  "Reed & Grant Sports Park": {
    "Field 3 (9v9)": "Reed/Grant",
  },
  "San Antonio Park - Sunnyvale": {
    "U14": "San Antonio",
  },
  "Seale Park": {
    "10U (7v7)": "Seale",
  },
  "Sheppard MS": {
    "Field #1": "Sheppard",
  },
  "Shoreline Athletic Fields": {
    "Shoreline North": "Shoreline N",
    "Shoreline South": "Shoreline S",
  },
  "Springer Elementary": {
    "Springer East": "Springer E",
    "Springer West": "Springer W",
  },
  "STEVENS CREEK ELEMENTARY": {
    "A (along Varian Way)": "Stevens Creek",
  },
  "Sunnyvale Middle School": {
    "Track Field": "Sunnyvale MS",
  },
  "Watson Park": {
    "12U North": "Watson N",
    "12U South": "Watson S",
    "Grass 1": "Watson 1",
    "Grass 2": "Watson 2",
    "Soccer Field 1A": "Watson 1A",
    "Soccer Field 1B": "Watson 1B",
  },
  "Wilson Park": {
    "Cupertino Field 1": "Wilson",
  },
}

seen = {}
for row in csv.reader(sys.stdin):
  if row[0] == "GameID": continue
  if not row[9].startswith("R45-") and not row[10].startswith("R45-"): continue

  name = map.get(row[4], {}).get(row[5])
  if name is None:
    print(f"Missing mapping for: {row[4]}, {row[5]}")
    exit(1)

  tt1 = row[2].split(' ')
  tt2 = tt1[0].split(':')
  hr = int(tt2[0])
  if hr < 12 and tt1[1] == 'PM': hr += 12
  tt = (10 + hr) * 100 + int(tt2[1])
  
  # We want to print local R45 fields first
  if name in ("Bubb", "Imai Lg", "Imai Sm", "Shoreline N", "Shoreline S",
              "Springer E", "Springer W"):
    local = 1
  else:
    local = 2

  key = f'{local}: {name}: {tt}'
  row[0] = name
  row[2] = row[2].replace(" ", "")
  while len(row) < 18:
    row.append("")
  seen[key] = row

print(f"Site,Time,Age,CR,AR1,AR2")
for key in sorted(seen.keys()):
  row = seen[key]
  print(f"{row[0]},{row[2]},{row[8]},{row[11]},{row[14]},{row[17]}")
