from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



class Character(db.Model):
    __tablename__ = 'characters'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(15), nullable=False)
    eye_color = db.Column(db.String(20), nullable=False)
    birth_year = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
        }
    

class Planet(db.Model):
    __tablename__ = 'planets'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20), nullable=False)
    diameter = db.Column(db.String(15), nullable=False)
    population = db.Column(db.String(20), nullable=False)
    climate = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "population": self.population,
            "climate": self.climate,
        }
    

class Starship(db.Model):
    __tablename__ = 'starships'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20), nullable=False)
    model= db.Column(db.String(40), nullable=False)
    starship_class = db.Column(db.String(40), nullable=False)
    crew = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "starship class": self.starship_class,
            "crew": self.crew,
        }
    

class Favourite(db.Model):
    __tablename__ = 'favourites'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }