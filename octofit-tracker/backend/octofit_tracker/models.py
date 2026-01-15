from djongo import models
from bson import ObjectId

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField('User', related_name='workouts')

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'
