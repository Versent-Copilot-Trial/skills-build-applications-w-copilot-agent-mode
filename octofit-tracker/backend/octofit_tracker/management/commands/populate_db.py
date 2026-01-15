from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        heroes = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
        ]
        user_objs = [User.objects.create(**hero) for hero in heroes]


        # Create activities
        for user in user_objs:
            Activity.objects.create(user=user, type='Running', duration=30)
            Activity.objects.create(user=user, type='Cycling', duration=45)

        # Create workouts and assign users
        workout1 = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        workout2 = Workout.objects.create(name='Power Yoga', description='Flexibility and strength')
        workout1.users.set(user_objs)
        workout2.users.set(user_objs)


        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
