# ...app/api/endpoints/google_api.py

# Понадобится для того, чтобы задать временные интервалы
from datetime import datetime
# Класс «обёртки»
from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser

from app.crud.charity_project import charity_project_crud

# Создаём экземпляр класса APIRouter
from app.schemas.charity_project import CharityProjectBase
from app.services.google_api import spreadsheets_create, set_user_permissions, spreadsheets_update_value

router = APIRouter()


@router.post(
    '/',
    # Тип возвращаемого эндпоинтом ответа
    response_model=list[dict[str, str]],

    # Определяем зависимости
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        # Сессия
        session: AsyncSession = Depends(get_async_session),
        # «Обёртка»
        wrapper_services: Aiogoogle = Depends(get_service)

):
    """
    Получить информацию из БД о скорости закрытия проектов,
    сформировать отчёт в гугл-таблице.
    Только для суперюзеров.
    """
    closed_projects = await charity_project_crud.get_projects_by_completion_rate(
        session=session
    )
    # Вызов функций
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(spreadsheetid,
                                    closed_projects,
                                    wrapper_services)
    return closed_projects

