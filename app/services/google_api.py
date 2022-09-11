from datetime import datetime, timedelta

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.services.constants import (DRIVE_SERVICE_VERSION, FORMAT,
                                    SHEETS_SERVICE_VERSION)


async def spreadsheets_create(
        wrapper_services: Aiogoogle
) -> str:
    """Создать гугл-таблицу с отчётом на диске сервисного аккаунта."""
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', SHEETS_SERVICE_VERSION)
    spreadsheet_body = {
        'properties': {'title': f'Отчет от {now_date_time}',
                       'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': 'Отчеты QRkot',
                                   'gridProperties': {'rowCount': 60,
                                                      'columnCount': 8}}}]
    }

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']
    print(f'https://docs.google.com/spreadsheets/d/{spreadsheetid}')
    return spreadsheetid


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    """Предоставить права доступа личному аккаунту к созданному документу."""
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', SHEETS_SERVICE_VERSION)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    """Записать, полученную из бд информацию в документ с таблицами."""
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', DRIVE_SERVICE_VERSION)
    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]

    for project in projects:
        new_row = [project.name, str(timedelta(days=project.project_duration)), project.description]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
