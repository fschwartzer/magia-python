# Arquitetura cloud - Magia Python

O projeto possui duas superfícies que compartilham o pacote `motor_magia`:

1. `app.py`: interface Streamlit, indicada para o Streamlit Community Cloud;
2. `api/main.py`: API FastAPI opcional para integrações futuras.

## Streamlit Community Cloud

O fluxo recomendado está documentado no `README.md`. O Community Cloud usa:

- `app.py` como entrypoint;
- `requirements.txt` para instalar Streamlit e Matplotlib;
- `.streamlit/config.toml` para o tema e configurações do aplicativo;
- Python 3.12 selecionado nas configurações avançadas do deploy.

O progresso não é salvo no sistema de arquivos do servidor. Notas, conclusões e histórico ficam na sessão do navegador e podem ser exportados/importados em JSON.

## Motor de execução

`motor_magia.runtime.RuntimeSession` mantém um subprocesso restrito por sessão. O subprocesso preserva variáveis entre células e é encerrado quando:

- o estudante clica em **Resetar**;
- uma execução ultrapassa o timeout;
- ocorre falha de comunicação com o worker.

O worker aplica validação AST, built-ins reduzidos, lista explícita de atributos, limite de saída e restrição de imports. Consulte `motor_magia/sandbox_worker.py`.

## API FastAPI opcional

Para executar apenas a API em ambiente de desenvolvimento:

```bash
python -m pip install -r requirements-cloud.txt
uvicorn api.main:app --reload
```

Documentação Swagger: `http://localhost:8000/docs`.

As rotas continuam disponíveis em `/api/v1`. A persistência em `progress_data/` é adequada somente para execução local ou instância única. Em múltiplas réplicas, substitua `FileProgressStore` por banco de dados.

## Notebooks e módulo pré-extraído

O aplicativo tenta carregar `motor_magia/licoes_extraidas.py` para reduzir I/O no deploy. Para atualizar o módulo após editar notebooks:

```bash
python scripts/extrair_licoes.py
```
