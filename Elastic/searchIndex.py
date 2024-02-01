from elasticsearch import Elasticsearch
import editdistance


es = Elasticsearch(['http://localhost:9200'])
docType = "doc"



def entitySearch(query):
    indexName = "orkgentityindex"
    results=[]
    ###################################################
    elasticResults=es.search(index=indexName, body={
              "query": {
                "match" : { "label" : query } 
              }
               ,"size":100
    }
           )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["label"].lower().replace('.','').strip()==query.lower().strip():
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*50,40])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*40,0])

    ###################################################
    elasticResults=es.search(index=indexName, body={
    "query": {
        "match" : {
            "label" : {
                "query" : query,
                "fuzziness": "AUTO"
                
            }
        }
    },"size":100
            }
           )
    for result in elasticResults['hits']['hits']:
        edit_distance=editdistance.eval(result["_source"]["label"].lower().replace('.','').strip(), query.lower().strip())
        if edit_distance<=1:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*50,30])
        else:
            results.append([result["_source"]["label"],result["_source"]["uri"],result["_score"]*25,0])

    #results= sorted(results, key = lambda x: (int(x[1][x[1].rfind("/")+2:-1]),-x[3],-x[2]))
    results = sorted(results, key=lambda x: (
        int(x[1][x[1].rfind("/") + 2:-1]) if x[1][x[1].rfind("/") + 2:-1].isdigit() else float('-inf'),
        -x[3],
        -x[2]
    ))
    seen = set()
    results = [x for x in results if x[1] not in seen and not seen.add(x[1])]
    results=results[:20]
    #results= sorted(results, key = lambda x: (-x[3],int(x[1][x[1].rfind("/")+2:-1])))
    results = sorted(results, key=lambda x: (-x[3],
                     int(x[1][x[1].rfind("/") + 2:-1]) if x[1][x[1].rfind("/") + 2:-1].isdigit() else float('-inf')))
    return results[:15]
    #for result in results['hits']['hits']:
        #print (result["_score"])
        #print (result["_source"])
        #print("-----------")
        
def propertySearch(query):
    indexName = "orkgpropertyindex"
    results = []
    ###################################################
    elasticResults = es.search(index=indexName, body={
        "query": {
            "match": {"label": query}
        }
        , "size": 100
    }
                               )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["label"].lower().replace('.','').strip()==query.lower().strip():
            results.append([result["_source"]["label"], result["_source"]["uri"], result["_score"] * 50, 40])
        else:
            results.append([result["_source"]["label"], result["_source"]["uri"], result["_score"] * 40, 0])

    ###################################################
    elasticResults=es.search(index=indexName, body={
    "query": {
        "match" : {
            "label" : {
                "query" : query,
                "fuzziness": "AUTO"
                
            }
        }
    },"size":100
            }
           )
    for result in elasticResults['hits']['hits']:
        edit_distance=editdistance.eval(result["_source"]["label"].lower().replace('.','').strip(), query.lower().strip())
        if edit_distance<=1:
            results.append([result["_source"]["label"], result["_source"]["uri"], result["_score"] * 50, 40])
        else:
            results.append([result["_source"]["label"], result["_source"]["uri"], result["_score"] * 25, 0])

    #results= sorted(results, key = lambda x: (int(x[1][x[1].rfind("/")+2:-1]),-x[3],-x[2]))
    results = sorted(results, key=lambda x: (
        int(x[1][x[1].rfind("/") + 2:-1]) if x[1][x[1].rfind("/") + 2:-1].isdigit() else float('-inf'),
        -x[3],
        -x[2]
    ))
    seen = set()
    results = [x for x in results if x[1] not in seen and not seen.add(x[1])]
    results=results[:20]
    results= sorted(results, key = lambda x: (-x[3],int(x[1][x[1].rfind("/")+2:-1]) if x[1][x[1].rfind("/") + 2:-1].isdigit() else 0))
    return results[:15]

def propertySearchExactmatch(query):
    indexName = "orkgpropertyindex"
    ###################################################
    elasticResults = es.search(index=indexName, body={
        "query": {
            "match": {"label": query}
        }
    }
                               )
    for result in elasticResults['hits']['hits']:
        if result["_source"]["label"].lower().replace('.','').strip()==query.lower().strip():
            return True


    return False

