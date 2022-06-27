from .. import db

# recipe_ingredient = db.Table('recipe_ingredient',
#                              db.Column('Recipe_id', db.Integer, db.ForeignKey('Recipe.id'), primary_key=True),
#                              db.Column('igd_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
#                              )


# tags = db.Table('tags',
#     db.Column('Recipe_id', db.Integer, db.ForeignKey('Recipe.id'), primary_key=True),
#     db.Column('igd_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
# )
class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    R_name = db.Column(db.String(80), nullable=True)
    R_description = db.Column(db.String(240), nullable=True)
    R_category = db.Column(db.String(120), nullable=True)
    R_calorie = db.Column(db.Integer, nullable=True)
    R_img_url = db.Column(db.BLOB)


    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # recipe_ingredient = db.relationship('recipe_ingredient', secondary=recipe_ingredient, lazy='subquery',
    #                        backref=db.backref('recipe', lazy=True))

    def __init__(self, R_name, user_id, R_description=None, R_category=None, R_calorie=0, R_img_url=None):
        self.R_name = R_name
        self.R_description = R_description
        self.R_category = R_category
        self.R_calorie = R_calorie
        self.user_id = user_id
        self.R_img_url=R_img_url

    def __repr__(self):
        return '<Recipe %r>' % self.R_name


class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    igd_name = db.Column(db.String(80), unique=True, nullable=False)
    igd_category = db.Column(db.String(120), nullable=True)
    igd_opponent = db.Column(db.String(80))

    igb_description = db.Column(db.String(240), nullable=True)
    igd_calorie = db.Column(db.Integer, nullable=True)
    igd_img_url = db.Column(db.String(50))

    def __init__(self, igd_name, igd_category=None,igd_opponent=None, igb_description=None, igd_calorie=0, igd_img_url=None):
        self.igd_name = igd_name
        self.igd_category=igd_category
        self.igd_opponent = igd_opponent
        self.igb_description = igb_description
        self.igd_calorie = igd_calorie
        self.igd_img_url =igd_img_url

    def __repr__(self):
        return '<ingredient %r>' % self.igd_name
