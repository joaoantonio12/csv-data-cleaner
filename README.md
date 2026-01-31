# csv-data-cleaner

## Problema

Datasets em formato CSV frequentemente contêm linhas duplicadas, colunas vazias ou inconsistentes e problemas de formatação. Esses erros atrapalham análises e automações simples. É importante realizar uma limpeza inicial para padronizar os dados antes de usá-los em outros processos.

## Solução

**csv-data-cleaner** é um utilitário em Python que lê um arquivo CSV, remove linhas duplicadas, verifica a existência de colunas obrigatórias, normaliza valores de texto (como remoção de espaços extras e padronização de caixa) e gera um relatório de erros encontrados. O resultado é salvo em um novo arquivo CSV pronto para uso.

## Como rodar

1. Clone este repositório ou copie os arquivos para sua máquina.
2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate    # Windows
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
4. Execute o script passando o arquivo de entrada e os nomes das colunas obrigatórias (se houver):

   ```bash
   python main.py --input-file dados.csv --output-file dados_limpos.csv \
                  --report-file relatorio_erros.txt \
                  --required-columns id,nome,email
   ```

## Exemplo de uso

Suponha que você tenha um arquivo `usuarios.csv` com as colunas `id`, `nome` e `email`, mas algumas linhas duplicadas e campos em branco. Para limpar o arquivo e gerar um relatório:

```bash
python main.py --input-file usuarios.csv --output-file usuarios_limpos.csv \
               --report-file usuarios_erros.txt \
               --required-columns id,nome,email
```

## Limitações

- Atualmente o script assume que o separador de campo é vírgula (`,` ) e codificação UTF-8. Ajustes podem ser necessários para outros formatos.
- A normalização de strings é simples: aplica `strip()` e converte para minúsculas. Não há transliteração nem remoção de acentos.
- O relatório de erros é básico e registra apenas registros com colunas obrigatórias ausentes.

## Próximos passos

- Suporte a delimitadores personalizados (como `;` ou `\t`).
- Opção de salvamento em outros formatos (JSON, Excel).
- Adicionar testes unitários e cobertura de código.
