from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import random
import string
from flask_cors import CORS
from waitress import serve

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)



class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)

with app.app_context():
    db.create_all()

def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(6))

@app.route('/api/encurtar', methods=['POST'])
def encurtar():
    original_url = request.json['url']
    short_url = generate_short_url()
    link = Link(original_url=original_url, short_url=short_url)
    db.session.add(link)
    db.session.commit()
    return jsonify({'short_url': short_url})

@app.route('/api/links', methods=['GET'])
def obter_links():
    links = Link.query.all()
    links_data = []
    for link in links:
        links_data.append({'original_url': link.original_url, 'short_url': link.short_url})
    return jsonify(links_data)


@app.route('/<short_url>')
def redirecionar(short_url):
    link = Link.query.filter_by(short_url=short_url).first()
    if link:
        return redirect(link.original_url)
    else:
        return 'URL curta não encontrada', 404

if __name__ == '__main__':
    
    port = int(os.getenv('PORT', 5000))  # A variável PORT é fornecida pelo Render
    print(f"Server started on port {port}")
    serve(app, host='0.0.0.0', port=port)