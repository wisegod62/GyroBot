import discord
from discord.ext import commands
from discord import app_commands


class Resources(commands.Cog):
    # Create the parent group
    resources_group = app_commands.Group(
        name="resources", description="LGBTQ+ and misc resources"
    )

    # Create the coming-out subgroup
    coming_out_group = app_commands.Group(
        name="coming-out",
        description="Resources for coming out of the closet",
        parent=resources_group,
    )

    def __init__(self, bot):
        self.bot = bot

    @coming_out_group.command(name="overview", description="General overview and tips")
    async def coming_out_overview(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Coming Out: Your Guide",
            description="Coming out is a deeply personal journey. This guide is here to support you, whatever you decide.",
            color=discord.Color.from_rgb(255, 0, 127),
        )
        embed.add_field(
            name="What is coming out?",
            value="Coming out means sharing your identity (sexual orientation, gender identity, etc.) with others. It's your story to tell, on your timeline, to whoever you choose.",
            inline=False,
        )
        embed.add_field(
            name="The golden rule",
            value="Your safety and wellbeing come first. There's no obligation to come out to anyone, and the right time is whenever *you're* ready—not when others expect it.",
            inline=False,
        )
        embed.set_footer(text="Stay safe ❤️")
        await interaction.response.send_message(embed=embed)

    @coming_out_group.command(name="ready", description="Am I ready to come out?")
    async def coming_out_ready(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Am I Ready to Come Out?",
            description="Only you can answer this. Here are some questions to reflect on:",
            color=discord.Color.from_rgb(255, 0, 127),
        )
        embed.add_field(
            name="Safety first",
            value="Will coming out put your physical, emotional, or financial safety at risk? (Housing, family support, job security, etc.)",
            inline=False,
        )
        embed.add_field(
            name="Emotional readiness",
            value="Do you feel mentally prepared for different reactions? Are you coming out for *you*, or because you feel pressured?",
            inline=False,
        )
        embed.add_field(
            name="Support system",
            value="Do you have people (friends, mentors, communities) who will support you afterward?",
            inline=False,
        )
        embed.add_field(
            name="You're allowed to say no",
            value="If the answer to safety is 'I'm not sure,' wait. If you're not ready emotionally, that's okay too. Coming out can wait.",
            inline=False,
        )
        embed.set_footer(text="Stay safe ❤️")
        await interaction.response.send_message(embed=embed)

    @coming_out_group.command(
        name="how-to", description="How do I start the conversation?"
    )
    async def coming_out_how_to(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="How to Start the Conversation",
            description="Here are some approaches that might work for you:",
            color=discord.Color.from_rgb(255, 0, 127),
        )
        embed.add_field(
            name="Direct approach",
            value="Pick a calm moment and say it plainly: 'I want to tell you something about myself...' or 'There's something I've been meaning to share.'",
            inline=False,
        )
        embed.add_field(
            name="Written approach",
            value="A letter, text, or email can give you time to find the right words and gives them time to process without pressure to react immediately.",
            inline=False,
        )
        embed.add_field(
            name="Third-party support",
            value="If you're worried about safety or reactions, consider having a supportive friend or counselor present, or telling someone you trust first.",
            inline=False,
        )
        embed.add_field(
            name="What to expect",
            value="Reactions vary—silence, tears, questions, acceptance, or time to process. None of these mean you did something wrong.",
            inline=False,
        )
        embed.set_footer(text="Stay safe ❤️")
        await interaction.response.send_message(embed=embed)

    @coming_out_group.command(name="bad-reaction", description="What if it goes badly?")
    async def coming_out_bad_reaction(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Handling Difficult Reactions",
            description="Bad reactions happen. Here's what to remember:",
            color=discord.Color.from_rgb(255, 0, 127),
        )
        embed.add_field(
            name="Their reaction is not about you",
            value="People sometimes react poorly because of their own beliefs, fears, or biases—not because there's anything wrong with *you*.",
            inline=False,
        )
        embed.add_field(
            name="You have options",
            value="If someone is abusive, disrespectful, or unsafe, you don't have to stay and listen. You can leave, end the conversation, or cut contact.",
            inline=False,
        )
        embed.add_field(
            name="It might take time",
            value="Some people need time to process. Others may come around later. Some won't—and that says nothing about your worth.",
            inline=False,
        )
        embed.add_field(
            name="Reach out for support",
            value="Talk to trusted friends, a therapist, or LGBTQ+ communities. You don't have to process this alone.",
            inline=False,
        )
        embed.set_footer(text="Stay safe ❤️")
        await interaction.response.send_message(embed=embed)

    @coming_out_group.command(name="next-steps", description="What happens after?")
    async def coming_out_next_steps(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="After You Come Out",
            description="What comes next is up to you:",
            color=discord.Color.from_rgb(255, 0, 127),
        )
        embed.add_field(
            name="Take care of yourself",
            value="Coming out is emotional. Rest, spend time with supportive people, do things that make you feel good.",
            inline=False,
        )
        embed.add_field(
            name="You're not done coming out",
            value="You may need to come out to others (coworkers, acquaintances, etc.). Each time is its own decision.",
            inline=False,
        )
        embed.add_field(
            name="Find your community",
            value="Connecting with other LGBTQ+ people—online or in person—can be incredibly healing and validating.",
            inline=False,
        )
        embed.add_field(
            name="Keep boundaries",
            value="You don't owe anyone details about your identity. Share what you're comfortable with, nothing more.",
            inline=False,
        )
        embed.set_footer(text="Stay safe ❤️")
        await interaction.response.send_message(embed=embed)

    @coming_out_group.command(
        name="not-ready", description="It's okay if you're not ready"
    )
    async def coming_out_not_ready(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="It's Okay to Wait",
            description="Not being ready is valid. Here's why:",
            color=discord.Color.from_rgb(255, 0, 127),
        )
        embed.add_field(
            name="Timing matters",
            value="Coming out when you're truly ready is better than doing it because you feel pressured. There's no deadline.",
            inline=False,
        )
        embed.add_field(
            name="You know your situation best",
            value="Only you understand your family dynamics, living situation, job security, and safety concerns. Trust yourself.",
            inline=False,
        )
        embed.add_field(
            name="Living authentically takes many forms",
            value="You can be true to yourself without coming out to everyone. Some people come out selectively to chosen family.",
            inline=False,
        )
        embed.add_field(
            name="You can change your mind",
            value="Not ready now doesn't mean not ready ever. Your readiness can shift as your situation changes.",
            inline=False,
        )
        embed.set_footer(text="Stay safe ❤️")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Resources(bot))
