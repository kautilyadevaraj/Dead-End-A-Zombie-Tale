# shop_items.py
from .models import db, ShopItem
from website import create_app

app = create_app()

shop_item_data = [
    {"name": "Knife", "description": "Restores some health points", "cost": 10},
    {"name": "Flashlight", "description": "Increases defense", "cost": 250},
    {"name": "First-aid", "description": "Increases defense", "cost": 30},
]

def populate_shop():
    with app.app_context():
        for item_data in shop_item_data:
            existing_item = ShopItem.query.filter_by(name=item_data["name"]).first()
            if not existing_item:
                new_item = ShopItem(**item_data)
                db.session.add(new_item)

        db.session.commit()
