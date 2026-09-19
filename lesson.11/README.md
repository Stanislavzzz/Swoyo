# Шпаргалка: виртуальные окружения и зависимости

## Виртуальное окружение

Виртуальное окружение нужно, чтобы у каждого проекта были свои библиотеки и их версии.

Создать окружение:

```bash
python -m venv .myvenv
```

На Linux:

```bash
python3 -m venv .myvenv
```

`.myvenv` - папка с виртуальным окружением.

---

## Активация окружения

Linux / macOS:

```bash
source ./.myvenv/bin/activate
```

Windows:

```bash
.myvenv\Scripts\activate
```

Windows PowerShell:

```powershell
.myvenv\Scripts\Activate.ps1
```

После активации работаем с Python и библиотеками именно этого окружения.

---

## Проверка окружения

Посмотреть, какой Python используется:

```bash
which python
```

Проверить версию Python:

```bash
python --version
```

Посмотреть, какой `pip` используется:

```bash
which pip
```

---

## Выход из окружения

```bash
deactivate
```

Выходим из текущего виртуального окружения.

---

# PyPI

Сайт с Python-библиотеками:

```text
https://pypi.org/
```

Там можно найти пакет, посмотреть его описание и доступные версии.

---

# pip

`pip` - стандартный менеджер пакетов Python.

Посмотреть установленные библиотеки:

```bash
pip list
```

Установить библиотеку:

```bash
pip install requests
```

Установить конкретную версию:

```bash
pip install requests==2.31.0
```

Посмотреть информацию о библиотеке:

```bash
pip show requests
```

Удалить библиотеку:

```bash
pip uninstall requests
```

Обновить библиотеку:

```bash
pip install --upgrade requests
```

---

# requirements.txt

Посмотреть установленные пакеты с версиями:

```bash
pip freeze
```

Сохранить зависимости в файл:

```bash
pip freeze > ./requirements.txt
```

Получим файл примерно такого вида:

```text
requests==2.31.0
urllib3==2.0.7
```

Установить зависимости из файла:

```bash
pip install -r ./requirements.txt
```

Обычно `requirements.txt` передают вместе с проектом.

---

# Простой порядок работы с venv и pip

Создаём окружение:

```bash
python3 -m venv .myvenv
```

Активируем:

```bash
source ./.myvenv/bin/activate
```

Устанавливаем библиотеки:

```bash
pip install requests
```

Сохраняем зависимости:

```bash
pip freeze > requirements.txt
```

Для запуска проекта на другом компьютере:

```bash
pip install -r requirements.txt
```

---

# Poetry

Poetry - инструмент для работы с проектом, виртуальным окружением и зависимостями.

Документация:

```text
https://python-poetry.org/docs/
```

---

## Установка Poetry

Linux / macOS:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows PowerShell:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Проверить установку:

```bash
poetry --version
```

---

# Создание проекта

Создать новый проект:

```bash
poetry new my_project
```

`my_project` - имя проекта.

Если проект уже существует:

```bash
poetry init
```

`poetry init` добавляет настройку Poetry в текущий проект.

---

# Выбор Python

Указать версию Python для окружения:

```bash
poetry env use python3.12
```

В данном случае используется Python 3.12.

---

# Установка библиотек через Poetry

Добавить библиотеку:

```bash
poetry add requests
```

Посмотреть зависимости:

```bash
poetry show
```

Посмотреть зависимости в виде дерева:

```bash
poetry show --tree
```

Так можно увидеть, какие библиотеки зависят друг от друга.

---

# Обновление и удаление

Обновить пакет:

```bash
poetry update rich
```

Удалить пакет:

```bash
poetry remove rich
```

---

# Установка зависимостей проекта

Установить зависимости:

```bash
poetry install
```

Обычно используется после скачивания готового проекта.

Установить только основные зависимости:

```bash
poetry install --only=main
```

---

# Группы зависимостей

В Poetry библиотеки можно разделять по группам.

Добавить `ruff` в группу `link`:

```bash
poetry add ruff --group link
```

Установить только эту группу:

```bash
poetry install --only=link
```

Например, отдельно можно хранить дополнительные инструменты для разработки.

---

# uv

Ещё один современный инструмент для работы с Python-проектами и зависимостями.

Документация:

```text
https://docs.astral.sh/uv/getting-started/installation/
```

