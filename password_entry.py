from datetime import datetime

class PasswordEntry:
    """Represents a password entry with relevant details."""
    def __init__(self, id, service, username, password, strength, last_updated, notes=""):
        self.id = id
        self.service = service
        self.username = username
        self.password = password # Original password
        self.strength = strength
        self.last_updated = last_updated
        self.notes = notes