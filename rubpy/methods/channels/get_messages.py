import rubpy
from rubpy.types import Update

class GetMessages:
    async def get_messages(
            self: "rubpy.Client",
            channel_guid: str,
    ) -> Update:
        """
        Get information about a channel.

        Parameters:
        - channel_guid (str): The GUID of the channel.

        Returns:
        rubpy.types.Update: The result of the API call.
        """
        return await self.builder('getLastMessageId', input={'channel_guid': channel_guid})