from typing import Union
import rubpy

class GetMessages:
    """
    Provides a method to Retrieve list of messages by

    Methods:
    - get_messages: Retrieve list of messages by

    Attributes:
    - self (rubpy.Client): The rubpy client instance.
    - object_guid (str): The GUID of the object to which the messages belong.
    - message_id (Union[str, int]): The ID or list of IDs of the messages to retrieve.
    - sort (str): The sort order of the messages (FromMax, FromMin). Default is 'FromMax'.
    """

    async def get_messages(
            self: "rubpy.Client",
            object_guid: str,
            message_id: Union[str, int],
            sort: str = 'FromMax',
    ) -> rubpy.types.Update:
        """
        Retrieve messages by their IDs.

        Parameters:
        - object_guid (str): The GUID of the object to which the messages belong.
        - message_ids (Union[str, list]): The ID or list of IDs of the messages to retrieve.

        Returns:
        - rubpy.types.Update: The retrieved messages identified by their IDs.
        """
        if isinstance(message_id, str):
            message_id = int(message_id)

        key_id = 'max_id'
        if sort == 'FromMin':
            key_id = 'min_id'

        return await self.builder('getMessages',
                                  input={
                                      'object_guid': object_guid,
                                      'sort': sort,
                                      key_id: message_id,
                                  })
