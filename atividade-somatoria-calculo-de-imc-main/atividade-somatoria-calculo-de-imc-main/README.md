# 🩺 Monitoramento de Saúde com Cálculo de IMC

Este projeto é uma aplicação simples em Python que ajuda o usuário a monitorar sua saúde com base no cálculo do IMC (Índice de Massa Corporal).

## 💡 Objetivo

Receber o **peso** e a **altura** do usuário, calcular o **IMC** e exibir:
- O valor calculado
- Uma mensagem de orientação baseada no resultado

## ⚙️ Itens críticos:

1. O usuário informa o **peso (kg)** e a **altura (m)**.
2. O programa calcula o IMC:

### IMC = peso / (altura ** 2)

3. O IMC é exibido junto com uma mensagem personalizada:
- IMC ≥ 30.0 → `Cuidado com a Saúde`
- IMC < 30.0 → `Tudo ok`

## 📊 Itens Desejáveis:

Você pode melhorar o programa utilizando a tabela abaixo para exibir classificações mais detalhadas:

| Faixa de IMC        | Classificação                  |
|---------------------|-------------------------------|
| < 18.5              | Abaixo do peso                 |
| 18.5 – 24.9         | Peso normal                    |
| 25.0 – 29.9         | Sobrepeso                      |
| 30.0 – 34.9         | Obesidade Grau I               |
| 35.0 – 39.9         | Obesidade Grau II              |
| ≥ 40.0              | Obesidade Grau III (mórbida)   |

## ✅ Critérios de Avaliação

### 🔴 Itens críticos (obrigatórios)
- Nome do repositório correto
- Código funcionando corretamente
- Entrega dentro do prazo

### ⚫ Itens desejáveis (valem pontos extras)
- O programa exibe:
- Nome do usuário
- Valor do IMC
- Classificação detalhada com base na tabela acima

## 🧠 Dica

- Entrada de dados com `input()`
- Conversão de tipos (`float`)
- Operadores aritméticos ( `divisão /`, `potência **`)
- Estrutura condicional com `if`, `elif`, `else`
  
## 🚀 Bora codar!

Este é um ótimo exercício para treinar entrada de dados, cálculos e estruturas condicionais no Python.

Contribuições e melhorias são bem-vindas!
