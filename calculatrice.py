def add(x,y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Erreur: Division par zéro"
    return x / y
print("Sélectionnez l'opération:")
print("1. Addition")
print("2. Soustraction")
print("3. multiplication")
print("4. Division")

choice = input("Entrez votre choix (1/2/3/5): ")
num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxième nombre: "))
if choice == '1':
   print("Résultat:", add(num1, num2))
elif choice == '2':
   print("Résultat", subtract(num1, num2))
elif choice == '3':
   print("Résultat", multiply(num1, num2))
elif choice == '4':
   print("Résultat", divide(num1, num2))
else:
    print("Choix invalide")
