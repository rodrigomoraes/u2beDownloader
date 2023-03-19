# U2be Downloader

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/rodrigomoraes/u2beDownloader)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/rodrigomoraes/u2beDownloader/pytube)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/rodrigomoraes/u2beDownloader/moviepy)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

u2beDownloader is a lightweight downloader and audio extractor for youtube videos.

To use is very simple, just follow the instructions below:

## Instalation

First clone this repo in yout computer.

```bash
  git@github.com:rodrigomoraes/u2beDownloader.git
  cd u2beDownloader
```

You need have python 3 and PIP already installed.
If you prefer, you can use virtual env to this project.

Already in directory, you need install all dependencies run this command:

```bash
  pip install -r requirements.txt
```

## How to use

After installed all dependencies, you can run the program using this command:

```bash
  python3 main.py
```

Now is just follow the instructions in interface to download the videos or audios.


## Disclaimer

Due to a bug in the library pytube, before run the program, you need a little change in the  **'cipher.py'** file.

This file is located in python's packages directory and once located you need **go to line 411 file** and do the change below:

```diff
- transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)
+ transform_plan_raw = js
```
An [issue](https://github.com/pytube/pytube/issues/1512) has been opened in the official pytube repositories to resolve this bug.



