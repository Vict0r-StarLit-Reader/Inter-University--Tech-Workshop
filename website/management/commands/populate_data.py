from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from website.models import Speaker, Schedule

class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        # Clear existing data
        Speaker.objects.all().delete()
        Schedule.objects.all().delete()

        # Create sample speakers
        speakers_data = [
            {
                'name': 'Dr. Jane Mwangi',
                'title': 'AI Research Lead',
                'topic': 'The Future of Machine Learning in Africa',
                'organization': 'Nairobi Innovation Hub'
            },
            {
                'name': 'Prof. John Kamau',
                'title': 'Computer Science Professor',
                'topic': 'Web Development Best Practices 2024',
                'organization': 'University of Nairobi'
            },
            {
                'name': 'Sarah Ochieng',
                'title': 'Senior Software Engineer',
                'topic': 'Building Scalable Mobile Applications',
                'organization': 'Safaricom PLC'
            },
            {
                'name': 'Michael Njoroge',
                'title': 'Cybersecurity Expert',
                'topic': 'Protecting Digital Assets in Modern Organizations',
                'organization': 'Kenya Cyber Security Agency'
            },
            {
                'name': 'Grace Wanjiru',
                'title': 'Data Science Lead',
                'topic': 'Data Analytics for Business Intelligence',
                'organization': 'IBM Kenya'
            },
            {
                'name': 'David Mutiso',
                'title': 'Blockchain Developer',
                'topic': 'Introduction to Blockchain Technology',
                'organization': 'Andela Kenya'
            }
        ]

        for speaker_data in speakers_data:
            Speaker.objects.create(**speaker_data)

        # Create sample schedule
        schedule_data = [
            {
                'start_time': timezone.now().replace(hour=9, minute=0, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1),
                'location': 'Main Auditorium',
                'description': 'Registration and Welcome Coffee'
            },
            {
                'start_time': timezone.now().replace(hour=10, minute=0, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1, minutes=30),
                'location': 'Main Auditorium',
                'description': 'Opening Ceremony and Keynote Speech'
            },
            {
                'start_time': timezone.now().replace(hour=11, minute=30, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1),
                'location': 'Lab Room A',
                'description': 'Workshop: Introduction to Machine Learning'
            },
            {
                'start_time': timezone.now().replace(hour=11, minute=30, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1),
                'location': 'Lab Room B',
                'description': 'Workshop: Modern Web Development with React'
            },
            {
                'start_time': timezone.now().replace(hour=13, minute=0, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1),
                'location': 'Dining Hall',
                'description': 'Lunch Break and Networking'
            },
            {
                'start_time': timezone.now().replace(hour=14, minute=0, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1, minutes=30),
                'location': 'Main Auditorium',
                'description': 'Panel Discussion: The Future of Tech in Africa'
            },
            {
                'start_time': timezone.now().replace(hour=15, minute=30, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1),
                'location': 'Lab Room A',
                'description': 'Workshop: Cybersecurity Fundamentals'
            },
            {
                'start_time': timezone.now().replace(hour=15, minute=30, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1),
                'location': 'Lab Room B',
                'description': 'Workshop: Mobile App Development'
            },
            {
                'start_time': timezone.now().replace(hour=17, minute=0, second=0, microsecond=0).time(),
                'duration': timedelta(hours=1),
                'location': 'Main Auditorium',
                'description': 'Closing Ceremony and Awards'
            }
        ]

        for schedule_item in schedule_data:
            Schedule.objects.create(**schedule_item)

        self.stdout.write(self.style.SUCCESS('Successfully populated sample data!'))
