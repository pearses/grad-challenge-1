from models.item import Item
from dto.item_dto import ItemDTO
from models.db import db

class ItemService():
    def create_item(self, name, description):
        item = Item(name=name, description=description)
        db.session.add(item)
        db.session.commit()
        return item.id

    def get_items(self, item_id):
        item = Item.query.get(item_id)
        return item

    def get_all_items(self):
        items = Item.query.all()
        return [ItemDTO(item.id, item.name, item.description) for item in items]


    def update_item(self, item_id, name, description):
        item = Item.query.get(item_id)
        if item:
            item.name = name
            item.description = description
            db.session.commit()
            return True
        return False
    
    def delete_item(self, item_id):
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
