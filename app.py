from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
app.app_context().push()
# db.drop_all()
# db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_pet_list():
    ''' Shows a list of all pets '''
    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    ''' Shows and handles add pet form '''
    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        img = form.img.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=img, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect ('/')
    
    else:
        return render_template('/add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_details(pet_id):
    ''' Shows pet's details and edit form '''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    print(form.data)
    if form.validate_on_submit():
        pet.photo_url = form.img.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(request.url)
    
    else:
        return render_template('pet_details.html', form=form, pet=pet)



