from django.db.models import QuerySet
from rest_framework.request import Request

from missions.models import Mission


class MissionService:
    @staticmethod
    def get_cat_missions_for_update(request: Request) -> QuerySet[Mission]:
        return (
            Mission.objects.select_for_update()
            .filter(cat_id=request.data.get("cat"))
            .prefetch_related("targets")
        )

    @staticmethod
    def has_incomplete_mission(missions: QuerySet[Mission]) -> bool:
        return any(not mission.is_completed for mission in missions)

    @staticmethod
    def validate_cat_has_not_incomplete_mission(
        missions: QuerySet[Mission],
        exception_to_rise: type[Exception],
    ):
        if MissionService.has_incomplete_mission(missions):
            raise exception_to_rise({"cat": "Cat has incompleted mission"})
