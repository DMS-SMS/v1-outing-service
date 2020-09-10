from datetime import datetime

from domain.entity.outing import Outing

from infrastructure.model import OutingModel


def create_outing_mapper(outing: Outing, uuid) -> OutingModel:
    return OutingModel(
        uuid = uuid,
        student_uuid = outing._student_uuid,
        status = "0",
        situation = outing._situation,
        date = datetime(year=int(outing._date[0:4]), month=int(outing._date[5:7]), day=int(outing._date[8:10])),
        start_time = outing._start_time,
        end_time = outing._end_time,
        place = outing._place,
        reason = outing._reason
    )

def get_outing_mapper(outing_model: OutingModel) -> Outing:
    return Outing(
        outing_uuid=outing_model.uuid,
        student_uuid=outing_model.student_uuid,
        status=outing_model.status,
        situation=outing_model.situation,
        accept_teacher=outing_model.accepted_teacher,
        date=outing_model.date,
        start_time=outing_model.start_time,
        end_time=outing_model.end_time,
        place=outing_model.place,
        reason=outing_model.reason,
        arrival_date=outing_model.arrival_date,
        arrival_time=outing_model.arrival_time
    )