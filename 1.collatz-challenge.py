def collatz(num):
  if (num % 2) == 0:
    return num/2  
  else:
    return 3*num + 1

def contar_pasos_desde(num_inicial):
  pasos = 1;
  num_actual = num_inicial;
  llego_a_uno = False;
  while not llego_a_uno:
    numero_siguiente = collatz(num_actual)
    num_actual = numero_siguiente;
    pasos += 1
    if num_actual == 1:
      llego_a_uno = True;
  return pasos

def conseguir_mayor_cantidad_de_pasos(max_lim):
  mayor_cantidad_de_pasos = 0;
  mayor_num_inicial = 0;
  for x in range(1,max_lim):
    if contar_pasos_desde(x) > mayor_cantidad_de_pasos:
      mayor_cantidad_de_pasos = contar_pasos_desde(x);
      mayor_num_inicial = x;
  return mayor_num_inicial;


print(conseguir_mayor_cantidad_de_pasos(1000000));



      
  


