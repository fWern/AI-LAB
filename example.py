from main import link_entity_to_text

# input query for Falcon 2.0, you can change this to use it for other queries
QUERY = "this is a sample text for the example to add an entity, in this case machine learning, to an text."

# output of the function are the found entities and the text linked with entities
# (first position in entry is ORKG entity, second position is part of text, for which the entity was found
entities, text_linked = link_entity_to_text(QUERY)
#Entities found for the QUERY :
#[
# ['http://orkg.org/orkg/resource/R4322', 'entity, in this case machine learning, to an text'],
# ['http://orkg.org/orkg/resource/R4647', 'sample text for the example']
#]

print(f"Input to Falcon 2.0: \n{QUERY}\n")
print(f"Entities found for the QUERY : \n{entities}\n")
# Output text with linked entities:
# this is a \uri{http://orkg.org/orkg/resource/R4647}{sample text for the example} to add an \uri{http://orkg.org/orkg/resource/R4322}{entity, in this case machine learning, to an text}.
print(f"Output text with linked entities: \n{text_linked}")