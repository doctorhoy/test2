# Simple Meta CRM

Este proyecto proporciona un peque\u00f1o CRM que guarda en una base de datos local los clientes potenciales obtenidos de un formulario de generaci\u00f3n de clientes de Meta (Facebook).

## Instalaci\u00f3n

```bash
pip install -r requirements.txt
```

## Uso

Para sincronizar los clientes potenciales de un formulario se ejecuta:

```bash
python -m crm.main sync <FORM_ID> --token <ACCESS_TOKEN>
```

Los datos se almacenan en un archivo SQLite llamado `crm.db` (se puede cambiar con `--db`).
