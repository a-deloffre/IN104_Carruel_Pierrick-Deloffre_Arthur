import time
import sys
from whoosh.index import create_in, open_dir, exists_in


def create_index(save_index_folder, index_name, num_docs_index, lst_articlesIndex, schema, pool):
    t0 = time.time() 
    
    if not exists_in(save_index_folder, index_name): # if the index is not created yet
        print('*' * 10 + ' Building the index for {} documents '.format(num_docs_index) + '*' * 10)
        
        ix = create_in(save_index_folder, schema, index_name)  
        # Cette ligne retourne un index et prend en compte l'emplacement spécifié pour le construire
        
        writer = ix.writer(procs=6, multisegment=True, limitmb=4096)
        # On introduit writer, qui permet de modifier l'index en "écrivant" dessus
        # procs=6, limitmb=4GB## OR 8192

        for idx, path_name_file_index in enumerate(lst_articlesIndex[:num_docs_index]):
            if idx % 10000 == 0: 
                #Cette boucle sert à connaître l'avancée de la construction de l'index (nombre de documents traités)
                t1 = time.time()
                print("  {}/{}. elapsed time : {}s".format(idx, num_docs_index, round(t1 - t0, 3)));

            article_content = open(path_name_file_index)
            # On récupère le contenu du document associé à l'index
            text = article_content.read()
            writer.add_document(path=path_name_file_index, content=text)  
            # , time=modtime
            # On ajoute le document (sa localisation et son contenu) dans l'index
        writer.commit(merge=False)
        
        t1 = time.time()
        print('*' * 10 + ' Index built in {}s '.format(round(t1 - t0, 3)) + '*' * 10)  # It's CPU seconds elapsed (floating point)

    ix = open_dir(save_index_folder, index_name) 
    #On ouvre le dossier afin de pouvoir manipuler l'index créé

    return ix
