from src.database.database import SessionLocal
from src.database.models import Profile

COLORS = {
    "blurple": 0x5865F2,
    "red": 0xED4245,
    "green": 0x57F287,
    "yellow": 0xFEE75C,
    "purple": 0x9B59B6,
    "orange": 0xE67E22,
    "pink": 0xEB459E,
}


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

    def parse_color(self, color_input: str) -> int:
        color_input = color_input.lower().strip()

        if color_input in COLORS:
            return COLORS[color_input]

        color_input = color_input.lstrip("#")

        return int(color_input, 16)

    def update_card_color(self, user_id: int, color_input: str):
        color = self.parse_color(color_input)

        with SessionLocal() as session:
            profile = self.get_or_create_profile(user_id)

            profile.card_color = color

            session.merge(profile)
            session.commit()

    def add_badge(self, user_id, badge):
        with SessionLocal() as session:
            profile = session.get(Profile, user_id)

            badges = profile.badges.split(",") if profile.badges else []

            if badge not in badges:
                badges.append(badge)

            profile.badges = ",".join(badges)

            session.commit()

    def check_automatic_badges(self, member):
        if member.guild_permissions.administrator:
            self.add_badge(member.id, "Admin")

        if member.id == 1210721923319865424:  # Me yay
            self.add_badge(member.id, "Owner")

        self.add_badge(member.id, "Early User")
