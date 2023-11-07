from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True) # id is a column in the table
    name = db.Column(db.String(80), unique=False, nullable=False) # name is a column in the table
    description = db.Column(db.String)
    # price = db.Column(db.Float(precision=2), unique=False, nullable=False) # price is a column in the table
    # store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False) # store_id is a column in the table
    # store = db.relationship("StoreModel", back_populates="items") # store is a column in the table
    # tags = db.relationship("TagModel", back_populates="items", secondary="items_tags") # tags is a column in the table
    orders = db.relationship("OrderModel", secondary="order_items", back_populates="items") # orders is a column in the table
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    variants = db.relationship("VariantModel", back_populates="item", lazy="dynamic", cascade="all, delete")
    image_url = db.Column(db.String(255), unique=False, nullable=True) # image_url is a column in the table
