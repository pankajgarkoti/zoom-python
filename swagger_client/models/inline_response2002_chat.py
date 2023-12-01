# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2002Chat(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_bots_chat': 'bool',
        'share_files': 'InlineResponse2002ChatShareFiles',
        'chat_emojis': 'AccountsaccountIdsettingsChatChatEmojis',
        'record_voice_messages': 'bool',
        'record_video_messages': 'bool',
        'screen_capture': 'bool',
        'create_public_channels': 'bool',
        'create_private_channels': 'bool',
        'share_links_in_chat': 'bool',
        'schedule_meetings_in_chat': 'bool',
        'set_retention_period_in_cloud': 'AccountsaccountIdsettingsChatSetRetentionPeriodInCloud',
        'set_retention_period_in_local': 'AccountsaccountIdsettingsChatSetRetentionPeriodInLocal',
        'allow_users_to_add_contacts': 'InlineResponse2002ChatAllowUsersToAddContacts',
        'allow_users_to_chat_with_others': 'InlineResponse2002ChatAllowUsersToChatWithOthers',
        'chat_etiquette_tool': 'InlineResponse2002ChatChatEtiquetteTool',
        'send_data_to_third_party_archiving_service': 'InlineResponse2002ChatSendDataToThirdPartyArchivingService',
        'apply_local_storage_to_personal_channel': 'AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel',
        'translate_messages': 'bool',
        'search_and_send_animated_gif_images': 'AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages'
    }

    attribute_map = {
        'allow_bots_chat': 'allow_bots_chat',
        'share_files': 'share_files',
        'chat_emojis': 'chat_emojis',
        'record_voice_messages': 'record_voice_messages',
        'record_video_messages': 'record_video_messages',
        'screen_capture': 'screen_capture',
        'create_public_channels': 'create_public_channels',
        'create_private_channels': 'create_private_channels',
        'share_links_in_chat': 'share_links_in_chat',
        'schedule_meetings_in_chat': 'schedule_meetings_in_chat',
        'set_retention_period_in_cloud': 'set_retention_period_in_cloud',
        'set_retention_period_in_local': 'set_retention_period_in_local',
        'allow_users_to_add_contacts': 'allow_users_to_add_contacts',
        'allow_users_to_chat_with_others': 'allow_users_to_chat_with_others',
        'chat_etiquette_tool': 'chat_etiquette_tool',
        'send_data_to_third_party_archiving_service': 'send_data_to_third_party_archiving_service',
        'apply_local_storage_to_personal_channel': 'apply_local_storage_to_personal_channel',
        'translate_messages': 'translate_messages',
        'search_and_send_animated_gif_images': 'search_and_send_animated_gif_images'
    }

    def __init__(self, allow_bots_chat=None, share_files=None, chat_emojis=None, record_voice_messages=None, record_video_messages=None, screen_capture=None, create_public_channels=None, create_private_channels=None, share_links_in_chat=None, schedule_meetings_in_chat=None, set_retention_period_in_cloud=None, set_retention_period_in_local=None, allow_users_to_add_contacts=None, allow_users_to_chat_with_others=None, chat_etiquette_tool=None, send_data_to_third_party_archiving_service=None, apply_local_storage_to_personal_channel=None, translate_messages=None, search_and_send_animated_gif_images=None):  # noqa: E501
        """InlineResponse2002Chat - a model defined in Swagger"""  # noqa: E501
        self._allow_bots_chat = None
        self._share_files = None
        self._chat_emojis = None
        self._record_voice_messages = None
        self._record_video_messages = None
        self._screen_capture = None
        self._create_public_channels = None
        self._create_private_channels = None
        self._share_links_in_chat = None
        self._schedule_meetings_in_chat = None
        self._set_retention_period_in_cloud = None
        self._set_retention_period_in_local = None
        self._allow_users_to_add_contacts = None
        self._allow_users_to_chat_with_others = None
        self._chat_etiquette_tool = None
        self._send_data_to_third_party_archiving_service = None
        self._apply_local_storage_to_personal_channel = None
        self._translate_messages = None
        self._search_and_send_animated_gif_images = None
        self.discriminator = None
        if allow_bots_chat is not None:
            self.allow_bots_chat = allow_bots_chat
        if share_files is not None:
            self.share_files = share_files
        if chat_emojis is not None:
            self.chat_emojis = chat_emojis
        if record_voice_messages is not None:
            self.record_voice_messages = record_voice_messages
        if record_video_messages is not None:
            self.record_video_messages = record_video_messages
        if screen_capture is not None:
            self.screen_capture = screen_capture
        if create_public_channels is not None:
            self.create_public_channels = create_public_channels
        if create_private_channels is not None:
            self.create_private_channels = create_private_channels
        if share_links_in_chat is not None:
            self.share_links_in_chat = share_links_in_chat
        if schedule_meetings_in_chat is not None:
            self.schedule_meetings_in_chat = schedule_meetings_in_chat
        if set_retention_period_in_cloud is not None:
            self.set_retention_period_in_cloud = set_retention_period_in_cloud
        if set_retention_period_in_local is not None:
            self.set_retention_period_in_local = set_retention_period_in_local
        if allow_users_to_add_contacts is not None:
            self.allow_users_to_add_contacts = allow_users_to_add_contacts
        if allow_users_to_chat_with_others is not None:
            self.allow_users_to_chat_with_others = allow_users_to_chat_with_others
        if chat_etiquette_tool is not None:
            self.chat_etiquette_tool = chat_etiquette_tool
        if send_data_to_third_party_archiving_service is not None:
            self.send_data_to_third_party_archiving_service = send_data_to_third_party_archiving_service
        if apply_local_storage_to_personal_channel is not None:
            self.apply_local_storage_to_personal_channel = apply_local_storage_to_personal_channel
        if translate_messages is not None:
            self.translate_messages = translate_messages
        if search_and_send_animated_gif_images is not None:
            self.search_and_send_animated_gif_images = search_and_send_animated_gif_images

    @property
    def allow_bots_chat(self):
        """Gets the allow_bots_chat of this InlineResponse2002Chat.  # noqa: E501

        Whether chatbots added to chats and channels can read and write messages.  # noqa: E501

        :return: The allow_bots_chat of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._allow_bots_chat

    @allow_bots_chat.setter
    def allow_bots_chat(self, allow_bots_chat):
        """Sets the allow_bots_chat of this InlineResponse2002Chat.

        Whether chatbots added to chats and channels can read and write messages.  # noqa: E501

        :param allow_bots_chat: The allow_bots_chat of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._allow_bots_chat = allow_bots_chat

    @property
    def share_files(self):
        """Gets the share_files of this InlineResponse2002Chat.  # noqa: E501


        :return: The share_files of this InlineResponse2002Chat.  # noqa: E501
        :rtype: InlineResponse2002ChatShareFiles
        """
        return self._share_files

    @share_files.setter
    def share_files(self, share_files):
        """Sets the share_files of this InlineResponse2002Chat.


        :param share_files: The share_files of this InlineResponse2002Chat.  # noqa: E501
        :type: InlineResponse2002ChatShareFiles
        """

        self._share_files = share_files

    @property
    def chat_emojis(self):
        """Gets the chat_emojis of this InlineResponse2002Chat.  # noqa: E501


        :return: The chat_emojis of this InlineResponse2002Chat.  # noqa: E501
        :rtype: AccountsaccountIdsettingsChatChatEmojis
        """
        return self._chat_emojis

    @chat_emojis.setter
    def chat_emojis(self, chat_emojis):
        """Sets the chat_emojis of this InlineResponse2002Chat.


        :param chat_emojis: The chat_emojis of this InlineResponse2002Chat.  # noqa: E501
        :type: AccountsaccountIdsettingsChatChatEmojis
        """

        self._chat_emojis = chat_emojis

    @property
    def record_voice_messages(self):
        """Gets the record_voice_messages of this InlineResponse2002Chat.  # noqa: E501

        Allow users to record voice messages that can be sent in direct messages or group conversations.  # noqa: E501

        :return: The record_voice_messages of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._record_voice_messages

    @record_voice_messages.setter
    def record_voice_messages(self, record_voice_messages):
        """Sets the record_voice_messages of this InlineResponse2002Chat.

        Allow users to record voice messages that can be sent in direct messages or group conversations.  # noqa: E501

        :param record_voice_messages: The record_voice_messages of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._record_voice_messages = record_voice_messages

    @property
    def record_video_messages(self):
        """Gets the record_video_messages of this InlineResponse2002Chat.  # noqa: E501

        Allow users to record video messages that can be sent in direct messages or group conversations. If the file share setting is disabled, they will not be able to record and send video messages.  # noqa: E501

        :return: The record_video_messages of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._record_video_messages

    @record_video_messages.setter
    def record_video_messages(self, record_video_messages):
        """Sets the record_video_messages of this InlineResponse2002Chat.

        Allow users to record video messages that can be sent in direct messages or group conversations. If the file share setting is disabled, they will not be able to record and send video messages.  # noqa: E501

        :param record_video_messages: The record_video_messages of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._record_video_messages = record_video_messages

    @property
    def screen_capture(self):
        """Gets the screen_capture of this InlineResponse2002Chat.  # noqa: E501

        Allow users to take and send screenshots in direct messages or group conversations.  # noqa: E501

        :return: The screen_capture of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._screen_capture

    @screen_capture.setter
    def screen_capture(self, screen_capture):
        """Sets the screen_capture of this InlineResponse2002Chat.

        Allow users to take and send screenshots in direct messages or group conversations.  # noqa: E501

        :param screen_capture: The screen_capture of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._screen_capture = screen_capture

    @property
    def create_public_channels(self):
        """Gets the create_public_channels of this InlineResponse2002Chat.  # noqa: E501

        Allow users to create public channels.  # noqa: E501

        :return: The create_public_channels of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._create_public_channels

    @create_public_channels.setter
    def create_public_channels(self, create_public_channels):
        """Sets the create_public_channels of this InlineResponse2002Chat.

        Allow users to create public channels.  # noqa: E501

        :param create_public_channels: The create_public_channels of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._create_public_channels = create_public_channels

    @property
    def create_private_channels(self):
        """Gets the create_private_channels of this InlineResponse2002Chat.  # noqa: E501

        Allow users to create private channels.  # noqa: E501

        :return: The create_private_channels of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._create_private_channels

    @create_private_channels.setter
    def create_private_channels(self, create_private_channels):
        """Sets the create_private_channels of this InlineResponse2002Chat.

        Allow users to create private channels.  # noqa: E501

        :param create_private_channels: The create_private_channels of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._create_private_channels = create_private_channels

    @property
    def share_links_in_chat(self):
        """Gets the share_links_in_chat of this InlineResponse2002Chat.  # noqa: E501

        Share links to messages and channels in Team Chat.  # noqa: E501

        :return: The share_links_in_chat of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._share_links_in_chat

    @share_links_in_chat.setter
    def share_links_in_chat(self, share_links_in_chat):
        """Sets the share_links_in_chat of this InlineResponse2002Chat.

        Share links to messages and channels in Team Chat.  # noqa: E501

        :param share_links_in_chat: The share_links_in_chat of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._share_links_in_chat = share_links_in_chat

    @property
    def schedule_meetings_in_chat(self):
        """Gets the schedule_meetings_in_chat of this InlineResponse2002Chat.  # noqa: E501

        Schedule a meeting from chat or channel.  # noqa: E501

        :return: The schedule_meetings_in_chat of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._schedule_meetings_in_chat

    @schedule_meetings_in_chat.setter
    def schedule_meetings_in_chat(self, schedule_meetings_in_chat):
        """Sets the schedule_meetings_in_chat of this InlineResponse2002Chat.

        Schedule a meeting from chat or channel.  # noqa: E501

        :param schedule_meetings_in_chat: The schedule_meetings_in_chat of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._schedule_meetings_in_chat = schedule_meetings_in_chat

    @property
    def set_retention_period_in_cloud(self):
        """Gets the set_retention_period_in_cloud of this InlineResponse2002Chat.  # noqa: E501


        :return: The set_retention_period_in_cloud of this InlineResponse2002Chat.  # noqa: E501
        :rtype: AccountsaccountIdsettingsChatSetRetentionPeriodInCloud
        """
        return self._set_retention_period_in_cloud

    @set_retention_period_in_cloud.setter
    def set_retention_period_in_cloud(self, set_retention_period_in_cloud):
        """Sets the set_retention_period_in_cloud of this InlineResponse2002Chat.


        :param set_retention_period_in_cloud: The set_retention_period_in_cloud of this InlineResponse2002Chat.  # noqa: E501
        :type: AccountsaccountIdsettingsChatSetRetentionPeriodInCloud
        """

        self._set_retention_period_in_cloud = set_retention_period_in_cloud

    @property
    def set_retention_period_in_local(self):
        """Gets the set_retention_period_in_local of this InlineResponse2002Chat.  # noqa: E501


        :return: The set_retention_period_in_local of this InlineResponse2002Chat.  # noqa: E501
        :rtype: AccountsaccountIdsettingsChatSetRetentionPeriodInLocal
        """
        return self._set_retention_period_in_local

    @set_retention_period_in_local.setter
    def set_retention_period_in_local(self, set_retention_period_in_local):
        """Sets the set_retention_period_in_local of this InlineResponse2002Chat.


        :param set_retention_period_in_local: The set_retention_period_in_local of this InlineResponse2002Chat.  # noqa: E501
        :type: AccountsaccountIdsettingsChatSetRetentionPeriodInLocal
        """

        self._set_retention_period_in_local = set_retention_period_in_local

    @property
    def allow_users_to_add_contacts(self):
        """Gets the allow_users_to_add_contacts of this InlineResponse2002Chat.  # noqa: E501


        :return: The allow_users_to_add_contacts of this InlineResponse2002Chat.  # noqa: E501
        :rtype: InlineResponse2002ChatAllowUsersToAddContacts
        """
        return self._allow_users_to_add_contacts

    @allow_users_to_add_contacts.setter
    def allow_users_to_add_contacts(self, allow_users_to_add_contacts):
        """Sets the allow_users_to_add_contacts of this InlineResponse2002Chat.


        :param allow_users_to_add_contacts: The allow_users_to_add_contacts of this InlineResponse2002Chat.  # noqa: E501
        :type: InlineResponse2002ChatAllowUsersToAddContacts
        """

        self._allow_users_to_add_contacts = allow_users_to_add_contacts

    @property
    def allow_users_to_chat_with_others(self):
        """Gets the allow_users_to_chat_with_others of this InlineResponse2002Chat.  # noqa: E501


        :return: The allow_users_to_chat_with_others of this InlineResponse2002Chat.  # noqa: E501
        :rtype: InlineResponse2002ChatAllowUsersToChatWithOthers
        """
        return self._allow_users_to_chat_with_others

    @allow_users_to_chat_with_others.setter
    def allow_users_to_chat_with_others(self, allow_users_to_chat_with_others):
        """Sets the allow_users_to_chat_with_others of this InlineResponse2002Chat.


        :param allow_users_to_chat_with_others: The allow_users_to_chat_with_others of this InlineResponse2002Chat.  # noqa: E501
        :type: InlineResponse2002ChatAllowUsersToChatWithOthers
        """

        self._allow_users_to_chat_with_others = allow_users_to_chat_with_others

    @property
    def chat_etiquette_tool(self):
        """Gets the chat_etiquette_tool of this InlineResponse2002Chat.  # noqa: E501


        :return: The chat_etiquette_tool of this InlineResponse2002Chat.  # noqa: E501
        :rtype: InlineResponse2002ChatChatEtiquetteTool
        """
        return self._chat_etiquette_tool

    @chat_etiquette_tool.setter
    def chat_etiquette_tool(self, chat_etiquette_tool):
        """Sets the chat_etiquette_tool of this InlineResponse2002Chat.


        :param chat_etiquette_tool: The chat_etiquette_tool of this InlineResponse2002Chat.  # noqa: E501
        :type: InlineResponse2002ChatChatEtiquetteTool
        """

        self._chat_etiquette_tool = chat_etiquette_tool

    @property
    def send_data_to_third_party_archiving_service(self):
        """Gets the send_data_to_third_party_archiving_service of this InlineResponse2002Chat.  # noqa: E501


        :return: The send_data_to_third_party_archiving_service of this InlineResponse2002Chat.  # noqa: E501
        :rtype: InlineResponse2002ChatSendDataToThirdPartyArchivingService
        """
        return self._send_data_to_third_party_archiving_service

    @send_data_to_third_party_archiving_service.setter
    def send_data_to_third_party_archiving_service(self, send_data_to_third_party_archiving_service):
        """Sets the send_data_to_third_party_archiving_service of this InlineResponse2002Chat.


        :param send_data_to_third_party_archiving_service: The send_data_to_third_party_archiving_service of this InlineResponse2002Chat.  # noqa: E501
        :type: InlineResponse2002ChatSendDataToThirdPartyArchivingService
        """

        self._send_data_to_third_party_archiving_service = send_data_to_third_party_archiving_service

    @property
    def apply_local_storage_to_personal_channel(self):
        """Gets the apply_local_storage_to_personal_channel of this InlineResponse2002Chat.  # noqa: E501


        :return: The apply_local_storage_to_personal_channel of this InlineResponse2002Chat.  # noqa: E501
        :rtype: AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel
        """
        return self._apply_local_storage_to_personal_channel

    @apply_local_storage_to_personal_channel.setter
    def apply_local_storage_to_personal_channel(self, apply_local_storage_to_personal_channel):
        """Sets the apply_local_storage_to_personal_channel of this InlineResponse2002Chat.


        :param apply_local_storage_to_personal_channel: The apply_local_storage_to_personal_channel of this InlineResponse2002Chat.  # noqa: E501
        :type: AccountsaccountIdsettingsChatApplyLocalStorageToPersonalChannel
        """

        self._apply_local_storage_to_personal_channel = apply_local_storage_to_personal_channel

    @property
    def translate_messages(self):
        """Gets the translate_messages of this InlineResponse2002Chat.  # noqa: E501

        Allow users to translate team chat messages. [Learn more].(https://support.zoom.us/hc/en-us/articles/12998089084685)  # noqa: E501

        :return: The translate_messages of this InlineResponse2002Chat.  # noqa: E501
        :rtype: bool
        """
        return self._translate_messages

    @translate_messages.setter
    def translate_messages(self, translate_messages):
        """Sets the translate_messages of this InlineResponse2002Chat.

        Allow users to translate team chat messages. [Learn more].(https://support.zoom.us/hc/en-us/articles/12998089084685)  # noqa: E501

        :param translate_messages: The translate_messages of this InlineResponse2002Chat.  # noqa: E501
        :type: bool
        """

        self._translate_messages = translate_messages

    @property
    def search_and_send_animated_gif_images(self):
        """Gets the search_and_send_animated_gif_images of this InlineResponse2002Chat.  # noqa: E501


        :return: The search_and_send_animated_gif_images of this InlineResponse2002Chat.  # noqa: E501
        :rtype: AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages
        """
        return self._search_and_send_animated_gif_images

    @search_and_send_animated_gif_images.setter
    def search_and_send_animated_gif_images(self, search_and_send_animated_gif_images):
        """Sets the search_and_send_animated_gif_images of this InlineResponse2002Chat.


        :param search_and_send_animated_gif_images: The search_and_send_animated_gif_images of this InlineResponse2002Chat.  # noqa: E501
        :type: AccountsaccountIdsettingsChatSearchAndSendAnimatedGifImages
        """

        self._search_and_send_animated_gif_images = search_and_send_animated_gif_images

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2002Chat, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2002Chat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
