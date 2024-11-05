from django.test import TestCase
from app.views import *
from app.forms import *

# Create your tests here.
class TestForms(TestCase):

    def test_font_times_1(self):
        response = self.client.get('/warmup/font-times/?string=bunger&num=3')
        form = FontTime(data={
            'string': 'bunger',
            'num': 3
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, "bunbunbun")

    def test_font_times_2(self):
        response = self.client.get('/warmup/font-times/?string=plinko&num=5')
        form = FontTime(data={
            'string': 'plinko',
            'num': 5
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, "pliplipliplipli")

    def test_font_times_no_data(self):
        form = FontTime(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_no_teen_sum_1(self):
        response = self.client.get('/logic/no-teen-sum/?a=1&b=2&c=3')
        form = TeenSum(data={
            'a': '1',
            'b': '2',
            'c': '3'
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, 6)
    
    def test_no_teen_sum_2(self):
        response = self.client.get('/logic/no-teen-sum/?a=2&b=13&c=1')
        form  = TeenSum(data={
            'a': '2',
            'b': '13',
            'c': '1'
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, 3)
    
    def test_no_teen_sum_empty(self):
        form = TeenSum(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_xyz_there_1(self):
        response = self.client.get('/string/xyz-there/?Input=abcxyz')
        form = XYZThere(data={
            'Input': 'abcxyz'
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, True)

    def test_xyz_there_2(self):
        response = self.client.get('/string/xyz-there/?Input=abc.xyz')
        form  = XYZThere(data={
            'Input': 'abc.xyz'
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, False)

    def test_xyz_there_empty(self):
        form = XYZThere(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_centered_average_1(self):
        response = self.client.get('/list/centered-average/?a=1&b=2&c=3&d=4&e=100')
        form = CenteredAverage(data={
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '100',
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, 3)

    def test_centered_average_2(self):
        response = self.client.get('/list/centered-average/?a=5&b=3&c=4&d=6&e=2')
        form = CenteredAverage(data={
            'a': '5',
            'b': '3',
            'c': '4',
            'd': '6',
            'e': '2',
        })
        self.assertTrue(form.is_valid())
        self.assertContains(response, 4)
    
    def test_centered_average_empty(self):
        form = CenteredAverage(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)