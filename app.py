from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Inicializa o banco de dados
db = SQLAlchemy()

# Criação do aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Modelo de Nota
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
        }


# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()


# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')


# Rota para criar uma nova nota
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()  # Recebe os dados no formato JSON

    if not data or not all(key in data for key in ('title', 'content')):
        return jsonify({'error': 'Dados inválidos'}), 400

    new_note = Note(title=data['title'], content=data['content'])

    try:
        db.session.add(new_note)
        db.session.commit()
        return jsonify(new_note.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Nota já existe'}), 409


# Rota para listar todas as notas
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([note.to_dict() for note in notes])


# Rota para obter uma nota específica
@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get(id)
    if note:
        return jsonify(note.to_dict())
    return jsonify({'error': 'Nota não encontrada'}), 404


# Rota para atualizar uma nota
@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.get_json()
    note = Note.query.get(id)

    if not note:
        return jsonify({'error': 'Nota não encontrada'}), 404

    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)
    db.session.commit()

    return jsonify(note.to_dict())


# Rota para excluir uma nota
@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get(id)
    if note:
        db.session.delete(note)
        db.session.commit()
        return jsonify({'message': 'Nota excluída com sucesso'})
    return jsonify({'error': 'Nota não encontrada'}), 404


# Executa o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
