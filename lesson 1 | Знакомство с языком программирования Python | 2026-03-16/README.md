# Документация по Уроку

## 1. Скачать Python
Официальный сайт Python:
- Python.org￼

Рекомендуется скачивать последнюю стабильную версию Python 3.x.

## 2. Онлайн-IDE для тестирования кода
- OnlineGDB Python Debugger￼ – быстрый способ тестировать Python-код без установки.

## 3. Правила написания кода
- Использовать стандарт PEP 8 (PEP 8 — Style Guide for Python Code￼).
- Чистый и читаемый код.
- Именование переменных в стиле snake_case.
- Ограничение длины строк 79–99 символов.
- Комментарии для сложной логики.

## 4. Установка Python и важные особенности

### Важно:

### Windows:
- Скачайте установщик с Python.org￼.
- Выберите опцию Add Python to [PATH](https://education.launchcode.org/lchs/_images/win-python-installer.png).
- Следуйте инструкциям установки.

### macOS:
- Установите через Homebrew:
```bash
brew install python
```
- Проверка версии:
```bash
python3 --version
```

### Linux:
- Установите через пакетный менеджер:
```bash
sudo apt update
sudo apt install python3 python3-pip
```
- Проверка версии:
```bash
python3 --version
```


### Важные особенности:
- Python 3 отличается от Python 2 (рекомендуется только Python 3.x).
- PIP устанавливается автоматически с Python 3.x.
- Для виртуальных окружений используйте venv:
```bash
python3 -m venv myenv
source myenv/bin/activate   # Linux/macOS
myenv\Scripts\activate      # Windows
```


## 5. Почему важно использовать аннотации типов сразу
- Улучшают читаемость и понимание кода.
- Помогают статическим анализаторам (mypy, Pyright) выявлять ошибки.
- Ускоряют работу IDE с автодополнением и рефакторингом.
- Стандарт в крупных проектах и профессиональной разработке.

### Пример аннотации:
```python
def add(a: int, b: int) -> int:
    return a + b
```
## 6. Рекомендуемые IDE для Python
- Jupyter Notebook￼ – для интерактивного анализа и визуализации данных.
- Google Colab￼ – облачная версия Jupyter с GPU.
- Visual Studio Code￼ – легкая IDE с расширениями Python.
- Zed￼ – современный текстовый редактор с поддержкой Python.
- PyCharm￼ – мощная профессиональная IDE.

## 7. Настройка VSCode под Python
1. Установите Visual Studio Code￼.
2. Установите расширение Python от Microsoft.
3. Настройте интерпретатор:
- Ctrl+Shift+P → “Python: Select Interpreter” → выберите установленный Python.
4. Настройка форматирования кода:
  - Установите black для автоформатирования:
```bash
pip install black
```
- В VSCode: Ctrl+, → Search “Format On Save” → включить.

5. Настройка проверки типов:
- Установите mypy:
```bash
pip install mypy
```
- Включите в настройках VSCode.

## 8. Полезные ссылки
- Документация Python￼
- PEP 8￼
- Mypy￼
- PyPI￼ – репозиторий пакетов Python
- VSCode Python Docs￼
