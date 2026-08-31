import subprocess
while True:
  try:
    subprocess.run("cls", shell=True)
    Age = int(input("Age: "))
    break
  except ValueError:
     print("Ingresar un valor numérico.")
     input("Press Enter to continue...")

print("Age registered: ", Age)