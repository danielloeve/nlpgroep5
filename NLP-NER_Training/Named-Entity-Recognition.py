# Package import
import spacy

# Create blank NER model
nlp = spacy.blank("nl")
print("Created blank `Dutch language` model ")

ner = nlp.add_pipe("ner")

# Create cusotm labels/entities
# ner.add_label("date_of_birth_ner")

nlp.to_disk("Document_Reader_NER")
