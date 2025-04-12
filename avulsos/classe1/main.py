from pessoa import Pessoa
from pessoa import Fazendo
#from pessoa import Pessoa, Fazendo
#from pessoa import *

def main():
    p1 = Pessoa("nome1", 17, 1.80, 80, "end1")
    p1.exibirDados()
    imc = p1.calcIMC()
    print(f"IMC: {imc:.2f}")
    print("Class id:", Pessoa.class_id)
    print("Numero de objetos: ", Pessoa.num_pessoa)
    print("------------------")
    pf1 = Fazendo("martelo", "estante")
    pf1.fazendo()
    print("Class id: ", Fazendo.class_id)

if __name__ == "__main__":
    main()