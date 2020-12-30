# Feriados ANBIMA

Módulo em Python que facilita o uso do [python-bizdays](https://github.com/wilsonfreitas/python-bizdays) para feriados Brasileiros.

## Instalando dependências

```sh
cd [project_dir]
pip install -r requirements.txt
```

## Uso

```python
from bizdays import Calendar
from anbima import holidays
cal = Calendar(holidays(), ['Saturday', 'Sunday'])
```

A função `anbima.holidays` faz download do arquivo de calendário do site da ANBIMA na pasta de trabalho. O link para o arquivo é http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls.
