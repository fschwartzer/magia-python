# Magia Python 🪄🐍

Aplicativo educacional em Streamlit para crianças e adolescentes aprenderem Python por meio de oito aulas interativas. O conteúdo vem dos notebooks do projeto e cada célula de código pode ser editada e executada dentro de um processo restrito.

## Recursos

- oito aulas com explicações em Markdown e laboratórios de código;
- caixas de resposta separadas e identificadas para cada chamada de `input()`;
- captura de saída, erros amigáveis e gráficos Matplotlib;
- variáveis preservadas entre execuções da mesma sessão;
- timeout, limite de saída e política de código para proteger o servidor público;
- progresso automático por laboratório executado, anotações e histórico isolados por sessão;
- exportação e restauração do progresso em JSON;
- interface responsiva em português.

## Executar localmente

Use Python 3.12, a mesma versão padrão indicada para o deploy no Community Cloud:

```bash
python -m venv .venv
```

No Windows:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

No Linux ou macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

## Publicar no Streamlit Community Cloud

1. Crie um repositório no GitHub e envie todo o conteúdo desta pasta, inclusive `.streamlit/config.toml`, os notebooks e `motor_magia/`.
2. Acesse [share.streamlit.io](https://share.streamlit.io) e escolha **Create app**.
3. Selecione o repositório e a branch.
4. Informe `app.py` como arquivo de entrada.
5. Em **Advanced settings**, selecione Python 3.12.
6. Clique em **Deploy**.

O Community Cloud instala automaticamente as versões fixadas em `requirements.txt`. Não é necessário usar o `Dockerfile` para essa publicação.

Referências oficiais:

- [Organização dos arquivos](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization)
- [Dependências do aplicativo](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)
- [Procedimento de implantação](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)

## Progresso no Community Cloud

Arquivos criados durante a execução não têm persistência garantida no Community Cloud. Por isso, o aplicativo não grava um JSON compartilhado no servidor. Cada estudante usa uma sessão independente e pode baixar o próprio arquivo `magia_python_progresso.json` para restaurá-lo em outro dia.

## Segurança do laboratório

O código do estudante não é executado diretamente pelo processo do Streamlit. Cada sessão usa um interpretador Python separado com:

- imports limitados a `math`, `random`, `time` e `matplotlib`;
- built-ins e atributos permitidos por lista explícita;
- bloqueio de arquivos, rede, introspecção e atributos especiais;
- timeout por execução;
- limite de caracteres de código, entrada, saída e gráficos;
- reinicialização automática após travamento ou timeout.

Esse mecanismo reduz o risco operacional, mas não deve ser tratado como uma sandbox de segurança equivalente a isolamento por máquina virtual. Para uma plataforma aberta em grande escala, prefira um serviço dedicado de execução isolada por contêiner.

## Atualizar as aulas extraídas

Depois de alterar qualquer notebook, regenere o módulo usado no deploy:

```bash
python scripts/extrair_licoes.py
```

O comando atualiza `motor_magia/licoes_extraidas.py`.

## Testes

```bash
python -m unittest discover -s tests -p "test_*.py"
python tests/smoke_motor.py
```

Com Streamlit instalado, a suíte também valida a inicialização da interface.

## Docker opcional

```bash
docker build -t magia-python .
docker run --rm -p 8501:8501 magia-python
```

Acesse `http://localhost:8501`.
