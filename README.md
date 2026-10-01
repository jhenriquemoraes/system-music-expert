# System Music Expert

Sistema especialista baseado em regras desenvolvido em Python para auxiliar usuários com pouco ou nenhum conhecimento de teoria musical na escolha de progressões harmônicas.

O sistema recebe características desejadas pelo usuário, como sensação, caráter, sonoridade e nível de complexidade, e utiliza uma base de conhecimento para recomendar um contexto harmônico, uma progressão e os acordes correspondentes.

## Objetivo

O objetivo do projeto é aplicar conceitos de **Inteligência Artificial e Sistemas Especialistas**, representando conhecimento musical por meio de regras e utilizando um motor de inferência para produzir recomendações.

O escopo foi delimitado à **harmonia**, funcionando como um ponto de partida para composição musical.

O sistema não busca gerar uma música completa e não contempla elementos como:

- melodia;
- letra;
- ritmo;
- arranjo;
- instrumentação;
- produção musical.

## Funcionamento

O usuário informa:

- nota inicial;
- sensação desejada;
- caráter da música;
- preferência de sonoridade;
- nível de complexidade.

Essas informações são transformadas em fatos e processadas pelo motor de inferência.

O fluxo geral pode ser representado como:

```text
Entradas do usuário
        ↓
       Fatos
        ↓
Base de conhecimento
        ↓
Motor de inferência
        ↓
Progressão selecionada
        ↓
Conversão musical
        ↓
Recomendação
```

Como resultado, o sistema apresenta:

- contexto harmônico;
- nível de complexidade;
- progressão em graus;
- acordes sugeridos;
- explicação da recomendação.

## Sistema Especialista

A base de conhecimento atual possui **30 regras**, responsáveis por representar decisões relacionadas a:

- contexto maior e menor;
- intenção musical;
- estabilidade e tensão;
- resolução harmônica;
- funções harmônicas;
- relativo menor;
- seleção de progressões;
- nível de complexidade;
- contextos Mixolídio e Lídio;
- tratamento de informações insuficientes;
- regras gerais e de fallback.

O sistema utiliza **forward chaining (encadeamento para frente)**.

A inferência começa a partir dos fatos conhecidos, fornecidos pelo usuário. As regras cujas condições são satisfeitas podem produzir ou modificar fatos, permitindo que outras regras sejam posteriormente aplicadas.

O processo continua enquanto existirem alterações relevantes no estado do sistema.

## Evolução da base de conhecimento

A primeira modelagem do domínio chegou a aproximadamente **48 regras**.

Durante a revisão, identificamos redundâncias e situações em que cálculos musicais determinísticos estavam sendo representados como regras do sistema especialista.

Após a separação dessas responsabilidades, a base foi reduzida para **22 regras**.

Em seguida, foram realizados **testes de mesa**, simulando diferentes combinações de fatos e acompanhando o comportamento esperado das inferências.

Esses testes revelaram lacunas relacionadas, entre outros pontos, à definição de contexto, situações com informações insuficientes, preservação de decisões mais específicas, contextos modais e seleção entre progressões candidatas.

A partir desses casos, a base foi refinada até chegar às **30 regras atuais**.

## Inferência e processamento musical

O projeto diferencia dois tipos de conhecimento.

### Conhecimento especialista

Responsável pelas decisões do sistema, como:

```text
SE a intenção for energética
E o usuário aceitar uma sonoridade menos convencional
E o caráter base for maior
ENTÃO considerar o contexto Mixolídio.
```

Essas decisões são processadas pelo motor de inferência.

### Processamento musical determinístico

Algumas operações musicais não precisam ser representadas como regras de inferência.

Entre elas:

- construção de escalas;
- construção de campos harmônicos;
- formação de acordes;
- conversão de graus em acordes;
- utilização de tríades ou tétrades.

Por exemplo:

```text
Progressão:
I – V – vi – IV

Contexto:
C Maior

Resultado:
C – G – Am – F
```

Essa separação evita a criação de regras redundantes para todas as combinações possíveis de tonalidades e acordes.

## Contextos harmônicos

O sistema trabalha atualmente com quatro contextos principais:

### Maior

Utilizado para características associadas ao campo harmônico maior.

Exemplo:

```text
I – V – vi – IV
```

### Menor

Utilizado para características associadas ao campo harmônico menor.

Exemplo:

```text
i – VI – III – VII
```

Também pode utilizar uma dominante maior quando uma resolução mais clara for necessária:

```text
i – iv – V – i
```

### Mixolídio

Pode ser inferido para determinadas combinações relacionadas a uma intenção energética e aberta.

Uma das progressões utilizadas é:

```text
I – ♭VII – IV – I
```

### Lídio

Pode ser inferido para determinadas combinações relacionadas a uma intenção contemplativa e aberta.

Uma das progressões utilizadas é:

```text
I – II – I – II
```

O usuário não precisa conhecer previamente esses modos. A intenção é que o sistema traduza preferências descritas em linguagem mais acessível para conceitos musicais internos.

## Progressões disponíveis

A base possui atualmente oito progressões principais:

| ID | Contexto | Progressão |
|---|---|---|
| P1 | Maior | I – V – vi – IV |
| P2 | Maior | vi – IV – I – V |
| P3 | Maior | I – IV – V – I |
| P4 | Maior | ii – V – I |
| P5 | Mixolídio | I – ♭VII – IV – I |
| P6 | Menor | i – VI – III – VII |
| P7 | Menor | i – iv – V – i |
| P8 | Lídio | I – II – I – II |

A escolha entre essas progressões depende dos fatos produzidos durante a inferência.

## Níveis de complexidade

O sistema possui dois níveis de complexidade.

### Simples

Prioriza tríades e progressões acessíveis.

Exemplo em C Maior:

```text
C – G – Am – F
```

### Intermediário

Permite acordes com sétima e uma sonoridade harmonicamente mais elaborada.

Exemplo:

```text
Cmaj7 – G7 – Am7 – Fmaj7
```

## Interface

A aplicação possui uma interface gráfica simples desenvolvida com **Tkinter**.

O usuário pode selecionar:

1. nota inicial;
2. sensação desejada;
3. caráter;
4. sonoridade;
5. complexidade.

Após selecionar as opções, basta clicar em **Gerar sugestão**.

A interface apresenta a recomendação produzida pelo sistema especialista e uma breve explicação sobre a escolha.

## Estrutura do projeto

```text
music_expert/
│
├── main.py
│
├── ui/
│   ├── __init__.py
│   └── app.py
│
├── engine/
│   ├── __init__.py
│   ├── inference_engine.py
│   ├── harmony_converter.py
│   └── music_expert_service.py
│
├── knowledge/
│   ├── __init__.py
│   ├── rules.py
│   ├── progressions.py
│   └── harmony.py
│
├── models/
│   ├── __init__.py
│   ├── facts.py
│   └── recommendation_result.py
│
└── tests/
    ├── __init__.py
    ├── test_engine.py
    ├── test_harmony.py
    ├── test_harmony_converter.py
    ├── test_recommendation_result.py
    └── test_music_expert_service.py
```

## Tecnologias utilizadas

- Python 3
- Tkinter
- Pytest
- Git
- GitHub

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/jhenriquemoraes/system-music-expert.git
```

### 2. Entre na pasta do projeto

```bash
cd system-music-expert
```

### 3. Crie um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instale o Pytest para executar os testes

```bash
python -m pip install pytest
```

A aplicação utiliza Tkinter para a interface gráfica e não depende de frameworks web.

### 6. Execute a aplicação

```bash
python main.py
```

## Testes

Para executar toda a suíte de testes:

```bash
python -m pytest -v
```

Os testes verificam diferentes partes do sistema, incluindo:

- motor de inferência;
- contextos harmônicos;
- escalas;
- campos harmônicos;
- progressões;
- conversão de graus para acordes;
- contexto maior;
- contexto menor;
- Mixolídio;
- Lídio;
- nível simples;
- nível intermediário;
- tratamento de informações insuficientes;
- fluxo completo de recomendação.

Os testes automatizados complementam os testes de mesa utilizados durante a construção e refinamento da base de conhecimento.

## Exemplo de utilização

Considere as seguintes escolhas:

```text
Nota inicial: G
Sensação: Energética e aberta
Caráter: Claro / aberto
Sonoridade: Pode ser um pouco diferente
Complexidade: Simples
```

O sistema pode produzir:

```text
Contexto harmônico: Mixolídio
Progressão: I – ♭VII – IV – I
Acordes sugeridos: G – F – C – G
```

Nesse cenário, as características informadas permitem ao sistema inferir um contexto Mixolídio sem exigir que o usuário conheça previamente esse conceito.

## Limitações

O projeto possui finalidade acadêmica e trabalha com um domínio musical deliberadamente limitado.

Entre as limitações atuais estão:

- não gera melodias;
- não gera letras;
- não define ritmo ou andamento;
- não produz arranjos;
- não substitui decisões criativas do compositor;
- trabalha com um conjunto limitado de contextos e progressões;
- não pretende representar toda a teoria harmônica existente.

As recomendações devem ser interpretadas como **pontos de partida para composição**, e não como a única solução musical possível.

## Contexto acadêmico

Projeto desenvolvido como trabalho prático da disciplina de **Inteligência Artificial**, com foco no desenvolvimento de um **Sistema Especialista baseado em regras**.

O trabalho envolve:

- delimitação de um domínio;
- aquisição e representação do conhecimento;
- construção de regras SE–ENTÃO;
- motor de inferência;
- testes de mesa;
- testes automatizados;
- interface para interação;
- demonstração dos resultados.

## Considerações finais

O projeto demonstra como conhecimento especializado pode ser representado computacionalmente para auxiliar usuários na tomada de decisão.

A partir de informações simples fornecidas por um usuário leigo, o sistema aplica sua base de conhecimento, realiza inferências e transforma a decisão obtida em uma progressão de acordes utilizável musicalmente.

Dessa forma, o sistema estabelece uma ligação entre **preferências do usuário, representação do conhecimento, inferência e aplicação prática da teoria musical**.
