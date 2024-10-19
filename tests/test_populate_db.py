from api.database import db
from api.models import Users, Roles, Claims, UserClaims

# Cria diversas entrada no banco de dados,
# Apenas para testes durante o desenvolvimento


def populate_db():
    roles = [
        Roles(description='Admin'),
        Roles(description='User'),
        Roles(description='Manager')
    ]

    db.session.bulk_save_objects(roles)
    db.session.commit()

    claims = [
        Claims(description='View Reports', active=True),
        Claims(description='Edit Reports', active=True),
        Claims(description='Delete Reports', active=True)
    ]
    db.session.bulk_save_objects(claims)
    db.session.commit()

    users = [
        Users(name='John Doe', email='john.doe@example.com',
              password='securepassword', role_id=1),
        Users(name='Jane Smith', email='jane.smith@example.com',
              password='anotherpassword', role_id=2),
        Users(name='Alice Johnson', email='alice.johnson@example.com',
              password='yetanotherpassword', role_id=3)
    ]
    db.session.bulk_save_objects(users)
    db.session.commit()

    user_claims = [
        # John Doe has View Reports
        UserClaims(user_id=1, claim_id=1),

        # Jane Smith has Edit Reports
        UserClaims(user_id=2, claim_id=2),

        # Alice Johnson has Delete Reports
        UserClaims(user_id=3, claim_id=3)
    ]
    db.session.bulk_save_objects(user_claims)
    db.session.commit()
