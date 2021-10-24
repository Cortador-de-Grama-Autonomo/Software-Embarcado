# Software-Embarcado

Repositório de Desenvolvimento dos Códigos de Software embarcados, para comunicação com os sensores e envio de informações para a API.
## Sumário

* [Dependências](#Dependências)
* [Manual de Instalação](#Manual-de-Instalação)
* [Guia de Contribuição](#Guia-de-Contribuição)
    * [Issues](#Issues)
    * [Branches](#Branches)
    * [Commits](#Commits)
    * [Pull Requests](#Pull-Requests)
* [Licença](#Licença)
* [Código de Conduta](#Código-de-Conduta)

## [**Dependências**](#Sumário)

Para a execução local da Wiki do projeto serão necessárias as seguintes dependências:

* [ROS Noetic]()

## [**Manual de Instalação**](#Sumário)

### Pacotes:
* Controle_Locomocao: Implementação do código de controle e dos nós de comunicação para movimento do robô cortador de grama.
* Controle_Corte:Implementação do código de controle da altura e velocidade do corte da grama.
* Sensores: Biblioteca de códigos para obtenção de dados dos sensores.
* worlds: Ambientes para simulação
* cortador_description: Descrição do cortador para simulação

### Instalação de Dependências

- Passo 1: Criar um diretório do projeto e fazer o download do repositório
```bash
  mkdir -p ~/Eletronica-Embarcado/
  cd ~/Eletronica-Embarcado/
  git clone https://github.com/Cortador-de-Grama-Autonomo/Eletronica-Embarcado.git
```

- Passo 2: Compilar os workspaces

```bash
  cd ~/Eletronica-Embarcado/Eletronica-Embarcado/catkin_ws
  catkin_make
  cd ~/Eletronica-Embarcado/Eletronica-Embarcado/simulation_ws
  catkin_make
```
### Execução

Para executar o repositório de documentação é necessários os seguintes passos:

```bash
# 1. Clone o repositório atual
$ git clone https://github.com/fga-eps-mds/2021.1-Cartografia-social-docs

# 2. Entre na página src do repositório
$ cd 2021.1-Cartografia-social-docs/src/

# 3. Install as dependências
$ npm install

# 4. Execute o projeto
$ npm run dev
```

Após a execução dos passos anteriores, o projeto de documentação será servido localmente, podendo, em geral, ser acessado através da URL:

```http
http://localhost:8080/2021.1-Cartografia-social-docs/
```

## [**Guia de Contribuição**](#Sumário)

Para a contribuição e evolução das informações presentes nesse repositório, o seguinte guia de contribuição foi criado, especificando instruções de uso e dos padrões utilizados.

### [**Issues**](#Sumário)

As issues devem ser criadas conforme template predefinido, contendo:

* ***Descrição*** - Descrição simples e direta do problema que a issue busca resolver ou da adição da issue;

* ***Tarefas*** - *Checklist* trazendo o passo a passo granularizado de como a issue deve ser executada, permitindo que cada tarefa seja marcada quando concluída;

* ***Critérios de Aceitação*** - *Checklist* do funcionamento ou resultado esperado após a conclusão da issue de forma satisfatória, permitindo que cada critério seja marcado quando concluído;

* ***Issue Vinculada*** - Referência a outra issue que esteja vinculada à issue presente, com link para a issue referenciada. Caso não haja issue, deve ser preenchido como 'Não se aplica.' somente;

* ***Assignees*** - As issues criadas devem ser atribuídas a um membro para execução, se houver alguém responsável por realizá-la;

* ***Labels*** - As issues criadas devem conter labels que categorizem aquela issue, para informar aos demais contribuidores sobre a natureza de seu conteúdo;

* ***Sprint*** - As issues devem possuir a sprint a qual se referem no campo destinado;

* ***Estimate*** - As issues devem ser pontuadas conforme seu grau de dificuldade;

