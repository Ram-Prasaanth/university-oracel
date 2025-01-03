import json


# add title to title_list.json is not present
def add_not_existing_title_to_title_list(title: str)-> None:
    "Function Running for adding titles"
    titles_stored = read_title_list()
    if len(title) !=0  and title != 'University' and title not in titles_stored:
        titles_stored.append(title)
    write_title_list(titles_stored)   
    
    
    
def read_title_list_for_display():
    data = ['University',]
    data = data + read_title_list()
  
    return data


        
def read_title_list():    
    data = []
    with open('./title_list.json','r') as titles:
        try:
            data = json.load(titles)
        except:
            return []
    return data
        
        
def write_title_list(data):
    with open('./title_list.json','w') as titles:
        json.dump(data, titles)
    return 'Success'
