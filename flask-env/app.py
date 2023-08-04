from flask import Flask, jsonify, request
from models.db import db
from dto.item_dto import ItemDTO
from services.item_service import ItemService
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
migrate = Migrate(app, db)
item_service = ItemService()


# --- ROUTES ---
# Return list of all items
#@app.route('/items', methods=['GET'])
#def get_items():
#    items = item_service.get_all_items()
#    return jsonify(items)
@app.route('/items', methods=['GET'])
def get_items():
    items = item_service.get_all_items()
    return jsonify([{
        'item_id': item.item_id,
        'name': item.name,
        'description': item.description
    } for item in items])

# NOT WORKING -----------
# Return single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_single_item(item_id):
    item = item_service.get_item(item_id)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item ID not found'}), 404

@app.route('/items', methods=['POST'])
def create_single_item():
    data = request.get_json()
    item_id = item_service.create_item(data['name'], data['description'])
    return jsonify({'message': 'Item created', 'id': item_id}), 201

# -- NOT WORKING
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_single_item(item_id):
    data = request.get_json()
    success = item_service.update_item(item_id, data['name'], data['description'])
    if success:
        return jsonify({'message': 'Item has been successfully updated'}), 200
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run()
