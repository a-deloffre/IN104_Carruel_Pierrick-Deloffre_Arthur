import os.path

from whoosh.fields import Schema, TEXT
from whoosh.analysis import *
from whoosh import qparser
from whoosh.qparser import QueryParser
import time
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import argparse
import glob

from index import create_index
from query import Query


def main():
    print('début')
    path_read_docs_index = 'D:/Documents/ENSTA/Matières/IN/IN104/new/'
    path_save_index_folder = 'D:/Documents/ENSTA/Matières/IN/IN104/index/'
    index_name = "index_IN104"
    num_docs_index = 1500
    number_docs_result_search = 5

    lst_index_docs = glob.glob(path_read_docs_index + '*.txt')
    
    pool = Pool(8)
    schema = Schema(path=TEXT(stored=True), content=TEXT(analyzer=StemmingAnalyzer()))
    ix = create_index(path_save_index_folder, index_name, num_docs_index, lst_index_docs, schema, pool)
    searcher = ix.searcher()
    parser_query = QueryParser("content", schema=schema, group=qparser.OrGroup)
    
    user_query = "viruses"
    # Object
    query = Query(user_query)
    docs_result = query.get_query(parser_query, searcher, number_docs_result_search)
    
    print(docs_result)
    for doc in docs_result:
        print('boucle')
        print(doc)
    print('fin boucle')

if __name__ == "__main__":
    main()
