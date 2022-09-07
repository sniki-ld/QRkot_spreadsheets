from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_charity_project_by_name(
            self,
            charity_project_name: str,
            session: AsyncSession,
    ):
        """Вернуть проект по его названию."""
        db_charity_project = await session.execute(
            select(self.model).where(
                self.model.name == charity_project_name
            )
        )

        db_charity_project = db_charity_project.scalars().first()
        return db_charity_project

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession
    ) -> list[dict[str, str]]:
        """
        Получить все закрытые проекты сортированные по продолжительности
        существования проекта (project_duration).
        """
        query = select(CharityProject.name,
                       CharityProject.description,
                       (func.julianday(CharityProject.close_date) -
                        func.julianday(CharityProject.create_date)).label('project_duration')).where(
            CharityProject.fully_invested.is_(True)).order_by('project_duration')

        closed_projects = await session.execute(query)
        return closed_projects.all()


charity_project_crud = CRUDCharityProject(CharityProject)
