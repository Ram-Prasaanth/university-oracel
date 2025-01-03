from pymongo.mongo_client import MongoClient

client = None
connetion_error_str: str = None
def connect_to_atlas_client():
    """ Establish connection between mongoDb Atlas cluster and return client on successfull connection 

    Returns:
        client: used to connect to database in MongoDB cluster
    """
    global client
    uri = "mongodb+srv://prasaanth2002:QPnIW6YvNsa2lAQC@cluster0.xl3rd.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)
        connetion_error_str = str(e)

#local_database
def get_client():
    """connect to local MongoDB database

    Returns:
        client: to establish connection with the mongoDB server in local machine
    """
    global client
    MONGO_URL = "mongodb://localhost:27017/"
    client = MongoClient(MONGO_URL)
    return client

def get_db(db_name='university-data'):
    client = connect_to_atlas_client()
    if client == None:
        print('Error Connecting')
        return None
    return client[db_name]

def get_collection(collection_name= "university-details"):
    db = get_db()
    if db == None:
        return None
    return db[collection_name]    

def connection_error()->dict:
    return {
        'code' : 500,
        'data' : f'Error while connecting to database : {connetion_error_str}'
    }
    

def insert_university_data(data):
    print("****************Insertion Data: ")
    print(data)
        
    collection = get_collection()
    try:
        if collection == None:
            return connection_error()
        result = collection.insert_one(data)
        return {
            'code' : 200,
            'data' : 'Inseted Successfully'
        }
        print('Success at insertion')
    except Exception as e:
        return {
            'code' : 500,
            'data' : f'Error while trying to insert - {str(e)}'
        }
    finally:
        client.close()
        
def get_university_data(find_values, sort_values={}):
    print("*******Find-Values: ",find_values)
    print("*******Sort-Values: ", sort_values)
    collection = get_collection()
    try:
        if collection == None:
            return connection_error()
        query_result  = collection.find(find_values)

        if len(sort_values) !=0:
            print("Sort Query")
            query_result = query_result.sort(sort_values)
            
        data = list(query_result)
        print('Data got from DB: ', data)
        return { 
            'code': 200, 
            'data' : data
        }
    except Exception as e:
        print("Error in get_university_data function while fetching ")
        print(data)
        return {
            'code' : 500,
            'data' : f'Error while trying to find the data - {str(e)} '
        }
    finally:
        client.close()
        
def update_university_data(selection_query, update_attributes):
    
    print("Selection Query: *********************")
    print(selection_query)
    print("Update Attributes: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(update_attributes)
    
    collection = get_collection()
    try:
        if collection == None:
            return connection_error()
        result = collection.update_one(selection_query, update=update_attributes)
        print(result)
        return{
            'code' : 200,
            'data' : 'Updated Succesfully'
        }
    except Exception as e:
        print("Error While updating the documents")
        return{
            'code' : 500,
            'data' : f'Error while trying to update - {str(e)} '
        }
    finally:
        client.close()
    
def delete_university_data_key(query: dict, delete_attributes: dict) -> dict:
    """ Delete a single or multiple keys from a single document 
    

    Args:
        query (): dict - {'University Name' : 'name'} selection query for selecting a document which need to be deleted
        delete_attributes (dict): {'$unset' : {'title' : '', ...} }the keys which need to be deleted

    Returns:
        dict: {'code' : 500, 'data ': str} 500 - error, 200 - success
    """
    collection = get_collection()
    
    print(f' {query = }')
    print(f' { delete_attributes = } ')
    
    try: 
        if collection == None:
            return connection_error()
        result = collection.update_one(query, delete_attributes)
        print("result from delete key in a document ",result)
        return {
            'code' : 200,
            'data' : 'Keys deleted successfully'
        }
    except Exception as e:
        return {
            'code' : 500,
            'data' : f'Error while deleting keys - str(e)'
        }
    finally:
        client.close()
    
    
def delete_university_data(query: dict):
    collection = get_collection()
    try: 
        if collection == None:
            return connection_error()
        result = collection.delete_one(query)
        print(result)
        return {
            'code' : 200,
            'data' : 'Deleted Successfully'
        }
    except Exception as e:
        return {
            'code' : 500,
            'data' : f'Error while deleting - str(e)'
        }
    finally:
        client.close()
        
def delete_university_documents():
    collection = get_collection()
    collection.delete_many({})
