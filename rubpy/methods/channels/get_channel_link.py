import rubpy
from rubpy.types import Update

class GetChannelLink:
    async def get_channel_link(
            self: "rubpy.Client",
            channel_guid: str,
    ) -> Update:
        """
        Get the join link of a channel.

        Parameters:
        - channel_guid (str): The GUID of the channel.

        Returns:
        rubpy.types.Update: The result of the API call.
        """
        return await self.builder('getChannelLink', input={'channel_guid': channel_guid})
