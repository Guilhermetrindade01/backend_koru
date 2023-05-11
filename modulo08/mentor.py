import sqlite3

class Mentor:
    # Método que define o objeto mentor
    def __init__(self, nome: str, linkedin: str, id = None):
        self.id = id
        self.nome = nome
        self.linkedin = linkedin

    # Sempre que a palavra 'self' aparecer dentro do parênteses do método => é um método que precisa do objeto mentor já criado aqui no python
        # Retorna os valores guardados no objeto mentor em forma de dicionário
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "linkedin": self.linkedin
        }
    
    # Método que cria um novo mentor no banco de dados caso não haja id ou método que atualiza dados de um mentor caso haja id
    def save(self, db_connection: sqlite3.Connection):
        if self.id is None:
            query = "INSERT INTO mentores (nome_mentor, linkedin_mentor) VALUES (?, ?)"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.nome, self.linkedin))
            self.id = cursor.lastrowid
            # self.id = db_connection.execute(query, (self.nome, self.linkedin))
        else:
            query = "UPDATE mentores SET nome_mentor = ?, linkedin_mentor = ? WHERE id_mentor = ?"
            db_connection.execute(query, (self.nome, self.linkedin, self.id))
        db_connection.commit()
        db_connection.close()

    # Método que deleta mentor
    def delete(self, db: sqlite3.Connection):
        query = "DELETE FROM mentores WHERE id_mentor = ?"
        cursor = db.cursor()
        cursor.execute(query, (self.id, ))
        db.commit()
        db.close()

    # Método estático => método que não necessita de um objeto criado (no caso, o objeto mentor) para ser usado
    @staticmethod
    def get_by_id(id: int, db: sqlite3.Connection):
        query = "SELECT * FROM mentores WHERE id_mentor = ?"
        cursor = db.cursor()
        result = cursor.execute(query, (id, )).fetchone()
        if result:
            # Devolve um mentor inteiro
            return Mentor(id = result[0], nome = result[1], linkedin = result[2])
        else:
            return None
        
    @staticmethod
    def get_all(db: sqlite3.Connection):
        query = "SELECT * FROM mentores"
        cursor = db.cursor()
        results = cursor.execute(query).fetchall()
        mentors = []
        for result in results:
            mentors.append(Mentor(id = result[0], nome = result[1], linkedin = result[2]).to_dict())
        return mentors