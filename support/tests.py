from django.test import TestCase

from django.contrib.auth.models import User
from .models import Ticket, Category, Answer


class DbTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create user & supp
        testuser1 = User.objects.create_user(username='testuser1', password='password')
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


    # def test_blog_content(self):
    #     post = Post.objects.get(id=1)
    #     author = f'{post.author}'
    #     title = f'{post.title}'
    #     body = f'{post.body}'
    #     self.assertEqual(author, 'testuser1')
    #     self.assertEqual(title, 'Blog title')
    #     self.assertEqual(body, 'Body content...')
