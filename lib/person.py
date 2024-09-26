#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    # List of approved jobs
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="John Doe", job="Admin"):
        """
        Initialize the Person instance with a default name and job.

        Parameters:
        name (str): The name of the person. Must be between 1 and 25 characters and will be converted to title case.
        job (str): The job of the person. Must be in the list of approved jobs.
        """
        self._name = None  # Initialize with None before calling the setter
        self._job = None   # Initialize with None before calling the setter
        self.name = name   # This will trigger the name setter for validation and formatting
        self.job = job     # This will trigger the job setter for validation

    @property
    def name(self):
        """Getter for the name property."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for the name property with validation and conversion to title case."""
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        """Getter for the job property."""
        return self._job

    @job.setter
    def job(self, value):
        """Setter for the job property with validation."""
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
