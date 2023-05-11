import sqlite3

class Mentorando:
    def __init__(self, nome: str, linkedin: str, id = None):
        self.id = id
        self.nome = nome
        self.linkedin = linkedin

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "linkedin": self.linkedin
        }
    
    # Este método da classe Mentorandos possui novamente o 'cursor', pois será necessário chamar o lastrowid e isso só é possível com ele presente
    def save(self, db_connection: sqlite3.Connection):
        if self.id is None:
            query = "INSERT INTO mentorandos (nome_mentorando, linkedin_mentorando) VALUES (?, ?)"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.nome, self.linkedin))
            self.id = cursor.lastrowid
        else:
            query = "UPDATE mentorandos SET nome_mentorando = ?, linkedin_mentorando = ? WHERE id_mentorando = ?"
            db_connection.execute(query, (self.nome, self.linkedin, self.id))
        db_connection.commit()
        db_connection.close()

    # Método que deleta mentorando
    def delete(self, db: sqlite3.Connection):
        query = "DELETE FROM mentorandos WHERE id_mentorando = ?"
        cursor = db.cursor()
        cursor.execute(query, (self.id, ))
        db.commit()
        db.close()

    @staticmethod
    def get_by_id(id: int, db: sqlite3.Connection):
        query = "SELECT * FROM mentorandos WHERE id_mentorando = ?"
        cursor = db.cursor()
        result = cursor.execute(query, (id, )).fetchone()
        if result:
            # Devolve um mentorando inteiro
            return Mentorando(id = result[0], nome = result[1], linkedin = result[2])
        else:
            return None
        
    @staticmethod
    def get_all(db: sqlite3.Connection):
        query = "SELECT * FROM mentorandos"
        cursor = db.cursor()
        results = cursor.execute(query).fetchall()
        mentorandos = []
        for result in results:
            mentorandos.append(Mentorando(id = result[0], nome = result[1], linkedin = result[2]).to_dict())
        return mentorandos