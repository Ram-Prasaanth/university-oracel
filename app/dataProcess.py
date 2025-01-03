from app.title_listOpeations import add_not_existing_title_to_title_list



def process_title(title: str)->str:
    """return a string with extra spaces on both ends trimmed and the title-cased 

    Args:
        title (str): str input 

    Returns:
        str: string with extra soaces trimmed and title cased
    """
    return title.strip().title()  

def process_value(value: str) -> str:
    """remove the extra space in both sides of the input passed"""
    return value.strip()

def process_document_for_insert(titles: list[str], values: list[str], university_name: str=None) -> dict:
    """preare the data for inserting in form of dictionary 
    {
        'University' : university_name,
        title : value
        ..
    }    
    Args:
        university_name (str): university name for inserting
        titles (list[str]): title values given by user for inserting
        values (list[str]): values for the titles given by user for inserting

    Returns:
        _dict_: {str : list[str] }
    """
    document = {}
    if university_name != None:
        document['University'] = university_name
    print('At processing documents')
    for title, value in zip(titles, values):
        print(f'{title = } ----- { value = }')
        if len(title) !=0 and len(value) != 0:
            print('inside if block')
            title = process_title(title)
            # add title  
            add_not_existing_title_to_title_list(title)       
            value = process_value(value)
            document[title] = value
    
    return document



def process_search_titles_values(search_titles, search_values) -> dict:
    """
    Combines search_titles with search_values to form a dictionary.
    If 'All' is in search_titles, returns an empty dictionary to retrieve all documents.

    Args:
        search_titles (list): List of search titles.
        search_values (list): List of search values corresponding to search_titles.

    Returns:
        dict: Dictionary of search attributes.
    """

    # Early return for the 'All' condition
    if "All" in search_titles:
        return {}

    # Initialize an empty dictionary to store search attributes
    search_attributes = {}

    # Iterate over title-value pairs using zip
    for title, value in zip(search_titles, search_values):
        # Process title and value
        processed_title = process_title(title)
        processed_value = process_value(value)

        # Use setdefault to simplify the logic for initializing and appending to the list
        search_attributes.setdefault(processed_title, {'$in': []}).get('$in').append(processed_value)

    return search_attributes



def process_sort_titles_values(sort_titles: list[str], sort_values: list[str]) -> dict:
    """return a dict which of sort_tiles with its corresponding sort_values_

    Args:
        sort_titles (list[str]): _description_
        sort_values (list[str]): _description_

    Returns:
        dict: _description_
    """
    sort_attributes = {}
    for title, value in zip(sort_titles, sort_values):
        title = process_title(title)
        sort_attributes[title] = int(value)
    return sort_attributes


def process_document_delete(titles: list[str]) -> dict:
    """ process the titles list to from a dict with title as key and value as empty string

    Args:
        titles (list[str]): title list 

    Returns:
        dict: dict {'$unset' : {'title' : ''}}
    """
    document = {}
    for title in titles:
        document[title] = ''
    return { '$unset' : document }
    


def process_documents_display(documents: dict) -> __dict__:
    sorted_documents = []
    for document in documents:
        document.pop('_id')
        university_name = document['University']  
              
        sorted_document = { 'University' : university_name}
        
        sorted_document.update( dict( sorted(document.items()) ) )
        
        sorted_documents.append(sorted_document)
        
    return sorted_documents