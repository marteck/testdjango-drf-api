from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Ticket, Category, Answer, generate_ticket_id
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
            self.permission_classes = (IsAuthenticated,)
        if self.action == 'retrieve':
            self.permission_classes = (IsOwner,)
        return super(self.__class__, self).get_permissions()

    def create(self, request, *args, **kwargs):
        ticket_id = generate_ticket_id()
        all_data = request.data
        # remember old state
        _mutable = all_data._mutable
        # set to mutable
        all_data._mutable = True
        # change the value for output
        all_data['ticket_id'] = ticket_id
        all_data['user'] = request.user.id
        # set mutable flag back
        all_data._mutable = _mutable
        new_tic_id = request.data['ticket_id']
        super(TicketViewSet, self).create(request, *args, **kwargs)

        context = f'Your ticket with unique ID {new_tic_id} will be added soon... '

        return Response({
            "Message": context
        })



class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = (IsStaffUser,)
        if self.action == 'retrieve':
            self.permission_classes = (IsAuthor,)
        return super(self.__class__, self).get_permissions()
