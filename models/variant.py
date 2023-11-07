from db import db

class VariantModel(db.Model):
    __tablename__ = 'variants'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    color = db.Column(db.String(30))
    size = db.Column(db.String(30))
    quantity = db.Column(db.Integer, nullable=False)

    price = db.Column(db.Float(precision=2))

    item = db.relationship('ItemModel', back_populates='variants')

    # Add a unique constraint to ensure no duplicate variants
    __table_args__ = (db.UniqueConstraint('item_id', 'color', 'size', name='_item_color_size_uc'),)
