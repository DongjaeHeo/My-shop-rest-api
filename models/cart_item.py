from db import db

class CartItemModel(db.Model):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
