## Desafio

Acessar [este site](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops) e pegar todos os notebooks Lenovo ordenando do mais barato para o mais caro. Pegar todos os dados disponíveis de cada produto.

É interessante que o robô possa ser consumido por outros serviços. Recomendamos a criação de uma pequena REST Ful API JSON para deixar mais otimizado.

Utilizar Puppeteer ou Playwright (Node ou Python)

Criar um repositório no github e nos enviar o link.


## Instalação

> Certifique-se de que possua `git` e `python` instalados em seu ambiente antes de seguir os proxímos passos.

Clone o projeto:

```bash
git clone https://github.com/matheusfelipeog/in8-test.git
```

Entre no diretório `in8-test`:

```bash
cd in8-test
```

Crie e ative o ambiente virtual usando [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html) ou similar:

```bash
virtualenv venv && source venv/bin/activate
```

Instale as dependências do projeto com `pip`:

```bash
pip install -r requirements.txt
```

Playwright para Python possue [algumas dependências](https://playwright.dev/python/docs/cli), instale todas com:

```bash
playwright install && playwright install-deps
```


## Start

Para executar apenas o scraper, sem iniciar a API, use o script `only_scraper.py`:

```bash
python only_scraper.py
```

Será mostrado no terminal todos os dados coletados no formato de uma lista de dicionários de dados.

---

Para iniciar a API, use o `gunicorn`:

```bash
gunicorn --workers=2 'app:create_app()'
```
> `gunicorn` não oferece suporte ao Windows (mas é executado no WSL). Alternativamente, use `flask run`.

Acesse http://127.0.0.1:8000 se iniciou com `gunicorn`

Acesse http://127.0.0.1:5000 se iniciou com `flask`


## Rotas

As rotas disponíveis para acesso aos dados pela API:

- **GET /**

    Retorna um objeto contendo o status, link para a documentação e as rotas disponíveis.

- **GET /api/**

    Retorna um objeto contendo as rotas disponíveis.

- **GET /api/products**

    Retorna uma lista de objetos contendo todos os produtos coletados e armazenados.

- **GET /api/products/\<int:product_id\>**

    Retorna um único objeto de um produto com base no identificador. Caso o identificador não exista, retornada um objeto com uma mensagem de aviso, junto com o código HTTP 404.

### Conteúdo do retorno

Os dados do produto retornado pela API:
- id
- name
- description
- prices
- hard_drives
- image
- reviews
- rating
- url
