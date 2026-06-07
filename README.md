# SentimentAI — Plataforma Inteligente de Análise de Sentimentos

Uma aplicação moderna desenvolvida com Python, FastAPI, Pandas e mongoDB para análise, monitoramento e visualização de sentimentos em textos. O sistema permite que usuários submetam textos para processamento e obtenham insights emocionais através de dashboards interativos, métricas estatísticas e histórico de análises.

---

## 📌 Visão Geral

O SentimentAI foi criado para auxiliar na identificação e interpretação de emoções expressas em conteúdos textuais, possibilitando a construção de soluções voltadas para:

•
Atendimento ao cliente: Compreender o sentimento dos clientes em interações e feedbacks.

•
Monitoramento de redes sociais: Acompanhar a percepção da marca e tendências de opinião pública.

•
Pesquisa de satisfação: Avaliar o nível de satisfação de usuários e consumidores.

•
Experiência do usuário (UX): Obter insights sobre a experiência do usuário com produtos e serviços.

•
Análise de feedbacks: Processar e categorizar grandes volumes de feedback.

•
Estudos acadêmicos: Apoiar pesquisas em Inteligência Artificial e Processamento de Linguagem Natural (NLP).

A plataforma foi projetada para ser facilmente integrada a APIs externas ou modelos próprios de Machine Learning.

---

# 🚀 Funcionalidades

## 📝 Análise de Sentimentos

•
Inserção de textos para análise.

•
Classificação automática do sentimento.

•
Exibição de resultados em tempo real.

•
Interface intuitiva e responsiva.

### Categorias suportadas:

•
😀 Positivo

•
😐 Neutro

•
😞 Negativo

---

## 📊 Dashboard Analítico

Painel visual com métricas detalhadas:

•
Quantidade total de análises realizadas.

•
Distribuição de sentimentos.

•
Tendências e comportamento emocional.

•
Estatísticas agregadas.


## 📚 Histórico de Análises

Permite consultar análises realizadas anteriormente:

•
Texto analisado

•
Resultado obtido

•
Data da análise

•
Métricas associadas

---

# 🛠️ Tecnologias

## Frontend

•
Next.js: Framework React para aplicações web.

•
TypeScript: Linguagem de programação que adiciona tipagem estática ao JavaScript.

•
Recharts: Biblioteca de gráficos para React.

•
Tailwind CSS: Framework CSS utilitário para estilização rápida.

•
Shadcn/UI: Componentes de UI construídos com Radix UI e Tailwind CSS.

•
Radix UI: Primitivas de UI sem estilo para construir sistemas de design acessíveis.

•
Lucide React: Biblioteca de ícones para React.

---

## Backend

•
Python: Linguagem de programação principal.

•
FastAPI: Framework web moderno e rápido para construir APIs.

•
Pandas: Biblioteca para análise e manipulação de dados.

•
OpenAI: Utilizado para aspectos emocionais e processamento de linguagem natural.

Banco de Dados

•
MongoDB (Opcional): Um banco de dados NoSQL, flexível e escalável, pode ser utilizado para persistência dos dados de análise e histórico.

---
# 📂 Estrutura do Projeto

```txt
sentiment-ai/
│
├── data/
│   ├── olist_order_reviews_dataset.csv
│   └── reviews_tratados.csv
│
├── models/
│   └── sentiment_model.pkl
│
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── config.py
│   ├── database.py
│   ├── openai_emotion_service.py
│   ├── predict.py
│   ├── preprocessing.py
│   └── train_baseline.py
│
├── tests/
│   ├── test_api.py
│   └── test_api_mock.py
│
├── .env
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Descrição das pastas e arquivos

•
`data/`: armazena o dataset original e o dataset tratado após o pré-processamento.

•
`models/`: armazena o modelo treinado utilizado pela API para realizar as predições.

•
`src/`: contém o código principal do backend, incluindo API, pré-processamento, treinamento, predição, conexão com banco de dados e integração com OpenAI.

•
`tests/`: contém os testes automatizados da API, incluindo testes de rota, validação e uso de mocks.

•
`.env`: armazena variáveis de ambiente, como chave da OpenAI e string de conexão com o MongoDB.

•
`.gitignore`: define arquivos e pastas que não devem ser enviados para o repositório.

•
`pytest.ini`: configura o ambiente de testes com Pytest.

•
`requirements.txt`: lista as dependências necessárias para executar o projeto.

•
`README.md`: documentação principal do projeto.

## Principais arquivos do backend

•
`api.py`: define as rotas da API, incluindo `/predict` e `/analyses`.

•
`config.py`: centraliza caminhos do projeto e variáveis de ambiente.

•
`database.py`: configura a conexão com o MongoDB.

•
`openai_emotion_service.py`: realiza a análise de aspectos emocionais usando a API da OpenAI.

•
`predict.py`: carrega o modelo treinado e executa predições pelo terminal.

•
`preprocessing.py`: realiza a limpeza dos dados e gera o dataset tratado.

•
`train_baseline.py`: treina o modelo baseline com TF-IDF e Regressão Logística.

# ⚙️ Instalação e Uso
---

## 1. Pré-requisitos

Antes de iniciar, é necessário ter instalado:

•
Python 3.10 ou superior

•
Git

•
MongoDB Atlas ou MongoDB local

•
Uma chave de API da OpenAI

•
Um editor de código, como VSCode

---

## 2. Clonar o projeto

Clone o repositório e acesse a pasta do projeto:

```bash
git clone <url-do-repositorio>
cd sentiment-ai
```

---

## 3. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux ou Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Instalar dependências

Com o ambiente virtual ativado, instale as dependências:

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` ainda não esteja configurado, instale manualmente as principais bibliotecas:

```bash
pip install pandas numpy scikit-learn joblib fastapi uvicorn openai python-dotenv pymongo pytest httpx
```

---

## 5. Configurar variáveis de ambiente

Crie um arquivo chamado `.env` na raiz do projeto.

Exemplo:

```env
OPENAI_API_KEY=sua_chave_da_openai
MONGO_URI=sua_string_de_conexao_mongodb
MONGO_DB_NAME=sentiment_analysis_db
```

A variável `OPENAI_API_KEY` é utilizada para a análise de aspectos emocionais do texto.

A variável `MONGO_URI` é utilizada para conectar a API ao MongoDB e salvar o histórico das análises.

A variável `MONGO_DB_NAME` define o nome do banco de dados utilizado pela aplicação.

Importante: o arquivo `.env` não deve ser enviado para o GitHub.

Recomenda-se adicionar ao `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
models/*.pkl
data/*.csv
```

---

## 6. Adicionar o dataset

O projeto utiliza o dataset de avaliações da Olist.

Adicione o arquivo:

```txt
olist_order_reviews_dataset.csv
```

dentro da pasta:

```txt
data/
```

A estrutura esperada é:

```txt
data/
└── olist_order_reviews_dataset.csv
```

---

## 7. Pré-processar os dados

Execute o script de pré-processamento:

```bash
python -m src.preprocessing
```

Essa etapa realiza:

•
Leitura do dataset original;

•
Concatenação do título e comentário da avaliação;

•
Remoção de textos vazios;

•
Criação dos rótulos de sentimento com base na nota da avaliação;

•
Geração do arquivo tratado.

Após a execução, será criado o arquivo:

```txt
data/reviews_tratados.csv
```

---

## 8. Treinar o modelo

Após o pré-processamento, execute o treinamento do modelo:

```bash
python -m src.train_baseline
```

Essa etapa treina um modelo de classificação de sentimentos utilizando TF-IDF e Regressão Logística.

O modelo treinado será salvo em:

```txt
models/sentiment_model.pkl
```

---

## 9. Testar predição pelo terminal

Para testar o modelo diretamente pelo terminal, execute:

```bash
python -m src.predict
```

Digite uma avaliação quando solicitado.

Exemplo:

```txt
Produto chegou atrasado e veio com defeito
```

O sistema retornará o sentimento previsto e as probabilidades associadas às classes.

---

## 10. Executar a API

Para iniciar a API com FastAPI, execute:

```bash
uvicorn src.api:app --reload
```

A API ficará disponível em:

```txt
http://127.0.0.1:8000
```

A documentação interativa pode ser acessada em:

```txt
http://127.0.0.1:8000/docs
```

---

## 11. Testar o endpoint de análise

Endpoint:

```txt
POST http://127.0.0.1:8000/predict
```

Exemplo de body JSON:

```json
{
  "texto": "Produto chegou atrasado e veio com defeito"
}
```

Também é possível enviar o campo como `text`:

```json
{
  "text": "Produto chegou atrasado e veio com defeito"
}
```

Exemplo de resposta:

```json
{
  "texto": "Produto chegou atrasado e veio com defeito",
  "sentimento": "negativo",
  "confianca": 0.87,
  "probabilidades": {
    "negativo": 0.87,
    "neutro": 0.08,
    "positivo": 0.05
  },
  "aspectos_detectados": [
    {
      "nome": "frustração",
      "intensidade": 80,
      "evidencia": "chegou atrasado e veio com defeito"
    }
  ],
  "created_at": "2026-05-29T16:30:19.896693+00:00"
}
```

---

## 12. Consultar histórico de análises

Caso o MongoDB esteja configurado corretamente, é possível consultar as análises salvas:

```txt
GET http://127.0.0.1:8000/analyses
```

Esse endpoint retorna as últimas análises registradas no banco de dados.

---
Comandos principais:

```bash
python -m src.preprocessing
python -m src.train_baseline
uvicorn src.api:app --reload
pytest -v
```


## 🤝 Contribuição

O projeto **Sentimental** foi desenvolvido de forma colaborativa por uma equipe multidisciplinar com foco em Inteligência Artificial, Processamento de Linguagem Natural (NLP), Desenvolvimento Web e Visualização de Dados.

## Integrantes

* Allan Marques
* Emerson Costa
* Felipe Pimentel
* Gabriel Martins
* Heloisa Costa
* Ricardo Tompson
* Walison Brandão

## 📄 Licença

Informações sobre a licença do projeto serão adicionadas aqui.

