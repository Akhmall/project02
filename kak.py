@app.route('/detail/<keyword>')
def detail(keyword):
    api_key = '3e0a68a9-2fdc-4b85-9e8e-64488a147c6d'
    url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{keyword}?key={api_key}'
    response = requests.get(url)
    definitions = response.json()

    if not definitions:
        return render_template('error.html', word=keyword)
    

    if isinstance(definitions[0], str):
        suggestions = definitions
        return render_template('error.html', word=keyword, suggestions=suggestions)


    status = request.args.get('status_give', 'new')
    return render_template(
        'detail.html',
        word=keyword,
        definitions=definitions,
        status=status
    )