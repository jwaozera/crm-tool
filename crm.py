import json
from datetime import datetime

class Contato:
    def __init__(self, name, email, telefone, company="", notes=""):
        self.id = id(self)
        self.name = name
        self.email = email
        self.telefone = telefone
        self.company = company
        self.notes = notes
        self.sales_stage = "Lead"
        self.stage_history = ["Lead"]
        self.activities = []
        self.tasks = []
        self.created_at = datetime.now().strftime("%d/%m/%Y")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "telefone": self.telefone,
            "company": self.company,
            "notes": self.notes,
            "sales_stage": self.sales_stage,
            "stage_history": self.stage_history,
            "created_at": self.created_at,
            "activities": [a.__dict__ for a in self.activities],
            "tasks": [t.__dict__ for t in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        c = cls(data["name"], data["email"], data["telefone"], data.get("company", ""), data.get("notes", ""))
        c.id = data["id"]
        c.sales_stage = data.get("sales_stage", "Lead")
        c.stage_history = data.get("stage_history", ["Lead"])
        c.created_at = data.get("created_at", datetime.now().strftime("%d/%m/%Y"))
        c.activities = [Atividade(**a) for a in data.get("activities", [])]
        c.tasks = [Task(**t) for t in data.get("tasks", [])]
        return c


class Atividade:
    def __init__(self, type, description):
        self.type = type
        self.description = description
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M")


class Task:
    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.completed = False


class CRM:
    def __init__(self):
        self.contatos = []
        self.load_data()

    def save_data(self):
        with open("contatos.json", "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contatos], f, indent=2, ensure_ascii=False)

    def load_data(self):
        try:
            with open("contatos.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.contatos = [Contato.from_dict(c) for c in data]
        except FileNotFoundError:
            self.contatos = []

    def add_contato(self):
        name = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        company = input("Empresa (opcional): ")
        notes = input("Notas (opcional): ")
        c = Contato(name, email, telefone, company, notes)
        self.contatos.append(c)
        self.save_data()
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
        self.save_data()
        print("Atividade registrada!")

    def add_task(self):
        self.listar_contatos()
        idx = int(input("Escolha o contato (número): ")) - 1
        titulo = input("Título da tarefa: ")
        data = input("Data (dd/mm/aaaa): ")
        self.contatos[idx].tasks.append(Task(titulo, data))
        self.save_data()
        print("Tarefa adicionada!")

    def update_sales_stage(self):
        self.listar_contatos()
        idx = int(input("Escolha o contato (número): ")) - 1
        novo = input("Novo estágio (Lead/Prospecto/Venda fechada): ")
        self.contatos[idx].sales_stage = novo
        self.contatos[idx].stage_history.append(novo)
        self.save_data()
        print("Estágio de venda atualizado!")

    def report_summary(self):
        print("\n=== Relatório ===")
        print(f"Total de contatos: {len(self.contatos)}")
        por_estagio = {"Lead": 0, "Prospecto": 0, "Venda fechada": 0}
        for c in self.contatos:
            if c.sales_stage in por_estagio:
                por_estagio[c.sales_stage] += 1
        for estagio, qtd in por_estagio.items():
            print(f"{estagio}: {qtd} contato(s)")


def main():
    crm = CRM()
    while True:
        print("\n--- MENU CRM ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Registrar atividade")
        print("4. Criar tarefa")
        print("5. Atualizar estágio de venda")
        print("6. Relatório")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1": crm.add_contato()
            case "2": crm.listar_contatos()
            case "3": crm.add_atividade()
            case "4": crm.add_task()
            case "5": crm.update_sales_stage()
            case "6": crm.report_summary()
            case "7":
                crm.save_data()
                print("Saindo... dados salvos.")
                break
            case _: print("Opção inválida.")


if __name__ == "__main__":
    main()
