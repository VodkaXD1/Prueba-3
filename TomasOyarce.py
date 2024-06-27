import FuncionesP3 as fn
while True:
    print("1) Registrar Libro")
    print("2) Listar Libros")
    print("3) Registrar venta")
    print("4) imprimir reporte de ventas")
    print("5) Generar txt")
    print("6) Salir el programa")

    op=int(input("Ingrese una opcion: "))

    if op==1:
        fn.RegistrarLibro()
    elif op==2:
        fn.ListarTodosLosLibros
    elif op==3:
        fn.RegistrarVenta()
    elif op==4:
        fn.ImprimirReportDeVentas()
    elif op==5:
        fn.GenerarTxt
    elif op==6:
        print("Programa terminado")
        break
    else:
        print("opcion no valida")