# README do Projeto
[![Build Status](https://app.travis-ci.com/joao0710/CalculoPECLD.svg?token=JzbHqyx2baBX9NvsAAcG)](https://app.travis-ci.com/joao0710/CalculoPECLD)
## Visão Geral

Este projeto é um sistema automatizado para calcular a Provisão para Perda Esperada (PE) associada ao risco de crédito, em total conformidade com a Resolução CMN n° 4.966. A principal finalidade é fornecer uma ferramenta robusta para instituições financeiras, que permite a importação de dados de carteiras de crédito, a classificação de contratos em diferentes estágios de risco e a geração de cálculos de PE de forma eficiente e transparente.

A solução otimiza o processo de conformidade regulatória, oferecendo a capacidade de auditar os cálculos e de gerar relatórios detalhados para análise de risco.

## Funcionalidades Principais

* **Importação de Dados:** Rotina para ingestão de bases de dados de contratos de crédito em massa.
* **Modelagem de Risco:** Cálculo automatizado de parâmetros de risco, incluindo:
    * **Probabilidade de Inadimplência (PD):** Análise e determinação da probabilidade de um contrato entrar em inadimplência.
    * **Perda Dada a Inadimplência (LGD):** Estimativa da perda em caso de inadimplência.
    * **Exposição na Data da Inadimplência (EAD):** Cálculo do valor exposto ao risco de crédito.
* **Classificação de Estágios:** Lógica de negócio para categorizar os contratos em Estágios 1, 2 e 3, com base em critérios de aumento de risco e tempo de atraso.
* **Cálculo da Perda Esperada:** Execução da fórmula `PE = PD x EAD x LGD` para cada contrato.
* **Relatórios e Análise:** Geração de relatórios e visualizações para análise agregada da carteira, incluindo matrizes de migração entre estágios, gráficos de rolagem de atraso e dashboards interativos.

## Tecnologias

* **Backend:**
    * Python 3.13
    * Django
    * Django REST Framework (para API, se aplicável)
    * Celery (para processamento de tarefas em segundo plano)
* **Banco de Dados:**
    * PostgreSQL (recomendado para performance e escalabilidade)
* **Frontend (opcional):**
    * React, Vue.js ou outro framework JavaScript (para a interface do usuário)

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento.

### Pré-requisitos

Certifique-se de que os seguintes softwares estão instalados na sua máquina:

* Python 3.8+
* `pip` (gerenciador de pacotes do Python)
* `virtualenv`
* PostgreSQL
* Redis (necessário para o Celery)

### Configuração do Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-projeto.git](https://github.com/seu-usuario/seu-projeto.git)
    cd seu-projeto
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    virtualenv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o banco de dados:**
    Edite o arquivo `settings.py` para incluir as credenciais do seu banco de dados PostgreSQL.

5.  **Aplique as migrações:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Inicie os serviços:**
    ```bash
    # Inicie o servidor web
    python manage.py runserver

    # Em uma nova janela de terminal, inicie o worker do Celery
    celery -A seu_projeto_base worker --loglevel=info
    ```

## Uso

* Acesse a interface administrativa do Django em `http://127.0.0.1:8000/admin` para gerenciar os modelos.
* Utilize o `management command` para importar dados da sua carteira de crédito:
    ```bash
    python manage.py importar_carteira --file=caminho/para/seus/dados.csv
    ```

## Estrutura do Projeto

* `app_core/`: Lógica central do projeto.
* `app_reports/`: Módulo para relatórios e visualizações.
* `app_data_ingestion/`: Módulo para importação de dados.
* `requirements.txt`: Lista de dependências do Python.
* `manage.py`: Utilitário para gerenciamento do projeto.

## Contribuição

Contribuições são muito bem-vindas. Para contribuir, siga o padrão de `fork`, `branch`, `commit` e `pull request`.

## Licença

Este projeto está licenciado sob a Licença MIT.
