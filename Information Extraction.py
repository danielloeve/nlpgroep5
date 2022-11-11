# Package import
import lxml.etree as etree
from pathlib import Path
import json

# Lezen van bestand op root folder
doc = etree.parse(
    "Patientgegevens_Justin/Patient Registratie Formulier Justin.xml")

# Alle zoektermen in een list en dan doorheen loopen
zoektermen = ["Achternaam",
              "Voorletters",
              "Roepnaam",
              "Geboortedatum",
              "Geslacht",
              "Beroep",
              "Burgerlijke staat",
              "Straatnaam",
              "Huisnummer",
              "Postcode",
              "Woonplaats",
              "Telefoonnr.",
              "E-mail",
              "Naam zorgverzekeraar",
              "Verzekeringsnummer",
              "Verzekering begindatum",
              "Burger Service Nummer",
              "Naam huisarts"]

# Aanmaken van een dictionary
opgezochte_gegevens = {
}

# Door alle zoektermen gaan
# https://morioh.com/p/974654c40dbe
for zoekterm in zoektermen:

    # Zoeken van de onderwerpen
    # sr = doc.xpath(f"//P[contains(text(), '{zoekterm}')]")

    # Zoeken van de ingevulde gegevens met corresponderende zoekterm
    sr = doc.xpath(f"//TR[TH//P[contains(text(), '{zoekterm}')]]//TD//P")

    # Voor nu alle resultaten uitprinten op console line
    for elem in sr:
        opgezochte_gegevens[f"{zoekterm}"] = f"{elem.text}"

        # print(f"{zoekterm} \t\t" + elem.text)

# print(opgezochte_gegevens)

# Vervolg:
# Beslissen hoe we de verkregen data opslaan.
# Naam + geboortedatum bestandsnaam voor makkelijke administratie en dan de andere gegevens in het bestand

# Benodigde gegevens in variabelen zetten
voornaam = opgezochte_gegevens["Roepnaam"]
achternaam = opgezochte_gegevens["Achternaam"]
geboortedatum = opgezochte_gegevens["Geboortedatum"]

# Benodigde gegevens samenvoegen tot één + met bestandsoort
# https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
bestandnaam = f"{voornaam.strip()}_{achternaam.strip()}_{geboortedatum.strip()}"

# Aanmaken van de map en bestanden
bestand = Path(f"Patientgegevens_Extracted/{bestandnaam}/{bestandnaam}.json")
bestand.parent.mkdir(exist_ok=True, parents=True)

# Het schrijven van alle data
# https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/
bestand.write_text(json.dumps(opgezochte_gegevens, indent=10))
