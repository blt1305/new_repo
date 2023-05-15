# Основные команды для работы с виртуальным окружением

```
- python -m venv <имя виртуального окружения> - создать виртуальное окружение
- windows: virtual_env\Scripts\activate, linux: source virtual_env/bin/activate - активировать виртуальное окружение
- deactivate - деактивировать виртуальное окружение
``` 

## Основные команды для работы с pip

```
- pip install requests - установить библиотеку
- pip freeze - вывести список установленных библиотек
- pip uninstall requests - удалить библиотеку
- pip freeze > requirements.txt - записать список установленных библиотек в файл
- pip install -r requirements.txt - установить библиотеки из файла
```

### Полезные ссылки

- [видео про виртуальное окружение](https://www.youtube.com/watch?v=z5GgYRldyDk)
- [гайд по pip](https://pythonworld.ru/osnovy/pip.html)
- [познакомиться с Markdown](https://paulradzkov.com/2014/markdown_cheatsheet/)
- [pipenv](https://pythonchik.ru/okruzhenie-i-pakety/pipenv-menedzher-zavisimostej-python)
- [poetry](https://www.8host.com/blog/ustanovka-menedzhera-zavisimostej-poetry/#:~:text=Poetry%20%E2%80%93%20%D1%8D%D1%82%D0%BE%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F,%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%B8%20%D0%B8%D0%B7%D0%BE%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%B2%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D1%81%D1%80%D0%B5%D0%B4.) и [здесь](https://habr.com/ru/articles/593529/)

## Работа с переменными окружения


<table>
    <th></th>
    <th>Windows</th>
    <th>Linux</th>
<tr>
    <td>Вывести переменные окружения</td>
    <td>SET</td>
    <td>printenv</td>
</tr>
<tr>
    <td>Вывести значение переменной</td>
    <td>echo %tms%</td>
    <td>printenv tms</td>
</tr>
<tr>
    <td>Задать переменную окружения</td>
    <td>set tms=example</td>
    <td>export tms=example</td>
</tr>
<tr>
    <td>Удалить переменную окружения</td>
    <td>set tms=</td>
    <td>unset tms</td>
</tr>

</table>