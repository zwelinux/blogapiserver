from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
class LatestPostsFeed(Feed):
	title = 'tweetie'
	link = '/'
	description = 'New posts'
	def items(self):
		return Post.objects.order_by('-date_posted')
	def item_title(self, item):
		return item.title
	def item_description(self, item):
		return truncatewords(item.content, 30)