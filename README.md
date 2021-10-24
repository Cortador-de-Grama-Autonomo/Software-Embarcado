# Eletronica-Embarcado
Repositório de Desenvolvimento dos Códigos de Conexão com os Sensores

## Requisitos:
* ROS Noetic

## Pacotes:
* Controle_Locomocao: Implementação do código de controle e dos nós de comunicação para movimento do robô cortador de grama.
* Controle_Corte:Implementação do código de controle da altura e velocidade do corte da grama.
* Sensores: Biblioteca de códigos para obtenção de dados dos sensores.
* worlds: Ambientes para simulação
* cortador_description: Descrição do cortador para simulação

## Por onde começar:
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




