from modelos.restaurante import Restaurante

restaurant_praca = Restaurante('praça','Gourmet')
restaurant_mexicano = Restaurante('Mexican food','Mexicana')
restaurant_japones = Restaurante('Japa','Japonesa')

restaurant_praca.receber_avaliacao('Gui', 10)
restaurant_praca.receber_avaliacao('Ana', 8)
restaurant_praca.receber_avaliacao('bob', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()