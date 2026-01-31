#!/bin/bash
set -euo pipefail

# Cria um CSV temporário para testes
cat > tmp_test.csv <<'CSV'
id,nome,email
1,Alice,alice@example.com
2,Bob,bob@example.com
2,Bob,bob@example.com
3,,charlie@example.com
CSV

# Compila os módulos Python
python -m compileall .

# Executa o script de limpeza
python main.py --input-file tmp_test.csv --output-file tmp_clean.csv --report-file tmp_report.txt --required-columns id,nome,email

echo "Script executado com sucesso. Saída gerada em tmp_clean.csv e relatório em tmp_report.txt"
