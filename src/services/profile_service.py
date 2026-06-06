from src.database.database import SessionLocal
from src.database.models import Profile


class ProfileService:
    def get_or_create_profile(self, user_id: int):

        with SessionLocal() as session:
            profile = session.get(Profile, user_id)

            if profile is None:
                profile = Profile(user_id=user_id)

                session.add(profile)

                session.commit()

                session.refresh(profile)

            return profile

    def update_field(self, user_id: int, field: str, value: str):

        with SessionLocal() as session:
            profile = session.get(Profile, user_id)

            if profile is None:
                profile = Profile(user_id=user_id)

                session.add(profile)

            setattr(profile, field, value)

            session.commit()

            session.refresh(profile)

            return profile
