"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMG_URL = 'https://tinyurl.com/demo-cupcake'

def connect_db(flask_app):
    db.app = flask_app
    db.init_app(flask_app)

class Cupcake(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default=DEFAULT_IMG_URL)


    def to_json(self):
        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image" : self.image
        }
    
    def update_from_json(self, json_obj):
        self.flavor = json_obj.get('flavor', self.flavor)
        self.size = json_obj.get('size', self.size)
        self.rating = json_obj.get('rating', self.rating)
        self.image = json_obj.get('image', self.image)