from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

blue = Pet(name='Blue', species='dog', age=4, available=False, photo_url='https://media.istockphoto.com/id/1297706369/vector/sun-paint-brush-strokes-on-white-background-vector-illustration.jpg?s=612x612&w=0&k=20&c=BvQi1mWNRrgaEJ5_AhOfs7OuXiCRb91-JJUI93LlAHg=', notes="she loved to sun bath")

snowball = Pet(name='snowball', species='porcupine', age=1, available=False, notes="she pooped a lot")

gigi = Pet(name='gigi', species='cat', age=10, available=True, notes="she is very tall")

db.session.add(blue)
db.session.add(snowball)
db.session.add(gigi)

db.session.commit()