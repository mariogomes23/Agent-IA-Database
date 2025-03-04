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
    salary DECIMAL(10, 2) NOT NULL
);

```
3. Dados para popular o Banco de dados:
```
INSERT INTO employees (name, salary) VALUES
('João Silva', 4500.00),
('Maria Oliveira', 5200.00),
('Carlos Souza', 3800.00),
('Ana Costa', 6100.00),
('Pedro Rocha', 4900.00),
('Lucia Mendes', 5400.00),
('Fernando Alves', 4700.00),
('Patricia Lima', 5800.00),
('Ricardo Santos', 4200.00),
('Mariana Gomes', 5300.00);

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
