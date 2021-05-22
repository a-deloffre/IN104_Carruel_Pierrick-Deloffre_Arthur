
class Query:

    def __init__(self, query):
        self.query = query

    def get_query(self, parser, searcher, number_docs_result_search):
        my_query = parser.parse(self.query) # sépare la recherche (suite de mots) en plusieurs "résultats"
        results = searcher.search(my_query, limit=number_docs_result_search) 
        # recherche de la requête "parsée" dans nos articles, avec une limite de résultats à afficher
        docs = []
        for x in list(results):
            doc_name = x['path'] #On récupère la localisation de chaque article correspondant à la requête
            docs.append(doc_name)
        return docs
