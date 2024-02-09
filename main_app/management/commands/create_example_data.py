from random import choice, randint
from typing import Any, Dict, List

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from pycountry import countries

from main_app.models import JobOffer


class Command(BaseCommand):
    help: str = "Create example users and JobOffers"

    def handle(self, *args, **kwargs) -> None:
        user_data: List[Dict[str, str]] = [
            {
                "username": "testuser1",
                "email": "test@email.com",
                "first_name": "Test",
                "last_name": "User",
                "password": "test_password",
            },
            {
                "username": "testuser2",
                "email": "test2@email.com",
                "first_name": "Second",
                "last_name": "User",
                "password": "second_password",
            },
        ]
        job_data: Dict[str, List[str]] = {
            "types": ["Remote", "Hybrid", "Office"],
            "seniority": ["Junior ", "Mid ", "Senior ", ""],
            "titles": [
                "Python Developer",
                "DevOps",
                "Django Developer",
                "Full-Stack Developer",
                "Software Engineer",
                ".NET Dev",
                "Frontend Programmer",
            ],
            "companies": [
                "Google",
                "Amazon",
                "Comarch",
                "Sii",
                "EY",
                "Netflix",
            ],
            "locations": [
                country.name for country in countries if len(country.name) < 20
            ],
        }
        self.stdout.write(self.style.SUCCESS("Creating users..."))
        try:
            users = [User.objects.create_user(**data) for data in user_data]
        except IntegrityError:
            users = User.objects.all()
            self.stdout.write(self.style.WARNING("Users already created."))

        offers_data: List[Dict[str, Any]] = [
            {
                "author": choice(users),
                "title": f"{choice(job_data['seniority'])}{choice(job_data['titles'])}",
                "company": choice(job_data["companies"]),
                "location": choice(job_data["locations"]),
                "is_remote": choice(job_data["types"]),
                "salary": randint(6000, 10000),
                "description": (
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do"
                    " eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut"
                    " enim ad minim veniam, quis nostrud exercitation ullamco laboris"
                    " nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in"
                    " reprehenderit in voluptate velit esse cillum dolore eu fugiat"
                    " nulla pariatur. Excepteur sint occaecat cupidatat non proident,"
                    " sunt in culpa qui officia deserunt mollit anim id est laborum."
                ),
                "url": f"https://example.com/{i}",
            }
            for i in range(100)
        ]
        self.stdout.write(self.style.SUCCESS("Creating job offers..."))
        JobOffer.objects.bulk_create([JobOffer(**data) for data in offers_data])

        self.stdout.write(self.style.SUCCESS("Data creation complete."))
