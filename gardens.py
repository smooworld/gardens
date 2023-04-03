# Import spacy
import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

# Define the list of garden path sentences
garden_path_sentences = ["The old man the boat.",
                         "The horse raced past the barn fell.",
                         "The tycoon sold the offshore oil tracts for a lot of money wanted to kill David",
                         "The sour drink from the ocean", "The cotton clothing is made of grows in Mississippi."
                         ]

for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print([(token, token.orth_, token.orth) for token in doc])
    print([(word, word.label_, word.label) for word in doc.ents])
    # The entity recognition doesn't find any words to label for these garden path sentences.
    print("")

# Explanation of an entity.
entity_fac = spacy.explain("FAC")
print(f"FAC:  {entity_fac}")


'''
Two entities found within the sentences:
1.  The entity recognition gave me "PERSON" for David which was expected.
2). The entity recognition gave me label 'GPE' which  assigned to geopolitical entities, i.e. countries, cities, states. 
    which is the Mississippi

I am able to read meaning to the entities except the last 3 digits
'''