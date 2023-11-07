from db import db

class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("UserModel", back_populates="orders")
    total_price = db.Column(db.Float(precision=2), nullable=False)
    items = db.relationship("ItemsModel", secondary="order_items", back_populates="order", lazy="dynamic", cascade="all, delete")
    order_items = db.relationship("OrderItemModel", back_populates="order", lazy="dynamic", cascade="all, delete")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    status = db.Column(db.String(80), nullable=False, server_default='Pending')
    address = db.Column(db.String(256), nullable=False, server_default='Default Address')
