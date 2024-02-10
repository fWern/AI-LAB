# AI-LAB

## How to use Falcon 2.0 to link ORKG entities to a given text
1. Execute the functions get_entities and get_properties in dataset.ipynb. This will create corresponding json, which will then be used by Falcon as Knowledge Base.
2. Download Elasticsearch. I was using version 8.12.0 for windows. Go into the elasticsearch-8.12.0\bin and execute elasticsearch.bat.
3. Go into the folder where you saved the json for the entities and properties from ORKG and execute the two follwing commands:
    elasticdump  --output=http://localhost:9200/orkgentityindex/  --input=orkgentity.json  --type=data <br />
    elasticdump  --output=http://localhost:9200/orkgpropertyindex/  --input=orkgpropertyindex.json  --type=data <br />
    This will setup the Knowledge base.
4. In the main.py you can then enter a sentence in the main function to link ORKG entities to the text.
