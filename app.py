import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
    with app.app_context():
        for rule in app.url_map.iter_rules():
            print(rule)
