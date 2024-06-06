from rich.console import Console
from rich.table import Table 

console = Console()

def get_user_data():
  users = []
  while True:
    nome = input("Digite o nome: (ou 'ok' para encerrar)")
    if nome. lower() == 'ok':
     break
    idade = input("Digite a idade:")
    email = input("Digite seu email:")


    try:
       idade = int(idade)
    except ValueError:
       console.print("[bold red]Idade invalida. Entre com os teclados numericos corretos. [/bold red]")
       continue

  users.append({"Nome": nome, "Idade": idade, "Email": email})

  return users 

users = get_user_data()

table = Table(title="user information")

table.add_column("Nome", justify="left", style="cyan", no_wrap=True)
table.add_column("Idade", justify="right", styly="magenta")
table.add_collumn("Email", justify="left", styly="green")

for user in users:
  table.add_row(user["Nome"], str(user["Idade"]), user["Email"])

console.print(table) 