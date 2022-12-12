from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepagesTests(SimpleTestCase):
    # prueba para saber si estan bien localizadas y si nos rediriege ha esa voista con la ruta establecida
    def text_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    # prueba para ver si esta correcta el nombre de la platilla cuando la llamamos
    def test_url_available_by_name(self): # new 
        response = self.client.get(reverse("home")) 
        self.assertEqual(response.status_code, 200)
        
    # prueba para para saber si el nombre del template es el correcto
    def test_template_name_correct(self): # new r
        response = self.client.get(reverse("home")) 
        self.assertTemplateUsed(response, "home.html")
    
    # prueba para verificar si el contenido del template es el correcto
    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutpagesTests(SimpleTestCase):
    def text_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self): # new 
        response = self.client.get(reverse("about")) 
        self.assertEqual(response.status_code, 200)
    
    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")

