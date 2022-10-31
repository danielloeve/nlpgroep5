# Package import
import lxml.etree as etree

# Lezen van bestand op root folder
doc = etree.parse(
    "Patientgegevens Justin/Patient Registratie Formulier Justin.xml")

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

# Door alle zoektermen gaan
# https://morioh.com/p/974654c40dbe
for zoekterm in zoektermen:

    # Zoeken van de onderwerpen
    # sr = doc.xpath(f"//P[contains(text(), '{zoekterm}')]")

    # Zoeken van de ingevulde gegevens met corresponderende zoekterm
    sr = doc.xpath(f"//TR[TH//P[contains(text(), '{zoekterm}')]]//TD//P")

    # Voor nu alle resultaten uitprinten op console line
    for elem in sr:
        print(f"{zoekterm} \t\t" + elem.text)

# Vervolg:
# Beslissen hoe we de verkregen data opslaan.
