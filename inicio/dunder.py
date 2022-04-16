"""
dunder name -> __name__

dunder main -> __main__

Em python, sõa utilizados dunder para criar funções, atributos, propriedades e etc utilizando
Double under para não gerar conflito com os nomes desses elementos na programação.

#na linguagem C, temos um programa da seguinte forma:

int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}
# Em Python, se executarmos um módulo Python diretamente na linha de comando, intenamenteo python atribuirá à variavel
__name__ o valor __main__ indicando que este módulo é o módulo de execução principal.


"""

from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))
