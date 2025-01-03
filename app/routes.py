from app import app
from flask import render_template, request, url_for, redirect


from app.dataFilter import insert_university_details, get_query_results

from app.dataFilter import update_university_details, delete_university_details

from app.title_listOpeations import read_title_list, read_title_list_for_display


@app.route('/home')
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', home=True)

@app.route('/insert')
def insert():
    title_value = read_title_list()
    return render_template('insert.html', title_value=title_value, insert=True)

    #return render_template( 'index.html' , title_value=title_value)

@app.route('/submit', methods=['POST'])
def insert_details():
        # Receive form data
        university_name = request.form['university-name']
        titles = request.form.getlist('titles[]')
        values = request.form.getlist('values[]')
        
        print(titles)
        print(values)
        
        result = insert_university_details(university_name, titles, values)
        
        return render_template('redirect.html', message=result['data'], redirect_to='/')

        
        # Return a success message or render a template
        return 'Form Submitted Successfully'

       
        
@app.route('/search')
def search():
    titles = read_title_list_for_display()
    return render_template('search.html', title_list = titles, search=True)

@app.route('/results', methods=['POST'])
def search_results():
    search_titles = request.form.getlist('search_titles[]')
    search_values = request.form.getlist('search_values[]')
    
    sort_titles = request.form.getlist('sort_titles[]')
    sort_values = request.form.getlist('sort_values[]')
    
    print("Search Titles: ", search_titles," Search Values: ", search_values)
    print('sort Titles: ', sort_titles, ' Sort Values: ', sort_values)
    
    result = get_query_results(search_titles, search_values, sort_titles, sort_values)
    
    print("Code:  ", result['code'])
    print("Data: ", result['data'])
    
    if result['code'] == 200:
        return render_template('search_result.html', result = result['data'])
        
    return render_template('redirect.html', message=result['data'], redirect_to='/index')


@app.route('/update')
def update():
    titles = read_title_list_for_display()  
    return render_template('update.html', title_value=titles, update=True)
    
    

@app.route('/update-details', methods=['POST'])
def update_details():
    university_name = request.form.get('university-name')
    title: list[str] = request.form.getlist('titles[]')
    value: list[str] = request.form.getlist('values[]')
    
    result = update_university_details(university_name, title, value)    
    
    return render_template('redirect.html', message= result['data'], redirect_to='/update')

# serving the delete page
@app.route('/delete')
def delete():
    title_value = read_title_list()
    return render_template( 'delete.html', title_value=title_value ,delete=True)

# form data from delete page
@app.route('/delete-university', methods=['POST'])
def delete_details():
    university_name = request.form.get('university-name')
    delete_all = bool( request.form.get('delete-all') )
    titles: list = request.form.getlist('title[]')
    
    print(f' {university_name = }')
    print(f'{delete_all = }')
    print(f'{titles = }')
    result = delete_university_details(university_name, delete_all, titles)
    
    return render_template('redirect.html', message=result['data'], redirect_to='/delete')