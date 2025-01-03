import json
from app.dbOperation import insert_university_data, get_university_data, update_university_data, delete_university_data, delete_university_data_key

from app.dataProcess import process_title, process_document_for_insert, process_search_titles_values, process_sort_titles_values, process_documents_display
from app.dataProcess import process_document_delete, process_value

def is_university_present(university_name: str)-> int:
    """check if the university is already exist in database 
        -1 - error while checking (database error)
         0 - university does not exist
         1 - university exist
       

    Args:
        university_name (str): university name 

    Returns:
        int: integer value depending on university exist or not
    """
    university_name = process_value(university_name)
    result = get_university_data({'University' : university_name})
    if result['code'] == 500:
        return -1
    data = result['data']
    if len(data) == 0:
        # no university exist
        return 0
    # the university name alreay exist
    return 1

def insert_university_details(university_name, title_names, values):
       
    flag = is_university_present(university_name)
    if flag == 1:
        return {
            'code' : 1,
            'data' : 'University Already Exist'
        }
    elif flag == -1:
        return {
            'code' : -1,
            'data' : 'Error While Checking if university already exists'
        }
        
    # process the document fro insertion
    document = process_document_for_insert(title_names, values, university_name)
    
    
    result = insert_university_data(document)
    # add code for error at insertion
    return result
    

    
    
def fetch_query_and_process(search_attributes, sort_attributes):
    
    query_result = get_university_data(search_attributes, sort_attributes)
    
    if query_result['code'] == 500:
        return query_result
    
    documents = query_result['data']
    if len(documents) == 0:
        return {
            'code' : 0,
            'data' : 'No University Found'
        }
    
    # removing the '_id' and sorting the documents 
    sorted_documents = process_documents_display(documents)
        
    return {
        'code' : 200,
        'data' : sorted_documents
    }

        
# get input for data retrival and send theresult based on the input param    
def get_query_results(search_titles, search_values, sort_titles, sort_values):
    
    search_attributes = process_search_titles_values(search_titles, search_values)
    sort_attributes = process_sort_titles_values(sort_titles, sort_values)       
    
    query_result = fetch_query_and_process(search_attributes, sort_attributes)
    return query_result

#update the university details
def update_university_details(university_name, title: list[str], value: list[str]):
    selection_query = {'University' : university_name}
    flag = is_university_present(university_name)
    if flag == -1:
        return {
            'code': -1,
            'data' : 'Error while checking university already exist'
        }
    elif flag == 0:
        return {
            'code' : 0,
            'data' : 'University Does Not Exist'
        }
    document: dict = process_document_for_insert(title, value)
    update_university_name = document.get('University')
    if update_university_name != None:
        falg = is_university_present(update_university_name)
        if flag == 1:
            return {
                'code' : 1,
                'data' : f' The University Name "{update_university_name}" you provide already exist in DataBase, So Please provide a another name '
            }
            
    update_attributes = {
        '$set' : document
    }
    
    result = update_university_data(selection_query, update_attributes)
    return result
    
# delete university details
def delete_university_details(university_name: str, delete_all: bool, titles: list[str]) ->dict:
    
    flag: int = is_university_present(university_name)
    
    if flag == 0:
        return {
            'code' : 0,
            'data' : f'The University "{university_name}" does not exist'
        }
    query = {'University' : university_name}
    if delete_all:
        print("Delete the whole document")        
        return delete_university_data(query)
            
    delete_attributes: dict = process_document_delete(titles)
    return  delete_university_data_key(query, delete_attributes)
