# LEITOR DE GABARITO OMR COM VISÃO COMPUTACIONAL

### Descrição 📝
Este projeto é um sistema de leitura automática de gabaritos baseado em marcação óptica (OMR), desenvolvido em Python com FastAPI e OpenCV. Ele converte PDFs de provas em imagens, identifica as áreas marcadas, extrai as respostas dos alunos e realiza a correção automática comparando com o gabarito oficial.

# Funcionabilidades ⚙
- Upload de arquivos PDF com respostas de gabaritos.
- Conversão automática de PDF para imagem.
- Detecção e recorte de colunas de respostas e matrícula.
- Extração de marcações preenchidas.
- Comparação com gabarito e retorno do resultado.
- API em FastAPI para integração com sistemas externos.

# Técnologias Utilizadas 💻
- Python 3.10+
- FastAPI
- OpenCV
- NumPy
- pdf2image
- Uvicorn

# Instalação 📘
### Clone o repositório
```
git clone https://github.com/joaosaiko/leitor-de-gabairto-OMR.git

cd leitor-de-gabairto-OMR
```
### Crie um ambiente virtual (Opcional pois já está criado no projeto, caso haja problema crie novamente)
```
python -m venv venv

source venv/bin/activate  # Linux/macOS

venv\Scripts\activate     # Windows
```
### Instale as dependências (Dentro do VsCode ou IDE que esteja utilizando, abra o terminal e cole o comando abaixo)
```
pip install -r requirements.txt
```
# Como usar 💭
### Execute o servidor FastAPI (No terminal da IDE utilizada)
```
uvicorn OMR_MAIN:app --reload
```
### Acesse a documentação da API no seu navegador em:
```
http://127.0.0.1:8000/docs
```
# Observação 📌
este projeto está em desenvolvimento e constante aprimoramento, erros podem ocorrer e para evitá-los considere as seguintes dicas.
- A precisão da leitura depende da qualidade da digitalização.
- É necessário manter o padrão dos modelos de gabarito para detecção correta outros modelos precisará de alterações na estrutura do algoritmo.
- O sistema ainda não lida com múltiplas páginas por PDF apenas com o modelo atual que conta com uma página.


