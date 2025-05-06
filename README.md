# 🧠 ORM_Main - Correção Automatizada de Gabaritos com FastAPI e OpenCV

Este sistema realiza a correção automática de gabaritos de múltipla escolha a partir de arquivos PDF escaneados. Utiliza tecnologias de visão computacional com OpenCV, conversão de PDF com `pdf2image`, API com FastAPI, e processamento assíncrono para gerar resultados rápidos, precisos e temporários.

---

## 📌 Visão Geral

A aplicação:

1. Recebe um arquivo PDF contendo um gabarito preenchido.
2. Converte o PDF em imagem.
3. Detecta automaticamente os campos marcados com caneta ou lápis (respostas e matrícula).
4. Compara as respostas com um gabarito oficial.
5. Retorna um JSON com os resultados.
6. Apaga os arquivos temporários após 10 minutos.

---

## 🚀 Como Usar

### ▶️ Subir o servidor

```bash
uvicorn ORM_Main:app --reload
```
### ▶️ Depois, acesse:

```bash
http://localhost:8000/docs
```

---

## 📦 Dependências
- fastapi
- uvicorn
- opencv-python-headless
- numpy
- pdf2image
- uuid

### Instalar:

```bash
pip install fastapi uvicorn opencv-python-headless numpy pdf2image
```
> ⚠️ Importante: Para pdf2image funcionar corretamente, o Poppler deve estar instalado. Guia de instalação (Windows)

---

## 📂 Estrutura de Arquivos Temporários
```bash
temp/
└── <session_id>/
    ├── jpeg/         # Página convertida do PDF em imagem
    ├── cutouts/      # Imagens cortadas com blocos de respostas
    ├── matricula/    # Imagem da matrícula marcada
    ├── json/         # Respostas detectadas e resultado corrigido
```

---

## 🔍 Rotas da API

POST /process-pdf
Faz todo o processamento: conversão, detecção, correção e resposta final.

Requisição:
- Multipart/form-data com campo _file_ (PDF).

Resposta:
```bash
{
  "resultado": { ... },
  "session_id": "uuid",
  "mensagem": "Resultado disponível por 10 minutos"
}
```

GET /resultado/{session_id}
Retorna o JSON corrigido, se ainda não tiver expirado.

---

## 🧠 Explicações Técnicas

process_pdf(file: UploadFile)
- Cria pastas temporárias com UUID.
- Converte PDF para imagem com _pdf2image.convert_from_path._
- Usa _cv2.Canny_ e _cv2.findContours_ para localizar retângulos (áreas marcadas).
- Classifica os retângulos: o maior é assumido como a matrícula, os demais como colunas de questões.
- Cada coluna é cortada em blocos (1 bloco por questão) e cada questão é dividida horizontalmente em 5 partes (A, B, C, D, E).
- A alternativa marcada é a que tiver mais pixels escuros.

---

## 📘 Função: detect_marked_choice(thresh_question)
```bash
def detect_marked_choice(thresh_question):
```

- Divide cada questão em 5 colunas verticais.
- Conta os pixels escuros em cada coluna.
- Marca como resposta a coluna com maior preenchimento (desde que tenha destaque claro).

---

## 📘 Função: detect_marked_matricula(thresh_matricula)

```bash
def detect_marked_matricula(thresh_matricula):
```

Divide a imagem da matrícula em 8 colunas (1 por dígito).

- Cada coluna é dividida em 10 blocos horizontais (de 0 a 9).
- O bloco com mais pixels escuros é considerado o número marcado.
- Se nenhum bloco ultrapassar o limiar, considera como "não marcado".

---

## 📘 Função: grade_answers(detected_answers, answer_key)
Local: _utils.py_

- Compara as respostas detectadas com o gabarito oficial.
- Classifica cada questão como:
- _correct_ se a resposta for igual ao gabarito
- _incorrect_ se for diferente
- _blank_ se nenhuma marcação foi detectada
- Gera um resumo com:
- Total de acertos
- Total de erros
- Total de questões em branco
- Porcentagem de acerto

## 📚 Explicação do utils.py

```bash
def findRectContours(contours): ...
```

- Filtra contornos que formam retângulos, ignorando ruídos pequenos.

```bash
def reorder(points): ...
```

- Reordena os 4 pontos de um retângulo para garantir consistência na leitura (cima/esquerda → baixo/direita).

```bash
def grade_answers(...): ...
```

- Realiza a correção final, já explicada acima.

## ⏳ Limpeza Automática

Ao final do processamento, é iniciado um _threading.Thread_ com _sleep(300)_ para excluir automaticamente os arquivos temporários depois de 5 minutos.

```bash
threading.Thread(target=remove_folder_later, daemon=True).start()
```

---

## 💡 Observações e Boas Práticas

- O código está modularizado para permitir expansão futura.
- O gabarito pode ser facilmente extraído de um JSON externo.
- A lógica de corte usa divisão proporcional, então o layout da folha deve ser bem padronizado.
- A detecção da matrícula pode ser sensível a sombras e escaneamentos ruins. Evite imagens borradas.
- O sistema atual só processa a primeira página do PDF. Ideal para provas de uma folha.

# 📌 Possibilidades Futuras
- Armazenamento em banco de dados
- Interface web para upload e download dos resultados
- Ajuste automático de gabaritos
- Leitura multi-página
- Módulo OCR para validar matrícula com texto
- aplicação de IA facilmente

## 🧑‍💻 Autor
Este projeto foi desenvolvido para uso educacional e institucional no Centro Universitário Santa Terezinha - CEST, com o objetivo de automatizar correções de provas de forma confiável, modular e extensível.

