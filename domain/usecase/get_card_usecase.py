from domain.entity import Outing, Student
from domain.repository import OutingRepository, StudentRepository
from domain.service.uuid_service import UuidService


class GetCardUseCase:
    def __init__(self, outing_repository, student_repository, uuid_service):
        self.outing_repository: OutingRepository = outing_repository
        self.student_repository: StudentRepository = student_repository
        self.uuid_service: UuidService = uuid_service

    def run(self, uuid, o_id):
        outing: Outing = self.outing_repository.get_outing_by_oid(o_id)
        student: Student = self.student_repository.get_student_by_uuid(
            outing._student_uuid
        )

        self.uuid_service.compare_uuid_and_sid(
            uuid, outing._student_uuid
        )

        return outing, student