# 🧠 ORM_Main - Correção Automatizada de Gabaritos com FastAPI e OpenCV

Este sistema realiza a correção automática de gabaritos de múltipla escolha a partir de arquivos PDF escaneados. Utiliza tecnologias de visão computacional com OpenCV, conversão de PDF com `pdf2image`, API com FastAPI, e processamento assíncrono para gerar resultados rápidos, precisos e temporários.

---

## 📌 Visão Geral

A aplicação:

1. Recebe um arquivo PDF contendo um gabarito preenchido.
2. Converte o PDF em imagem.
3. Detecta automaticamente os campos marcados com caneta ou lápis (respostas e matrícula).
4. Compara as respostas com um gabarito oficial.
5. Retorna um JSON e CSV com os resultados.
6. Apaga os arquivos temporários após 6 minutos.

---

## 🚀 Como Usar
### Clonar repositorio com git bash
```bash
git clone https://github.com/joaosaiko/leitor-de-gabarito-OMR.git
```
> ⚠️ Após clonar o repositório abra-o no VScode, certique de possua todas os requisitos necessario para a execução em Python.

---

### Instalar dependências necessárias:

```bash
pip install -r requirements.txt
```
> ⚠️ Importante: Para a biblioteca pdf2image funcionar corretamente, o Poppler deve ser baixado e adicionado ao disco local C:/ nas variáveis do ambiente do Win ou intalado via terminal em quaisquer linux de base Debian ou Arch Linux.

---

## 📦 Dependências utilizadas
- fastapi
- uvicorn
- opencv-python
- numpy
- pdf2image
- python-multipart
- uuid
- aspose-words
- time
- threading
- tempfile
- json
- os

---

## 📂 Estrutura de Arquivos e Pastas
```bash
1. C:\appprointer - pasta criada ao executar o código pela primeira vez.

2. C:\appprointer\app - subpasta dentro da pasta principal criada.

3. C:\appprointer\app\data - localizada duas pastas importantes, sendo "PDF" aonde é colocado o pdf na qual será analisado e "Processados" aonde fica todos PDF dos gabaritos processados.
```

---

## 🧠 Explicações Técnicas

- Adicionar o modelo de gabarito marcado e digitalizado em PDF na pasta localizada em C:\appprointer\app\data\PDF
- No Vscode, abrir a pasta do projeto, no terminal executar o comando python códigoservidor.py 123 nome_do_gabarito_pdf
- será inciado o processo de conversão de PDF para imagem com _pdf2image.convert_from_path._
- Usará _cv2.Canny_ e _cv2.findContours_ para localizar retângulos (áreas marcadas).
- Classifica os retângulos: o primeiro identificado é assumido como a matrícula, os demais como colunas de questões.
- Cada coluna é cortada em blocos (1 bloco por questão) e cada questão é dividida horizontalmente em 5 partes (A, B, C, D, E).
- A alternativa marcada é a que tiver maior agrupamento de pixel brancos, as que possuírem marcação são reconhecidas como 1 e as que não possuí são reconhecidass como 0.

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
- O bloco com maior agrupamento de pixels em branco é considerado o número marcado.
- Se nenhum bloco ultrapassar o limiar, considera como "não marcado" e adicionado "_" como sinal de que não foi possivel identificar o campo marcado.

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

