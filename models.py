from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()

class Note(db.Model):
    __tablename__ = 'notes'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)  # Título único
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"

    def to_dict(self):
        """Representa a nota como um dicionário."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
        }

    @classmethod
    def create(cls, title, content):
        """Cria uma nova nota e a adiciona ao banco de dados."""
        new_note = cls(title=title, content=content)
        try:
            db.session.add(new_note)
            db.session.commit()
            return new_note
        except IntegrityError:
            db.session.rollback()
            return None

    @classmethod
    def get_all(cls):
        """Retorna todas as notas do banco de dados."""
        return cls.query.all()

    @classmethod
    def get_by_id(cls, note_id):
        """Retorna uma nota pelo seu ID."""
        return cls.query.get(note_id)

    @classmethod
    def update(cls, note_id, title=None, content=None):
        """Atualiza uma nota existente."""
        note = cls.query.get(note_id)
        if note:
            if title:
                note.title = title
            if content:
                note.content = content
            db.session.commit()
            return note
        return None

    @classmethod
    def delete(cls, note_id):
        """Exclui uma nota pelo seu ID."""
        note = cls.query.get(note_id)
        if note:
            db.session.delete(note)
            db.session.commit()
            return True
        return False
