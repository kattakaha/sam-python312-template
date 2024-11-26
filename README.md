# sam-python312-template

AWS SAM Python3.12 template repository

![python](https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge) ![AWS](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) ![lambda](https://img.shields.io/badge/-AWS%20lambda-232F3E.svg?logo=aws-lambda&style=for-the-badge) ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white) ![github-actions](https://img.shields.io/badge/-githubactions-FFFFFF.svg?logo=github-actions&style=for-the-badge)

## 環境構築

- [ ] nodenv
- [ ] pyenv
- [ ] wsl2 Ubuntu
- [ ] Docker
- [ ] sam

ここら辺参考になるかも

- <https://qiita.com/kkml_4220/items/9daf2117e515e5342bac>
- <https://qiita.com/kkml_4220/items/1b239b3aabfabc6f5586>
- <https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/install-sam-cli.html>

## Installation

`pyenv`を使って`Python`のバージョン合わせる場合は[こちらの記事](https://qiita.com/twipg/items/75fc9428e4c33ed429c0)を参考に`Python 3.12.6
`を使用してください。

```bash
# install poetry
pip install poetry
# Poetry to use project-specific virtual env
poetry config virtualenvs.in-project true
# install virtual env
poetry install
# install npm dependencies
npm install
```

## Usage

### Task Runner

> [!NOTE]
> 開発用サーバーは、Python ファイルが変更されるたびに再ビルドし実行されます。

#### Python

```bash
# start local api server
poetry run task dev
# format
poetry run task format
# lint
poetry run task lint
# pytest
poetry run task test
```

> [!TIP] > `poetry shell`で仮想環境に入った状態で実行する場合は、`poetry run`を省略可能です。

```bash
# start local api server
task dev
# format
task format
# lint
task lint
# pytest
task test
```
