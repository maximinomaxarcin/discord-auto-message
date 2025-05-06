import discord
import asyncio

class AutoMessageBot(discord.Client):
    def __init__(self, message, channel_ids, loop_interval=86400, **kwargs):
        super().__init__(**kwargs)
        self.message = message
        self.channel_ids = channel_ids
        self.loop_interval = loop_interval  # default 24 hours in seconds

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        while True:
            for channel_id in self.channel_ids:
                channel = self.get_channel(channel_id)
                if channel is None:
                    print(f"Warning: Cannot find channel with ID {channel_id}. Skipping.")
                    continue
                try:
                    await channel.send(self.message)
                    print(f"Sent message to channel ID {channel_id}")
                except Exception as e:
                    print(f"Failed to send message to channel ID {channel_id}: {e}")
            print(f"Waiting for {self.loop_interval} seconds before next round...")
            await asyncio.sleep(self.loop_interval)

def main():
    token = input("Enter your Discord Bot Token: ").strip()
    message = input("Enter the message you want to send: ").strip()
    channel_ids_input = input("Enter Discord Channel IDs (comma-separated): ").strip()

    # Parse channel IDs into integers
    try:
        channel_ids = [int(cid.strip()) for cid in channel_ids_input.split(",") if cid.strip()]
    except ValueError:
        print("Error: Channel IDs must be integers.")
        return

    intents = discord.Intents.default()
    intents.message_content = True  # Not strictly needed here but good practice

    bot = AutoMessageBot(message, channel_ids, intents=intents)
    bot.run(token)

if __name__ == "__main__":
    main()
