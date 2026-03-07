from google.adk import Agent


root_agent = Agent(
    name="StoryTeller",
    model="gemini-2.5-flash-lite",
    instruction="""
あなたは楽しい友人です。
ユーザーとの雑談を楽しんでください！
""",
)
