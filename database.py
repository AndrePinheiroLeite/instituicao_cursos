import sqlite3

class ConexaoBanco:
    def __init__ (self,nome_banco = "instituto.db"):
        self.nome_banco = nome_banco
        self.conexao = None
        self.cursor = None

    def conectar (self):
        """ABRE A CONEXÃO COM BANCO DE DADOS SQLTE"""
        try:
            self.conexao = sqlite3.connect(self.nome_banco)
            self.cursor = self.conexao.cursor()
            self.cursor.execute("PRAGMA foreign_keys = ON;")
            print("[LOG] CONEXÃO COM O BANCO DE DADOS ESTABELECIDA COM SUCESSO! ")
        except sqlite3.Error as e:
            print(f"[Erro] ERRO AO CONECTAR AO BANCO DE DADOS: {e}")

    def criar_tabelas(self):
        try:
            if not self.cursor: self.conectar()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_curso TEXT NOT NULL,
                categoria TEXT NOT NULL,
                carga_horaria INTEGER NOT NULL
             )    
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inscricoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_aluno TEXT NOT NULL,
            cpf TEXT NOT NULL,
            curso_id INTEGER NOT NULL,
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
            
            )
            """)

            

            self.conexao.commit()
            print("[LOG] TABELAS VERIFICADAS E CRIADA COM SUCESSO NO SQLITE3")
        except sqlite3.Error as e:
            print(f"[ERRO] Erro ao criar as tabelas: {e}")

    def fechar(self):
        if self.conexao:
            self.conexao.close()
            print("[LOG] CONEXÃO COM O BANCO DE DADOS DE FECHADA!")

            
#bloco de teste para o banco de dados
if __name__ == "__main__":
    db = ConexaoBanco()
    db.conectar()
    db.criar_tabelas()
    db.fechar()