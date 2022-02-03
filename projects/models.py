from email.policy import default
from django.db import models
import uuid
from users.models import Profile
# Create your models here.


# to register this table to the db, we need to declare it in the admin.py class.
class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    # null is for the database to understand the value can be null (or empty). Blank is for the project to understand we can submit a request with an empty description field. They're the same in the core, but for the 'language' to each functionality.
    description = models.TextField(null=True, blank=True)
    # to create the image we need to install pillow module. we also need to define a default and make changes to the settings.py and URL
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    # autho_now_add= true means that, whenever a instance of this class is created, it'll capture the time stamp of its creation and store it to the database.

    # Many to Many relationship
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratial = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title

# One to many relationship


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.value

# Many to Many relationship


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
