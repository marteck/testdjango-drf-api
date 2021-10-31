from django.test import TestCase

from django.contrib.auth.models import User
from .models import Ticket, Category, Answer


class DbTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create user & supp
        testuser1 = User.objects.create_user(username='testuser', password='password')
        testuser1.save()
        supp = User.objects.create_user(username='supp1', password='pass', is_staff=True)
        supp.save()

        # Create category
        cat = Category(name='Common', slug='cmn_')
        cat.save()

        # Create ticket
        test_ticket = Ticket(title='Ticket', user=testuser1, content='Some content', category=cat)
        test_ticket.save()

        # Create Answer
        answer = Answer(content='Relax', user=supp)
        answer.save()

    def test_db_entry(self):
        user = User.objects.get(id=1)
        name = f'{user.username}'
        ticket = Ticket.objects.get(id=1)
        content = f'{ticket.content}'
        answer = Answer.objects.get(id=1)
        text = f'{answer.content}'

        self.assertEqual(name, 'testuser')
        self.assertEqual(content, 'Some content')
        self.assertEqual(text, 'Relax')
