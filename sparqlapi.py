from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph

sparql = SPARQLWrapper("http://localhost:7200/repositories/001apart")


def byName(name):
    query="""
            PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>
            PREFIX dbpedia: <http://dbpedia.org/resource/>
            PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?apartment  WHERE {{ 
                apartment a  swp:Apartment  ;
                FILTER regex(str(?apartment), "{name}").
            }}
        """.format(name=name)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def bySameBedroom(bedroomCount):
    query="""
        PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>
        PREFIX dbpedia: <http://dbpedia.org/resource/>
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?apartment 
        WHERE {{
        ?apartment swp:hasNumberOfBedrooms {bedroomCount}.
        }}
        ORDER BY DESC(?bedrooms)
    """.format(bedroomCount=bedroomCount)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def byBedroom(bedroomCount):
    query="""
        PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>
        PREFIX dbpedia: <http://dbpedia.org/resource/>
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?apartment ?bedrooms
        WHERE {{
        ?apartment swp:hasNumberOfBedrooms ?bedrooms.
        FILTER (?bedrooms > {bedroomCount}).
        }}
        ORDER BY DESC(?bedrooms)
    """.format(bedroomCount=bedroomCount)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def byLocation(location):
    query="""
            PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>
            PREFIX dbpedia: <http://dbpedia.org/resource/>
            PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?apartment  WHERE {{ 
                ?apartment dbpedia-owl:location|dbpedia-owl:locationCity dbpedia:{location}.    
            }}
        """.format(location=location)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def searchByAddress(address):
    query="""
            PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>
            PREFIX dbpedia: <http://dbpedia.org/resource/>
            PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?apartment ?address WHERE {{ 
                ?apartment swp:address ?address. 
                FILTER regex(str(?apartment), "{address}").    
            }}
        """.format(address=address)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

    
# for result in results['results']['bindings']:
#     print(result['bedrooms']['value'])
#     print(result['apartment']['value'])
