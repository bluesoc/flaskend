from flask_seeder import Seeder

from api.database import db
from api.models import Roles, Claims, UserClaims


class RolesAndClaimsSeeder(Seeder):
    def run(self):
        # Inserindo roles
        roles = [
            Roles(description='User'),
            Roles(description='Manager'),
            Roles(description='Admin'),
        ]

        for role in roles:
            db.session.add(role)
            print(f"Adicionando role: {role.description}")

        # Inserindo claims
        claims = [
            Claims(description='View Reports', active=True),
            Claims(description='Edit Reports', active=True),
            Claims(description='Delete Reports', active=True)
        ]

        for claim in claims:
            db.session.add(claim)
            print(f"Adicionando claim: {claim.description}")

        # Commit as roles e claims
        db.session.commit()
