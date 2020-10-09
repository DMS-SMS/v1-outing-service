from domain.usecase.approve_outing_teacher_usecase import ApproveOutingTeacherUseCase
from domain.usecase.certify_outing_usecase import CertifyOutingUseCase
from domain.usecase.get_outings_with_filter_usecase import GetOutingsWithFilterUseCase
from domain.usecase.reject_outing_teacher_usecase import RejectOutingTeacherUseCase
from proto.python.outing import outing_teacher_pb2_grpc, outing_teacher_pb2

from application.service.teacher_outing_service import TeacherOutingService
from application.decorator.metadata import jagger_enable
from application.decorator.error_handling import error_handling

from infrastructure.implementation.repository.outing_repository_impl import OutingRepositoryImpl
from infrastructure.implementation.service.paging_service_impl import PagingServiceImpl


class TeacherOutingServicer(outing_teacher_pb2_grpc.OutingTeacherServicer):
    def __init__(self):
        self.outing_repository = OutingRepositoryImpl()
        self.paging_service = PagingServiceImpl()

        self.service = TeacherOutingService(
            approve_outing_teacher_usecase=ApproveOutingTeacherUseCase(
                self.outing_repository
            ),
            reject_outing_teacher_usecase=RejectOutingTeacherUseCase(
                self.outing_repository
            ),
            certify_outing_usecase=CertifyOutingUseCase(
                self.outing_repository
            ),
            get_outings_with_filter_usecase=GetOutingsWithFilterUseCase(
                self.outing_repository,
                self.paging_service
            )
        )

    @error_handling(outing_teacher_pb2.OutingResponse)
    @jagger_enable
    def GetOutingWithFilter(self, request, context):
        return self.service.get_outings_with_filter(request)

    @error_handling(outing_teacher_pb2.ConfirmOutingResponse)
    @jagger_enable
    def ApproveOuting(self, request, context):
        return self.service.approve_outing(request)

    @error_handling(outing_teacher_pb2.ConfirmOutingResponse)
    @jagger_enable
    def RejectOuting(self, request, context):
        return self.service.reject_outing(request)

    @error_handling(outing_teacher_pb2.ConfirmOutingResponse)
    @jagger_enable
    def CertifyOuting(self, request, context):
        return self.service.certify_outing(request)
