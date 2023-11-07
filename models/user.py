from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(256), nullable=False, server_default='Default Address')
    cart_items = db.relationship("Cart_Items_Model", back_populates="user", lazy="dynamic", cascade="all, delete")
    orders = db.relationship("OrderModel", back_populates="user", lazy="dynamic", cascade="all, delete")
