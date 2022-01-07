from flask_app import app
from flask import session, request, redirect, flash, render_template
from flask_app.models.recipe import Recipe


@app.route('/userDashboard/<user_id>/<recipe_id>')
def view_recipe(user_id, recipe_id):
    return render_template('recipeinfo.html')

@app.route('/userDashboard/<user_id>/<recipe_id>/edit')
def edit_recipe(user_id, recipe_id):
    return render_template('editrecipe.html')

@app.route('/userDashboard/<user_id>/<recipe_id>/delete')
def delete_recipe(user_id, recipe_id):
    return redirect('/userDashboard/',user_id)

@app.route('/userDashboard/<user_id>/newRecipe')
def new_recipe(user_id):
    return render_template('editrecipe.html')