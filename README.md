# Sistema de Gerenciamento de Relacionamento com o Cliente (CRM)

Um sistema de CRM simples e eficiente implementado em Python, oferecendo funcionalidades essenciais para gerenciar contatos, leads, atividades e campanhas de marketing.

## 🚀 Funcionalidades

### ✅ Implementadas

- **📋 Gerenciamento de Contatos**: Armazena e gerencie informações completas de contato (nome, e-mail, telefone)
- **📈 Funil de Vendas**: Gerencie as etapas do processo de vendas com histórico de mudanças de estágio
- **📝 Rastreamento de Atividades**: Registre interações como chamadas, e-mails e reuniões
- **⏰ Agendamento de Tarefas**: Organize tarefas e compromissos com datas específicas
- **📧 Campanhas de E-mail**: Crie e envie campanhas segmentadas por estágio de vendas
- **🎯 Gerenciamento de Leads**: Rastreie leads e converta-os em contatos
- **📊 Relatórios e Análises**: Visualize resumos de vendas e distribuição por estágio

### ❌ Não Implementadas

- **📱 Acesso Mobile**: Funcionalidade para dispositivos móveis
- **🎨 Painéis Personalizáveis**: Dashboards customizáveis por perfil de usuário
- **📁 Gerenciamento de Documentos**: Armazenamento de arquivos relacionados a vendas

## 🛠️ Instalação e Execução

### Pré-requisitos

- Python 3.6 ou superior instalado

### Como executar

1. **Clone o repositório**
   ```bash
   git clone github.com/jwaozera/crm-tool
   cd crm-system
   ```

2. **Salve o código principal**
   - Certifique-se de que o arquivo principal esteja salvo como `crm.py`

3. **Execute o sistema**
   ```bash
   python crm.py
   ```

4. **Navegue pelo menu**
   - O programa apresentará um menu interativo
   - Digite o número da opção desejada e pressione Enter
   - Os dados são salvos automaticamente em `crm_data.json`

## 📁 Estrutura de Dados

O sistema utiliza um arquivo JSON (`crm_data.json`) para persistência de dados, contendo:

- **Contatos**: Informações pessoais e histórico de vendas
- **Leads**: Potenciais clientes em prospecção
- **Atividades**: Registro de interações
- **Tarefas**: Compromissos agendados
- **Campanhas**: Histórico de e-mail marketing

## 🎯 Estágios de Vendas

O sistema gerencia os seguintes estágios:

- **Lead**: Primeiro contato identificado
- **Prospecto**: Lead qualificado em avaliação
- **Proposta**: Apresentação de soluções
- **Negociação**: Discussão de termos
- **Venda Fechada**: Conversão bem-sucedida

## 📈 Relatórios Disponíveis

- Total de contatos cadastrados
- Distribuição por estágio de vendas

  
