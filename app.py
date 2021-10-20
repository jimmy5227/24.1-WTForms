from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'HelloWorld'

connect_db(app)


@app.route('/')
def index():
    listed_pets = Pet.query.all()
    return render_template('index.html', listed_pets=listed_pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=pet_name, species=species,
                      photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'New pet {pet_name} added successfully!')
        return redirect('/')
    else:
        return render_template('add.html', form=form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def pet(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm()
    # availability = db.session.query(Pet.available)
    # form.availability.choices = availability
    # form(pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.availability.data

        if photo_url != '':
            pet.photo_url = photo_url
        if notes != '':
            pet.notes = notes
        if available == 'True':
            pet.available = True
        else:
            pet.available = False

        db.session.add(pet)
        db.session.commit()

        flash(f'Pet edited successfully!')
        return redirect('/')

    return render_template('pet.html', pet=pet, form=form)

# @app.route('/users')
# def Users():
#     listed_users_with_link = users.query.all()
#     return render_template('users.html', listed_users_with_link=listed_users_with_link)

# @app.route('/users/new', methods=['POST'])
# def UsersNewPost():
#     firstname = request.form['firstname']
#     lastname = request.form['lastname']
#     imageurl = request.form['imageurl']
#     if imageurl == '':
#         imageurl = default

#     new_user = users(first_name=firstname,
#                      last_name=lastname, image_url=imageurl)
#     db.session.add(new_user)
#     db.session.commit()

#     return redirect('/users')
#     # return redirect(f'/{new_user.id}')


# @app.route('/users/<int:users_id>/delete', methods=["POST"])
# def delete(users_id):

#     user = users.query.get_or_404(users_id)
#     db.session.delete(user)
#     db.session.commit()

#     return redirect("/")
