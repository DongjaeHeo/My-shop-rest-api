from db import db

class OrderItemModel(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    quantity = db.Column(db.Integer, nullable=False)
    item = db.relationship("ItemModel", back_populates="orders")
    order = db.relationship("OrderModel", back_populates="items")
