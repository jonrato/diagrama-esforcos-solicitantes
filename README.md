# 📐 Gerador de Diagramas NVM (Normal, Cortante e Momento)

Este projeto é uma aplicação **Streamlit** desenvolvida como parte do **projeto semestral da disciplina PEF3208 - Fundamentos de Mecânica das Estruturas**.

A aplicação permite ao usuário gerar e visualizar os diagramas de esforços internos (Normal, Cortante e Momento Fletor) para diferentes configurações clássicas de vigas submetidas a carregamentos mecânicos.

O projeto encontra-se no ar no seguinte link: https://diagrama-esforcos-solicitantes.streamlit.app/


---

## 🧮 Casos disponíveis

1. Viga em balanço com carga concentrada na extremidade  
2. Viga biapoiada com carga concentrada no meio  
3. Viga biapoiada com carga distribuída uniforme  
4. Viga engastada com carga triangular crescente  

---

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/jonrato/diagrama-esforcos-solicitantes
cd seu-repositorio

python3 -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

streamlit run main.py
```

## 📦 Estrutura do Projeto
```
.
├── main.py                   # Interface principal em Streamlit
├── casos/                  # Códigos de cada cenário
│   ├── viga_balcao_concentrada.py
│   ├── viga_biapoiada_concentrada.py
│   ├── viga_biapoiada_distribuida.py
│   └── viga_engastada_triangulo.py
├── requirements.txt
└── .gitignore
```