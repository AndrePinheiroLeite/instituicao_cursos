class Cursos:
    def __init__ (self,nome_curso,categoria,carga_horaria,id=None):
        #Atributos encapsulados e protegido 
        self.id = id
        self.nome_curso = nome_curso
        self.categoria = categoria
        self.carga_horaria = carga_horaria

    @property
    def nome_curso(self):
        return self._nome_curso

    @nome_curso.setter
    def nome_curso(self,valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do curso não pode ser vazio")
        self._nome_curso = valor.strip()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome da categoria não pode ser vazio")
        self._categoria = valor.strip()

    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
            raise ValueError("A carga horária deve ser um número inteiro maior que zero.")       
        self._carga_horaria = valor