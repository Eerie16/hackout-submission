from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Book
class HighestRatedFeed(Feed):
   title = "Highest Rated Books"
   link = "/feed"
   description = "Highest Rated Books in the Store"

   def items(self):
      return Book.objects.all().order_by("-rating")[:5]
		
   def item_title(self, item):
      return item.title+" by " +item.author.first_name+" "+item.author.last_name
		
   def item_description(self, item):
      return item.description
		
   def item_link(self, item):
      return reverse('book_detail', kwargs = {'bid':item.pk})