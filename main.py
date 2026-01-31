main.py"""
csv-data-cleaner
-----------------

Script em Python para limpeza básica de arquivos CSV. Remove registros
duplicados, verifica a presença de colunas obrigatórias e normaliza valores
textuais. Também gera um relatório simples de erros encontrados.

Utiliza a biblioteca pandas pela simplicidade e robustez no tratamento de
dados tabulares.
"""

import argparse
from pathlib import Path
from typing import List

import pandas as pd


def clean_csv(
    input_file: Path,
    output_file: Path,
    report_file: Path,
    required_columns: List[str],
) -> None:
    """Executa a limpeza do arquivo CSV e gera o relatório de erros."""
    df = pd.read_csv(input_file)
    errors: List[str] = []

    # Verifica se todas as colunas obrigatórias existem
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Colunas obrigatórias ausentes: {', '.join(missing_cols)}")

    # Remove linhas duplicadas
    num_duplicates = df.duplicated().sum()
    df = df.drop_duplicates().reset_index(drop=True)

    # Normaliza strings (remove espaços nas pontas e converte para minúsculas)
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip().str.lower()

    # Gera relatório de linhas com valores obrigatórios ausentes
    for idx, row in df.iterrows():
        missing_values = [col for col in required_columns if not str(row[col]).strip()]
        if missing_values:
            errors.append(f"Linha {idx + 1}: campos ausentes em {', '.join(missing_values)}")

    # Salva arquivo de saída
    df.to_csv(output_file, index=False)

    # Escreve relatório
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"Linhas duplicadas removidas: {num_duplicates}\n")
        for error in errors:
            f.write(error + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Limpa e normaliza um arquivo CSV.")
    parser.add_argument("--input-file", required=True, help="Caminho para o CSV de entrada")
    parser.add_argument("--output-file", required=True, help="Caminho do CSV limpo a ser gerado")
    parser.add_argument("--report-file", default="report.txt", help="Arquivo de relatório a ser gerado")
    parser.add_argument(
        "--required-columns",
        default="",
        help="Colunas obrigatórias separadas por vírgula (ex: id,nome,email)",
    )
    args = parser.parse_args()
    required_cols = [c.strip() for c in args.required_columns.split(",") if c.strip()] if args.required_columns else []
    clean_csv(
        Path(args.input_file), Path(args.output_file), Path(args.report_file), required_cols
    )
    print(
        f"Limpeza concluída. Arquivo salvo em {args.output_file} e relatório em {args.report_file}."
    )


if __name__ == "__main__":
    main()
