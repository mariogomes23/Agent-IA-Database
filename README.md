# Agente de IA para consultas em banco de dados

Este repositório contém um projeto de um agente de IA que realiza consultas em um banco de dados. O banco de dados utilizado é o `employees`, que contém uma tabela com as colunas `id`, `name` e `salary`.

## Pré-requisitos

- Python 3.x
- MySQL ou outro banco de dados compatível com `pymysql`
- Bibliotecas Python listadas no `requirements.txt`

## Instruções

### 1. Configuração do banco de dados

#### Criar o banco de dados e a tabela `employees`

1. Conecte-se ao seu servidor MySQL (ou outro banco de dados compatível).
2. Execute o seguinte comando SQL para criar o banco de dados e a tabela:

```sql
CREATE DATABASE employees;

USE employees;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    department VARCHAR(100) NOT NULL,
    gender VARCHAR(100) NOT NULL,
    date_start_contract (DATE) NOT NULL

);

```
3. Dados para popular o Banco de dados:
```
INSERT INTO employees (name, salary, department, gender, date_start_contract) VALUES
('Carlos Mateus', 350000, 'TI', 'Masculino', '2021-05-12'),
('Ana Joaquim', 250000, 'Recursos Humanos', 'Feminino', '2022-01-15'),
('Joaquim António', 450000, 'Financeiro', 'Masculino', '2020-09-30'),
('Rosa Maria', 200000, 'Marketing', 'Feminino', '2023-03-10');

```

3. requirements.txt:
   ```
   streamlit
   langchain
   pymysql
   langchain-community
   ```


4. Install requirements :
   ```
   pip install -r requirements.txt
   ```
