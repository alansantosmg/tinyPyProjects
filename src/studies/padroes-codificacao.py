
# Comentários devem ter no máximo 72 caracteres
# Por padrão o PEP 8 recomenda tamanho max. de 80 linhas. 
# tab stop = 4
# tabs = spaces

padrao_nome_de_variavel = 4

def minha_funcao(x: int, y: int) -> int:
    """Teste.

    ARGS: 
        x: recebe valor x
        y: recebe rvalor y

    VARS:

        r: retorna x + y

    Esta função recebe valores x e y

    """

    r = x + y
    pass


def segunda_funcao(x: int, y: int) -> int:
    """Teste

    ARGS: 
        x recebe valor x
        y recebe rvalor y

    Esta função recebe valores x e y. 
    De uma função para outra separar com 2 linhas em branco

    """
    
    pass


# Padrão para classe é capital letter

class MinhaClasse:

    def __init__():
        pass

    def metodo_publico(x: int, y: int) -> int:
        # De um método para outro separar com 1 linha em branco."
        pass

    def __funcao_publica():
        pass