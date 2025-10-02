# Simple Meta CRM

Este proyecto proporciona un peque\u00f1o CRM que guarda en una base de datos local los clientes potenciales obtenidos de un formulario de generaci\u00f3n de clientes de Meta (Facebook).

## Instalaci\u00f3n

```bash
pip install -r requirements.txt
```

## Uso de la l\u00ednea de comandos

Para sincronizar los clientes potenciales de un formulario se ejecuta:

```bash
python -m crm.main sync <FORM_ID> --token <ACCESS_TOKEN>
```

Los datos se almacenan en un archivo SQLite llamado `crm.db` (se puede cambiar con `--db`).

## Interfaz web

Se puede iniciar una peque\u00f1a interfaz web para ver y sincronizar los clientes potenciales:

```bash
python -m crm.web --db crm.db --host 0.0.0.0 --port 5000
```

Al abrir `http://localhost:5000` se mostrar\u00e1 una lista de los clientes guardados y un formulario para sincronizar nuevos contactos desde Meta.
