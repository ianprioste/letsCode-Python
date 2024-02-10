def transmissao(lista_loc_eixo_x, lista_loc_eixo_y):
    print('Cheguei!')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lista_loc_eixo_x_count = int(input().strip())

    lista_loc_eixo_x = []

    for _ in range(lista_loc_eixo_x_count):
        lista_loc_eixo_x_item = int(input().strip())
        lista_loc_eixo_x.append(lista_loc_eixo_x_item)

    lista_loc_eixo_y_count = int(input().strip())

    lista_loc_eixo_y = []

    for _ in range(lista_loc_eixo_y_count):
        lista_loc_eixo_y_item = int(input().strip())
        lista_loc_eixo_y.append(lista_loc_eixo_y_item)

    result = transmissao(lista_loc_eixo_x, lista_loc_eixo_y)

    fptr.write(str(result) + '\n')

    fptr.close()