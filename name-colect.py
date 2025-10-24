import os
import pdfplumber
import csv

def aggressive_extract(pdf_path):
    """Extrai todas as linhas e tenta identificar padrões"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = pdf.pages[0].extract_text() or ""
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            
            print(f"\n=== {os.path.basename(pdf_path)} ===")
            for i, line in enumerate(lines):
                print(f"Linha {i}: {line}")
            
            # Pega as primeiras linhas que não são metadata
            candidate_lines = []
            for line in lines:
                if (len(line) > 3 and 
                    not any(word in line.lower() for word in ['tcpdf', 'powered', 'horas', 'concluído']) and
                    not line.replace('/', '').isdigit() and  # Não é data
                    not line.replace('h', '').replace(' ', '').isdigit()):  # Não é hora
                    candidate_lines.append(line)
            
            nome_aluno = candidate_lines[0] if candidate_lines else "NÃO ENCONTRADO"
            nome_curso = candidate_lines[1] if len(candidate_lines) > 1 else "NÃO ENCONTRADO"
            
            print(f"→ Aluno: {nome_aluno}")
            print(f"→ Curso: {nome_curso}")
            
            return nome_aluno, nome_curso
            
    except Exception as e:
        print(f"Erro: {e}")
        return "ERRO", "ERRO"

# Usar este
pasta_pdfs = "certificados"
arquivo_saida = "certificados_final.csv"

pdf_files = [f for f in os.listdir(pasta_pdfs) if f.lower().endswith('.pdf')]

with open(arquivo_saida, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Arquivo', 'Nome_Aluno', 'Nome_Curso'])
    
    for pdf_file in pdf_files:
        caminho = os.path.join(pasta_pdfs, pdf_file)
        nome, curso = aggressive_extract(caminho)
        writer.writerow([pdf_file, nome, curso])

print(f"✅ Finalizado! {len(pdf_files)} arquivos em {arquivo_saida}")
