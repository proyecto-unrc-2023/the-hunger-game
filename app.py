import os
from app import create_app
from app import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
    
    with app.app_context():
        db.create_all()
