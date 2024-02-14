from main import link_entity_to_text

# input query for Falcon 2.0, you can change this to use it for other queries
QUERY = "this is a sample text for the example to add an entity, in this case machine learning, to an text."

# output of the function are the found entities and the text linked with entities
entities, text_linked = link_entity_to_text(QUERY)

print(f"Input to Falcon 2.0: \n{QUERY}\n")

# (first position in entry is ORKG entity, second position is part of text, for which the entity was found
print(f"Entities found for the QUERY : \n{entities}\n")

print(f"Output text with linked entities: \n{text_linked}")