# **Описание проекта**
Данный репозиторий является реализацией первого проекта "Игры разума" на платформе Hexlet. Проект представляет собой реализацию 5 простых текстовых игр на языке программирования Python.
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Celovechek/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Celovechek/python-project-49/actions)

### CodeClimate Maintainability Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/88ce675dc28e290e0fce/maintainability)](https://codeclimate.com/github/Celovechek/python-project-49/maintainability)

## Минимальные требования
1. ОС Linux
2. Python версии 3.6 или выше
3. pip версии 19 и выше

Для проверки версии необходимо выполнить команду:
```
python3 -m pip --version
```

При необходимости версию можно обновить командой:
```
python3 -m pip install --upgrade --user pip
```

## Инструкции по установке и запуску
1. Клонируйте репозиторий на свой компьютер.
```
git clone git@github.com:Celovechek/python-project-49.git
```

2. Для установки пакета необходимо выполнить одну из следующих команд:
```
make package-install
```
```
python3 -m pip install --user dist/*.whl
```

3. В случае, если небходимо переустановить пакет, можно выполнить одну из команд:
```
package-reinstall
```
```
python3 -m pip install --user --force-reinstall dist/*.whl
```

4. Для запуска игр достаточно запустить одну из команд:

Определение чётности числа:
```
brain-even
```
Решение простого примера:
```
brain-calc
```
Определение наибольшего делителя двух чисел:
```
brain-gcd
```
Определение недостающего члена арифмитической прогрессиии:
```
brain-progression
```
Определение, является ли число простым:
```
brain-prime
```

## Asciinemas
### Asciinema (installation + brain-even game)
[![asciicast](https://asciinema.org/a/v7E0wgZSqzfZxUysnNPtaYodH.svg)](https://asciinema.org/a/v7E0wgZSqzfZxUysnNPtaYodH)

### Asciinema (brain-calc game)
[![asciicast](https://asciinema.org/a/m4xvWYTFcd9JQ28qVbvvZz304.svg)](https://asciinema.org/a/m4xvWYTFcd9JQ28qVbvvZz304)

### Asciinema (brain-gcd game)
[![asciicast](https://asciinema.org/a/jSosIntJDapDrIdTMxvnRuIk6.svg)](https://asciinema.org/a/jSosIntJDapDrIdTMxvnRuIk6)

### Asciinema (brain-progression game)
[![asciicast](https://asciinema.org/a/K63r6kQETUq6yIssEOJTkFFzV.svg)](https://asciinema.org/a/K63r6kQETUq6yIssEOJTkFFzV)

### Asciinema (brain-prime game)
[![asciicast](https://asciinema.org/a/xnib6aPLo4nHzQj69zP4ve0EH.svg)](https://asciinema.org/a/xnib6aPLo4nHzQj69zP4ve0EH)
