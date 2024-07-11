def calcular_multa(velocidade):
 
  if velocidade <= 80:
    return 0.0

  excesso = velocidade - 80
  multa = excesso * 5.0

  return multa

velocidade_usuario = float(input("Digite a velocidade do carro (km/h): "))

multa = calcular_multa(velocidade_usuario)

if multa > 0:
  print(f"Você foi multado! O valor da multa é de {multa:.2f} euros.")
else:
  print("Você não foi multado.")
