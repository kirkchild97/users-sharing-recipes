from flask_app import app
from flask import session, request, redirect, render_template
from flask_app.models.recipe import Recipe


@app.route('/userDashboard/<user_id>/<recipe_id>')
def view_recipe(user_id, recipe_id):
    data = {'id' : recipe_id}
    recipe_info = Recipe.get_recipes(data)
    return render_template('recipeinfo.html', recipe = recipe_info)

@app.route('/userDashboard/<user_id>/<recipe_id>/edit')
def edit_recipe(user_id, recipe_id):
    data = {'id' : recipe_id}
    recipe_info = Recipe.get_recipes(data)
    return render_template('editrecipe.html', recipe = recipe_info)

@app.route('/userDashboard/<user_id>/<recipe_id>/edit/commit', methods=['POST'])
def commit_recipe_changes(user_id, recipe_id):
    data = {
        'name' : request.form['recipe_name'],
        'description' : request.form['description'],
        'under_30' : request.form['under_30'],
        'instructions' : request.form['instructions'],
        'date_recipe_made' : request.form['date_made'],
        'id' : recipe_id
    }
    if Recipe.validate_recipe_input(data):
        Recipe.edit_recipe(data)
        return redirect('/userDashboard/' + user_id)
    else:
        return redirect('/userDashboard/' + user_id + '/' + recipe_id + '/edit')

@app.route('/userDashboard/<user_id>/<recipe_id>/delete')
def delete_recipe(user_id, recipe_id):
    data = {'id' : recipe_id}
    Recipe.delete_recipe(data)
    return redirect('/userDashboard/' + user_id)

@app.route('/userDashboard/<user_id>/newRecipe')
def new_recipe(user_id):
    return render_template('editrecipe.html', recipe = False)

@app.route('/userDashboard/<user_id>/newRecipe/create', methods=['POST'])
def save_recipe(user_id):
    data = {
        'name' : request.form['recipe_name'],
        'description' : request.form['description'],
        'under_30' : request.form['under_30'],
        'instructions' : request.form['instructions'],
        'date_recipe_made' : request.form['date_made'],
        'user_id' : user_id
    }
    if Recipe.validate_recipe_input(data):
        Recipe.save_recipe(data)
        return redirect('/userDashboard/' + user_id)
    else:
        return redirect('/userDashboard/' + user_id + '/newRecipe')