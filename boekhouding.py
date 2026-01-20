import csv
from helper import *
from presentatie import *

Boekhouding = {
"Aardbeien-ijs-totaal": 1000,
"Vanille-ijs-totaal": 2000,
"Chocolade-ijs-totaal": 1500,
"Waterijsjes-totaal": 750
}

totaal_inkomsten = som(Boekhouding.values())

presenteer(Boekhouding, totaal_inkomsten)

''' 
ik krijg dit alleen werkend als ik een # in presentatie.py voor presenteer() zet. 
Ben erg benieuwd hoe het anders of eenvoudiger kan
'''

with open('boekhouding.csv', 'w',newline='') as csvfile:     
      for key, value in inkomsten.items():     
      writer = csv.writer(csvfile, delimiter=';')     
      writer.writerow([key,value])