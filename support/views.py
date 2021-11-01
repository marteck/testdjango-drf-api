from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Ticket, Category, Answer
from .serializers import UserSerializer, TicketSerializer, CategorySerializer, AnswerSerializer
from .permissions import IsStaffUser, IsOwner, IsAuthor


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsStaffUser,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsStaffUser,)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = (IsStaffUser,)
        if self.action == 'retrieve':
            self.permission_classes = (IsOwner,)
        return super(self.__class__, self).get_permissions()


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = (IsStaffUser,)
        if self.action == 'retrieve':
            self.permission_classes = (IsAuthor,)
        return super(self.__class__, self).get_permissions()







