from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Tatiana")
print(result)

suma = client.service.SumaDosNumeros(num1=5, num2=3)
print(suma)

es_palindromo = client.service.CadenaPalindromo(cadena="radar")
print(es_palindromo)
