class Contato:
    def __init__(self, name, email, telefone):
        self.name = name
        self.email = email
        self.telefone = telefone
        self.activities = []
        self.tasks = []
        self.sales_stage = "Lead"  # Lead > Prospecto > Venda fechada
        self.stage_history = "Lead"  # Histórico de stages

class Atividade:
    def __init__(self, type, description):
        self.type = type  # ex: "call", "email", "meeting"
        self.description = description

class Task:
    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.completed = False

class EmailCampaign:
    def __init__(self, title, description, target_stage):
        self.title = title
        self.description = description
        self.target_stage = target_stage
        self.sent_to = []


class CRM:
    def __init__(self):
        self.contatos = []
        self.campanhas = []

    def add_contato(self):
        name = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        self.contatos.append(Contato(name, email, telefone))
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        for i, c in enumerate(self.contatos):
            print(f"{i+1}. {c.name} - {c.email} - {c.sales_stage}")

    def add_atividade(self):
        self.listar_contatos()
        idx = int(input("Escolha o contato (número): ")) - 1
        tipo = input("Tipo (chamada/email/reunião): ")
        desc = input("Descrição: ")
        self.contatos[idx].activities.append(Atividade(tipo, desc))
        print("Atividade registrada!")

    def add_task(self):
        self.listar_contatos()
        idx = int(input("Escolha o contato (número): ")) - 1
        titulo = input("Título da tarefa: ")
        data = input("Data (dd/mm/aaaa): ")
        self.contatos[idx].tasks.append(Task(titulo, data))
        print("Tarefa adicionada!")

    def update_sales_stage(self):
        self.listar_contatos()
        idx = int(input("Escolha o contato (número): ")) - 1
        print("Estágios: Lead > Prospecto > Venda fechada")
        novo_estagio = input("Novo estágio: ")
        self.contatos[idx].sales_stage = novo_estagio
        self.contatos[idx].stage_history.append = novo_estagio
        print("Estágio de venda atualizado!")

    def add_email_campaign(self):   
        title = input("Título da campanha: ")
        description = input("Descrição: ")
        target_stage = input("Estágio alvo? (Lead/Prospecto/Venda fechada): ")
        self.campanhas.append(EmailCampaign(title, description, target_stage))
        print("Campanha de email criada!")

    def report_summary(self):
        print("\n=== Relatório ===")
        print(f"Total de contatos: {len(self.contatos)}")
        por_estagio = {"Lead": 0, "Prospecto": 0, "Venda fechada": 0}
        for c in self.contatos:
            estagio = c.sales_stage
            if estagio in por_estagio:
                por_estagio[estagio] += 1
        for estagio, qt in por_estagio.items():
            print(f"{estagio}: {qt} contato(s)")


    

def main():
    crm = CRM()
    while True:
        print("\n--- MENU CRM ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Registrar atividade")
        print("4. Criar tarefa")
        print("5. Registrar campanha de email")
        print("6. Atualizar estágio de venda")
        print("7. Relatório")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            crm.add_contato()
        elif opcao == "2":
            crm.listar_contatos()
        elif opcao == "3":
            crm.add_atividade()
        elif opcao == "4":
            crm.add_task()
        elif opcao == "5":
            crm.add_email_campaign()
        elif opcao == "6":
            crm.update_sales_stage()
        elif opcao == "7":
            crm.report_summary()
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()


