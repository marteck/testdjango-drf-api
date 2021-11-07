from celery import shared_task

from .serializers import TicketSerializer


@shared_task
def create(data):
    serializer = TicketSerializer(data=data)
    serializer.is_valid()
    serializer.save()
    return True
