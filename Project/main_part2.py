from whoosh.fields import Schema, TEXT
from whoosh.analysis import *
from whoosh import qparser
from whoosh.qparser import QueryParser
import time
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import argparse
import glob
from whoosh.index import create_in, open_dir, exists_in
import time
import sys
from query import Query
from index import create_index

def main():

    path_read_docs_index = 'C:/Users/Arthur/newdocs/' #localisation des articles résumés
    path_save_index_folder = 'C:/Users/Arthur/index/' #localisaton de l'index (à supprimer avant chaque mise en route)
    index_name = "index_IN104"
    
    num_docs_index = 17 #Nombre de documents où la recherche sera effectuée
    
    number_docs_result_search = 10 #nombre maximum de documents contenant la requête qui seront affichés

    lst_index_docs = glob.glob(path_read_docs_index + '*.txt') #On récupère la liste des localisations des articles modifiés
    
    for i in range(len(lst_index_docs)) :
        lst_index_docs[i] = lst_index_docs[i][:23] + '/' + lst_index_docs[i][24:]
        #Problème lorsque l'on affiche leur localisation, un \\ apparaît : on le remplace par /
    
    pool = Pool(8)
    schema = Schema(path=TEXT(stored=True), content=TEXT(analyzer=StemmingAnalyzer()))
    #On instaure le schéma
    ix = create_index(path_save_index_folder, index_name, num_docs_index, lst_index_docs, schema, pool)
    #On crée le nouvel index
    searcher = ix.searcher()
    parser_query = QueryParser("content", schema=schema, group=qparser.OrGroup)
    
    
    user_query = "number of case" #On insère notre requête ici
    
    query = Query(user_query)
    docs_result = query.get_query(parser_query, searcher, number_docs_result_search)
    #On utilise la fonction get_query, qui retourne la localisation de chaque article correspondant à la requête sous forme de liste
    for doc in docs_result:
        print(doc) #Affichage des résultats


if __name__ == "__main__":
    main()
