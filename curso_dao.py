import sqlite3

class CursoDAO:
    def __init__(self, db):
        self.db = db

    def salvar_curso(self,curso):
        try:
            sql = """
                 INSERT INTO cursos(nome_curso, categoria, carga_horaria)
                 VALUES (?,?,?)
            """
            valores = (curso.nome_curso, curso.categoria, curso.carga_horaria)
            self.db.cursor.execute(sql,valores)
            self.db.conexao.commit()
            print("CURSO SALVO COM SUCESSO!: ")
        except sqlite3.Error as e:
            print(f"ERRO AO SALVAR CURSO: {e}")
