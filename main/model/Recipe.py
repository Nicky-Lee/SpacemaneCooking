from .. import db


# recipe_ingredient = db.Table('recipe_ingredient',
#                              db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
#                              db.Column('igd_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
#                              )


# ingredient_tag = db.Table('ingredient_tag',
#     db.Column('igd_category_id', db.Integer, db.ForeignKey('IGD_category.id')),
#     db.Column('igd_id', db.Integer, db.ForeignKey('Ingredient.id'))
# )
#
# association_table = db.Table(
#     "association",
#     db.Column("ingredient_id", db.ForeignKey("Ingredient.id"), primary_key=True),
#     db.Column("recipe_id", db.ForeignKey("Recipe.id"), primary_key=True),
# )


class Recipe(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    R_name = db.Column(db.String(80), nullable=True)
    R_description = db.Column(db.String(240), nullable=True)
    R_category = db.Column(db.String(120), nullable=True)
    R_calorie = db.Column(db.Integer, nullable=True)
    image_id = db.Column(db.Integer)

    # igd_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, R_name, user_id, R_description=None, R_category=None, R_calorie=0, R_img_url=None):
        self.R_name = R_name
        self.R_description = R_description
        self.R_category = R_category
        self.R_calorie = R_calorie
        self.user_id = user_id
        self.R_img_url = R_img_url

    def __repr__(self):
        return '<Recipe %r>' % self.R_name


# class IGD_category(db.Model):
#     __tablename__ = 'igd_category'
#
#     id = db.Column(db.Integer, primary_key=True)
#     igd_category = db.Column(db.String(30), unique=True, nullable=False)
#     igd_id = db.Column(db.Integer,db.ForeignKey('ingredient.id'))
#
#     # igd=db.relationship('Ingredient',secondary=ingredient_tag)
#
#     # igd_id = db.relationship("Ingredient", secondary=ingredient_tag, backref="IGD_category")
#     # recipe = db.relationship("recipe", backref="ingredient")
#     # recipe = db.Column(db.Integer, db.ForeignKey('recipe.id'))
#     # recipe = db.relationship('recipe', secondary=recipe_ingredient,backref='ingredient')
#
#     def __init__(self, igd_category):
#         self.igd_category = igd_category


# class Ingredient(db.Model):
#     __tablename__ = 'ingredient'
#
#     id = db.Column(db.Integer, primary_key=True)
#     igd_name = db.Column(db.String(80), unique=True, nullable=False)
#     igd_category = db.Column(db.String(120), nullable=True)
#     igd_opponent = db.Column(db.String(80))
#     igd_calorie = db.Column(db.Integer, nullable=True)
#     image_id = db.Column(db.Integer)
#     # recipe = db.Column(db.Integer,db.ForeignKey('Recipe.id'))
#
#
#     # recipe = db.relationship("Recipe", secondary=association_table, backref="Ingredient")
#     # recipe = db.relationship("recipe", backref="ingredient")
#     # recipe = db.Column(db.Integer, db.ForeignKey('recipe.id'))
#     # recipe = db.relationship('recipe', secondary=recipe_ingredient,backref='ingredient')
#
#     def __init__(self, igd_name, igd_category=None,igd_opponent=None, igb_description=None, igd_calorie=0, image_id=None):
#         self.igd_name = igd_name
#         self.igd_category=igd_category
#         self.igd_opponent = igd_opponent
#         self.igb_description = igb_description
#         self.igd_calorie = igd_calorie
#         self.image_id =image_id
#
#     def __repr__(self):
#         return '<ingredient %r>' % self.igd_name

#
tags = db.Table('tags'
                , db.Column('igd_category_id', db.Integer, db.ForeignKey('igd_category.id'))
                , db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')))


class IGD_category(db.Model):
    __tablename__ = 'igd_category'
    id = db.Column(db.Integer, primary_key=True)
    igd_category_name = db.Column(db.String(30), unique=True, nullable=False)
    Ingredient = db.relationship('Ingredient', secondary=tags)

    def __init__(self, igd_category_name):
        self.igd_category_name = igd_category_name




class Ingredient(db.Model):
    ___tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    igd_name = db.Column(db.String(80), unique=True, nullable=False)
    igd_category = db.Column(db.String(120), nullable=True)
    igd_opponent = db.Column(db.String(80))
    igd_calorie = db.Column(db.Integer, nullable=True)
    image_id = db.Column(db.Integer)

    # student_id=db.Column(db.Integer,db.ForeignKey('student.id'))
    def __init__(self, igd_name, igd_category=None, igd_opponent=None, igb_description=None, igd_calorie=0,
                 image_id=None):
        self.igd_name = igd_name
        self.igd_category = igd_category
        self.igd_opponent = igd_opponent
        self.igb_description = igb_description
        self.igd_calorie = igd_calorie
        self.image_id = image_id


