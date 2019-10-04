from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
# Create your models here.
User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    # only filtering data
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(user__username__icontains=query)

                    )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    # modifying get_queryset
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        # getting all data through get_queryset but then using published function in above class
        return self.get_queryset().published()
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null = True , on_delete=[models.SET_NULL])
    image = models.ImageField(upload_to="image/" , blank =True, null= True)
    title   = models.CharField(max_length=100)
    slug	= models.SlugField(unique=True)
    content = models.TextField(default="Content")
    publish_date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()
    class Meta:
        ordering = [
                    '-publish_date',
                    '-updated',
                    '-timestamp'
                    ]
    # not working
    def get_absolute_url(self):
        return f"blog/{self.slug}"
    # not working
    def get_edit_url(self):
        return f"{self.get_absolute_url}/edit"
    # not working
    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"

class SearchQuery(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null= True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)
