# PDF Name and Course Extractor

Um script Python robusto para extrair automaticamente nomes de alunos e cursos de certificados PDF em lote.

## 📋 Descrição do Projeto

Este projeto foi desenvolvido para automatizar o processo de extração de dados de certificados PDF em grande volume. Originalmente criado para processar 161 certificados do Senac, o script identifica e extrai automaticamente:

- **Nome do aluno** (geralmente na primeira linha relevante do PDF)
- **Nome do curso** (geralmente na segunda linha relevante do PDF)

Os dados extraídos são salvos em um arquivo CSV estruturado para fácil importação em planilhas, bancos de dados ou outras ferramentas de análise.

## 🚀 Funcionalidades

- ✅ **Extração de texto** de PDFs usando `pdfplumber` (mais robusto que PyPDF2)
- ✅ **Processamento em lote** de múltiplos arquivos
- ✅ **Filtragem inteligente** de linhas irrelevantes (datas, horas, metadata)
- ✅ **Saída em CSV** com codificação UTF-8 para caracteres especiais
- ✅ **Log detalhado** do processo de extração para debugging
- ✅ **Tratamento de erros** individual por arquivo

## 📦 Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/pdf-certificate-extractor.git
cd pdf-certificate-extractor
```

### 2. Crie um ambiente virtual (recomendado)

#### No Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### No Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install pdfplumber
```

### 🛠️ Configuração e Uso

1. Preparação dos arquivos

Crie uma pasta chamada certificados na raiz do projeto e coloque todos os PDFs dentro:

pdf-certificate-extractor/  
├── certificados/  
│   ├── certificado1.pdf  
│   ├── certificado2.pdf  
│   └── ...  
├── extract_certificates.py  
└── README.md  

2. Execução do script
```bash
python name-colect.py
```

3. Verificação do resultado

O script gerará:
Log no terminal: Mostrando o processamento de cada arquivo
Arquivo CSV: certificados_final.csv com os dados extraídos

📊 Estrutura do Arquivo de Saída

O CSV gerado contém três colunas:


Coluna	    |       Descrição	            |   Exemplo
------------|-------------------------------|--------------------------------------
Arquivo	    | Nome do arquivo PDF original  |   1178346064EF.pdf
Nome_Aluno  | Nome completo do aluno	    |   Emanuely Fiori
Nome_Curso	| Nome completo do curso	    | Escrita criativa para blogs e mídias digitais
------------|-------------------------------|--------------------------------------

#### 🔍 Funcionamento do Algoritmo

Estratégia de Extração "Agressiva"
O script utiliza uma abordagem chamada "extração agressiva" que:

- Extrai todo o texto de cada PDF
- Divide em linhas e remove espaços desnecessários

Filtra linhas irrelevantes baseado em palavras-chave:
- Metadata técnica: tcpdf, powered
- Informações de tempo: horas, concluído
- Datas e números
- Seleciona as primeiras linhas relevantes como nome e curso

#### ⚠️ Solução de Problemas

##### Problemas Comuns e Soluções

1. "NÃO ENCONTRADO" para todos os campos
- Verifique se os PDFs não estão protegidos por senha
- Teste com pdfplumber manualmente em um arquivo

2. Caracteres especiais incorretos
- O script usa UTF-8, mas alguns PDFs podem ter codificação diferente
- Verifique o encoding do texto extraído no log

3. Estrutura diferente do esperado
- Ajuste as palavras-chave no filtro na função aggressive_extract

#### Modo Debug
Para entender problemas, analise o log do terminal que mostra:

- Texto completo extraído de cada PDF
- Todas as linhas identificadas
- Linhas filtradas e resultado final

#### 🔗 Dependências
pdfplumber: Biblioteca para extração de texto de PDFs

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.