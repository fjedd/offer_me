import sys
from random import choice, randint
from typing import Any, Dict, List

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from main_app.models import JobOffer


class Command(BaseCommand):
    help: str = "Create example users and JobOffers"

    def handle(self, *args, **kwargs) -> None:
        self.stdout.write(self.style.SUCCESS("Creating users..."))
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
        try:
            users = [User.objects.create_user(**data) for data in user_data]
        except IntegrityError:
            self.stdout.write(self.style.ERROR("Data already created."))
            sys.exit(1)

        offers_data: List[Dict[str, Any]] = [
            {
                "author": choice(users),
                "title": f"Offer {i}",
                "company": f"Company {i}",
                "location": f"City {i}",
                "is_remote": choice(["Remote", "Hybrid", "Office"]),
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
                "url": f"https://example.com/offer{i}",
            }
            for i in range(10)
        ]

        self.stdout.write(self.style.SUCCESS("Creating job offers..."))
        JobOffer.objects.bulk_create([JobOffer(**data) for data in offers_data])

        self.stdout.write(self.style.SUCCESS("Data creation complete."))
