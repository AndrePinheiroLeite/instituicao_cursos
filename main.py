from curso_dao import CursoDAO
from database import ConexaoBanco
from cursos import Cursos

def menu():
    db = ConexaoBanco()
    db.conectar()
    db.criar_tabelas()
    curso_dao = CursoDAO(db)


    while True:
            try:      
                print("======= MENU PARA CADASTRO DIGITE UMA DAS OPÇÃO: ========= ")
                print("======= PARA CADASTRAR UM CURSO DIGITE OPÇÃO 1:=========== ") 
                print("========PARA SAIR DIGITE OPÇÃO 0: =========================")
                print("=============================================================")
                print("")

                opcao = int(input("Digite uma das opção: "))
           

                if opcao == 1:
                    nome_curso = input("Digite o nome do curso: ")
                    categoria = input("Qual é a categoria do curso: ")
                    carga_horaria = int(input("Qual é a carga horaria do curso ex: 30, 40: "))
                    curso = Cursos(nome_curso,categoria,carga_horaria)
                    curso_dao.salvar_curso(curso)
                    


                elif opcao == 0:
                    print("Você escolheu a opção 0, sair!...")
                    db.fechar()
                    break
                else:
                    print("Você precisa escolher uma das opção de 1 a 0")
            except ValueError as e:
                print(f"Erro: opção inválida({e})")
          
                




if __name__ == "__main__":
    menu()