from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True) # id is a column in the table
    name = db.Column(db.String(80), unique=True, nullable=False) # name is a column in the table
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete") # items is a column in the table
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
