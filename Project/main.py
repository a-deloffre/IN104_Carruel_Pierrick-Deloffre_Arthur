import json
import glob
import sys

from extract_data import ExtractData
from preprocess_data import PreprocessData
from utils import read_json
from utils import write_file

if __name__ == '__main__':
    path_documents = 'D:/Documents/ENSTA/Matières/IN/IN104/pmc_json/'
    list_documents = glob.glob(path_documents + '*.xml.json')
    path_new_doc='D:/Documents/ENSTA/Matières/IN/IN104/new/'

    # Path of each document
    for path_doc in list_documents:
        # Load json
        data = read_json(path_doc)
        # object
        obj_data = ExtractData(data)
        # call get_paper_id method
        paper_id=obj_data.get_paper_id()
        #print(paper_id)
        
        # call get_title method
        title=obj_data.get_title()
       # print(title)
        
        # call get_text method
        text=obj_data.get_text()
       # print(text)

        # Object to pre-process the text
        obj_preprocess = PreprocessData(text)
        # Convert the text to lower case
        
        new_text=obj_preprocess.convert_lowercase()

        # Remove punctuation, number , stop words, special characters
        new_text=obj_preprocess.remove_all(new_text)

        # Remove numbers
       # new_text=obj_preprocess.remove_number(new_text)

        # Remove stop words
        #new_text=obj_preprocess.remove_stop_words(new_text)

        # Remove the special characters
       # new_text=obj_preprocess.remove_special_character(new_text)

        # Lemmatization
        new_text=obj_preprocess.lemmatization_text(new_text)
       # print (new_text)
        # Write the documents
       # print("fini" + '\n')
        write_file(path_new_doc,new_text, paper_id)


