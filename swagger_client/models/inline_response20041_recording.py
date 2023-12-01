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

class InlineResponse20041Recording(object):
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
        'account_user_access_recording': 'bool',
        'archive': 'InlineResponse20041RecordingArchive',
        'auto_recording': 'str',
        'cloud_recording': 'bool',
        'cloud_recording_download': 'bool',
        'cloud_recording_download_host': 'bool',
        'host_delete_cloud_recording': 'bool',
        'record_files_separately': 'GroupsgroupIdsettingsRecordingRecordFilesSeparately',
        'display_participant_name': 'bool',
        'recording_thumbnails': 'bool',
        'optimize_recording_for_3rd_party_video_editor': 'bool',
        'recording_highlight': 'bool',
        'save_panelist_chat': 'bool',
        'save_poll_results': 'bool',
        'save_close_caption': 'bool',
        'ip_address_access_control': 'GroupsgroupIdlockSettingsRecordingIpAddressAccessControl',
        'local_recording': 'bool',
        'prevent_host_access_recording': 'bool',
        'record_audio_file': 'bool',
        'record_gallery_view': 'bool',
        'record_speaker_view': 'bool',
        'recording_audio_transcript': 'bool',
        'smart_recording': 'AccountsaccountIdsettingsRecordingSmartRecording',
        'save_chat_text': 'bool',
        'show_timestamp': 'bool'
    }

    attribute_map = {
        'account_user_access_recording': 'account_user_access_recording',
        'archive': 'archive',
        'auto_recording': 'auto_recording',
        'cloud_recording': 'cloud_recording',
        'cloud_recording_download': 'cloud_recording_download',
        'cloud_recording_download_host': 'cloud_recording_download_host',
        'host_delete_cloud_recording': 'host_delete_cloud_recording',
        'record_files_separately': 'record_files_separately',
        'display_participant_name': 'display_participant_name',
        'recording_thumbnails': 'recording_thumbnails',
        'optimize_recording_for_3rd_party_video_editor': 'optimize_recording_for_3rd_party_video_editor',
        'recording_highlight': 'recording_highlight',
        'save_panelist_chat': 'save_panelist_chat',
        'save_poll_results': 'save_poll_results',
        'save_close_caption': 'save_close_caption',
        'ip_address_access_control': 'ip_address_access_control',
        'local_recording': 'local_recording',
        'prevent_host_access_recording': 'prevent_host_access_recording',
        'record_audio_file': 'record_audio_file',
        'record_gallery_view': 'record_gallery_view',
        'record_speaker_view': 'record_speaker_view',
        'recording_audio_transcript': 'recording_audio_transcript',
        'smart_recording': 'smart_recording',
        'save_chat_text': 'save_chat_text',
        'show_timestamp': 'show_timestamp'
    }

    def __init__(self, account_user_access_recording=None, archive=None, auto_recording=None, cloud_recording=None, cloud_recording_download=None, cloud_recording_download_host=None, host_delete_cloud_recording=None, record_files_separately=None, display_participant_name=None, recording_thumbnails=None, optimize_recording_for_3rd_party_video_editor=None, recording_highlight=None, save_panelist_chat=None, save_poll_results=None, save_close_caption=None, ip_address_access_control=None, local_recording=None, prevent_host_access_recording=None, record_audio_file=None, record_gallery_view=None, record_speaker_view=None, recording_audio_transcript=None, smart_recording=None, save_chat_text=None, show_timestamp=None):  # noqa: E501
        """InlineResponse20041Recording - a model defined in Swagger"""  # noqa: E501
        self._account_user_access_recording = None
        self._archive = None
        self._auto_recording = None
        self._cloud_recording = None
        self._cloud_recording_download = None
        self._cloud_recording_download_host = None
        self._host_delete_cloud_recording = None
        self._record_files_separately = None
        self._display_participant_name = None
        self._recording_thumbnails = None
        self._optimize_recording_for_3rd_party_video_editor = None
        self._recording_highlight = None
        self._save_panelist_chat = None
        self._save_poll_results = None
        self._save_close_caption = None
        self._ip_address_access_control = None
        self._local_recording = None
        self._prevent_host_access_recording = None
        self._record_audio_file = None
        self._record_gallery_view = None
        self._record_speaker_view = None
        self._recording_audio_transcript = None
        self._smart_recording = None
        self._save_chat_text = None
        self._show_timestamp = None
        self.discriminator = None
        if account_user_access_recording is not None:
            self.account_user_access_recording = account_user_access_recording
        if archive is not None:
            self.archive = archive
        if auto_recording is not None:
            self.auto_recording = auto_recording
        if cloud_recording is not None:
            self.cloud_recording = cloud_recording
        if cloud_recording_download is not None:
            self.cloud_recording_download = cloud_recording_download
        if cloud_recording_download_host is not None:
            self.cloud_recording_download_host = cloud_recording_download_host
        if host_delete_cloud_recording is not None:
            self.host_delete_cloud_recording = host_delete_cloud_recording
        if record_files_separately is not None:
            self.record_files_separately = record_files_separately
        if display_participant_name is not None:
            self.display_participant_name = display_participant_name
        if recording_thumbnails is not None:
            self.recording_thumbnails = recording_thumbnails
        if optimize_recording_for_3rd_party_video_editor is not None:
            self.optimize_recording_for_3rd_party_video_editor = optimize_recording_for_3rd_party_video_editor
        if recording_highlight is not None:
            self.recording_highlight = recording_highlight
        if save_panelist_chat is not None:
            self.save_panelist_chat = save_panelist_chat
        if save_poll_results is not None:
            self.save_poll_results = save_poll_results
        if save_close_caption is not None:
            self.save_close_caption = save_close_caption
        if ip_address_access_control is not None:
            self.ip_address_access_control = ip_address_access_control
        if local_recording is not None:
            self.local_recording = local_recording
        if prevent_host_access_recording is not None:
            self.prevent_host_access_recording = prevent_host_access_recording
        if record_audio_file is not None:
            self.record_audio_file = record_audio_file
        if record_gallery_view is not None:
            self.record_gallery_view = record_gallery_view
        if record_speaker_view is not None:
            self.record_speaker_view = record_speaker_view
        if recording_audio_transcript is not None:
            self.recording_audio_transcript = recording_audio_transcript
        if smart_recording is not None:
            self.smart_recording = smart_recording
        if save_chat_text is not None:
            self.save_chat_text = save_chat_text
        if show_timestamp is not None:
            self.show_timestamp = show_timestamp

    @property
    def account_user_access_recording(self):
        """Gets the account_user_access_recording of this InlineResponse20041Recording.  # noqa: E501

        Make cloud recordings accessible to account members only.  # noqa: E501

        :return: The account_user_access_recording of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._account_user_access_recording

    @account_user_access_recording.setter
    def account_user_access_recording(self, account_user_access_recording):
        """Sets the account_user_access_recording of this InlineResponse20041Recording.

        Make cloud recordings accessible to account members only.  # noqa: E501

        :param account_user_access_recording: The account_user_access_recording of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._account_user_access_recording = account_user_access_recording

    @property
    def archive(self):
        """Gets the archive of this InlineResponse20041Recording.  # noqa: E501


        :return: The archive of this InlineResponse20041Recording.  # noqa: E501
        :rtype: InlineResponse20041RecordingArchive
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        """Sets the archive of this InlineResponse20041Recording.


        :param archive: The archive of this InlineResponse20041Recording.  # noqa: E501
        :type: InlineResponse20041RecordingArchive
        """

        self._archive = archive

    @property
    def auto_recording(self):
        """Gets the auto_recording of this InlineResponse20041Recording.  # noqa: E501

        Record meetings automatically as they start.  # noqa: E501

        :return: The auto_recording of this InlineResponse20041Recording.  # noqa: E501
        :rtype: str
        """
        return self._auto_recording

    @auto_recording.setter
    def auto_recording(self, auto_recording):
        """Sets the auto_recording of this InlineResponse20041Recording.

        Record meetings automatically as they start.  # noqa: E501

        :param auto_recording: The auto_recording of this InlineResponse20041Recording.  # noqa: E501
        :type: str
        """

        self._auto_recording = auto_recording

    @property
    def cloud_recording(self):
        """Gets the cloud_recording of this InlineResponse20041Recording.  # noqa: E501

        Allow hosts to record and save the meeting / webinar in the cloud.  # noqa: E501

        :return: The cloud_recording of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_recording

    @cloud_recording.setter
    def cloud_recording(self, cloud_recording):
        """Sets the cloud_recording of this InlineResponse20041Recording.

        Allow hosts to record and save the meeting / webinar in the cloud.  # noqa: E501

        :param cloud_recording: The cloud_recording of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._cloud_recording = cloud_recording

    @property
    def cloud_recording_download(self):
        """Gets the cloud_recording_download of this InlineResponse20041Recording.  # noqa: E501

        Allow anyone with a link to the cloud recording to download.  # noqa: E501

        :return: The cloud_recording_download of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_recording_download

    @cloud_recording_download.setter
    def cloud_recording_download(self, cloud_recording_download):
        """Sets the cloud_recording_download of this InlineResponse20041Recording.

        Allow anyone with a link to the cloud recording to download.  # noqa: E501

        :param cloud_recording_download: The cloud_recording_download of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._cloud_recording_download = cloud_recording_download

    @property
    def cloud_recording_download_host(self):
        """Gets the cloud_recording_download_host of this InlineResponse20041Recording.  # noqa: E501

        Allow only the host with a link to the cloud recording to download.  # noqa: E501

        :return: The cloud_recording_download_host of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_recording_download_host

    @cloud_recording_download_host.setter
    def cloud_recording_download_host(self, cloud_recording_download_host):
        """Sets the cloud_recording_download_host of this InlineResponse20041Recording.

        Allow only the host with a link to the cloud recording to download.  # noqa: E501

        :param cloud_recording_download_host: The cloud_recording_download_host of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._cloud_recording_download_host = cloud_recording_download_host

    @property
    def host_delete_cloud_recording(self):
        """Gets the host_delete_cloud_recording of this InlineResponse20041Recording.  # noqa: E501

        Allow the host to delete the recordings. If this option is disabled, the recordings cannot be deleted by the host and only admin can delete them.  # noqa: E501

        :return: The host_delete_cloud_recording of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._host_delete_cloud_recording

    @host_delete_cloud_recording.setter
    def host_delete_cloud_recording(self, host_delete_cloud_recording):
        """Sets the host_delete_cloud_recording of this InlineResponse20041Recording.

        Allow the host to delete the recordings. If this option is disabled, the recordings cannot be deleted by the host and only admin can delete them.  # noqa: E501

        :param host_delete_cloud_recording: The host_delete_cloud_recording of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._host_delete_cloud_recording = host_delete_cloud_recording

    @property
    def record_files_separately(self):
        """Gets the record_files_separately of this InlineResponse20041Recording.  # noqa: E501


        :return: The record_files_separately of this InlineResponse20041Recording.  # noqa: E501
        :rtype: GroupsgroupIdsettingsRecordingRecordFilesSeparately
        """
        return self._record_files_separately

    @record_files_separately.setter
    def record_files_separately(self, record_files_separately):
        """Sets the record_files_separately of this InlineResponse20041Recording.


        :param record_files_separately: The record_files_separately of this InlineResponse20041Recording.  # noqa: E501
        :type: GroupsgroupIdsettingsRecordingRecordFilesSeparately
        """

        self._record_files_separately = record_files_separately

    @property
    def display_participant_name(self):
        """Gets the display_participant_name of this InlineResponse20041Recording.  # noqa: E501

        Whether participants' names display in the recording.  # noqa: E501

        :return: The display_participant_name of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._display_participant_name

    @display_participant_name.setter
    def display_participant_name(self, display_participant_name):
        """Sets the display_participant_name of this InlineResponse20041Recording.

        Whether participants' names display in the recording.  # noqa: E501

        :param display_participant_name: The display_participant_name of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._display_participant_name = display_participant_name

    @property
    def recording_thumbnails(self):
        """Gets the recording_thumbnails of this InlineResponse20041Recording.  # noqa: E501

        Whether thumbnails of the presenter are recorded when they are sharing their screen.  # noqa: E501

        :return: The recording_thumbnails of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_thumbnails

    @recording_thumbnails.setter
    def recording_thumbnails(self, recording_thumbnails):
        """Sets the recording_thumbnails of this InlineResponse20041Recording.

        Whether thumbnails of the presenter are recorded when they are sharing their screen.  # noqa: E501

        :param recording_thumbnails: The recording_thumbnails of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._recording_thumbnails = recording_thumbnails

    @property
    def optimize_recording_for_3rd_party_video_editor(self):
        """Gets the optimize_recording_for_3rd_party_video_editor of this InlineResponse20041Recording.  # noqa: E501

        Whether recordings will be optimized for a 3rd party video editor. This can increase the file size and the time it takes to generate recording files.  # noqa: E501

        :return: The optimize_recording_for_3rd_party_video_editor of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_recording_for_3rd_party_video_editor

    @optimize_recording_for_3rd_party_video_editor.setter
    def optimize_recording_for_3rd_party_video_editor(self, optimize_recording_for_3rd_party_video_editor):
        """Sets the optimize_recording_for_3rd_party_video_editor of this InlineResponse20041Recording.

        Whether recordings will be optimized for a 3rd party video editor. This can increase the file size and the time it takes to generate recording files.  # noqa: E501

        :param optimize_recording_for_3rd_party_video_editor: The optimize_recording_for_3rd_party_video_editor of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._optimize_recording_for_3rd_party_video_editor = optimize_recording_for_3rd_party_video_editor

    @property
    def recording_highlight(self):
        """Gets the recording_highlight of this InlineResponse20041Recording.  # noqa: E501

        Whether the [recording highlights](https://support.zoom.us/hc/en-us/articles/360060802432) feature is enabled.  # noqa: E501

        :return: The recording_highlight of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_highlight

    @recording_highlight.setter
    def recording_highlight(self, recording_highlight):
        """Sets the recording_highlight of this InlineResponse20041Recording.

        Whether the [recording highlights](https://support.zoom.us/hc/en-us/articles/360060802432) feature is enabled.  # noqa: E501

        :param recording_highlight: The recording_highlight of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._recording_highlight = recording_highlight

    @property
    def save_panelist_chat(self):
        """Gets the save_panelist_chat of this InlineResponse20041Recording.  # noqa: E501

        Whether panelist chats are saved to the recording.  # noqa: E501

        :return: The save_panelist_chat of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._save_panelist_chat

    @save_panelist_chat.setter
    def save_panelist_chat(self, save_panelist_chat):
        """Sets the save_panelist_chat of this InlineResponse20041Recording.

        Whether panelist chats are saved to the recording.  # noqa: E501

        :param save_panelist_chat: The save_panelist_chat of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._save_panelist_chat = save_panelist_chat

    @property
    def save_poll_results(self):
        """Gets the save_poll_results of this InlineResponse20041Recording.  # noqa: E501

        Whether poll results shared during the meeting or webinar are saved. This also includes poll results shared during the meeting or webinar.  # noqa: E501

        :return: The save_poll_results of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._save_poll_results

    @save_poll_results.setter
    def save_poll_results(self, save_poll_results):
        """Sets the save_poll_results of this InlineResponse20041Recording.

        Whether poll results shared during the meeting or webinar are saved. This also includes poll results shared during the meeting or webinar.  # noqa: E501

        :param save_poll_results: The save_poll_results of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._save_poll_results = save_poll_results

    @property
    def save_close_caption(self):
        """Gets the save_close_caption of this InlineResponse20041Recording.  # noqa: E501

        Whether [closed captions](https://support.zoom.us/hc/en-us/articles/207279736) are saved as a VTT (Video Track Text) file.  # noqa: E501

        :return: The save_close_caption of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._save_close_caption

    @save_close_caption.setter
    def save_close_caption(self, save_close_caption):
        """Sets the save_close_caption of this InlineResponse20041Recording.

        Whether [closed captions](https://support.zoom.us/hc/en-us/articles/207279736) are saved as a VTT (Video Track Text) file.  # noqa: E501

        :param save_close_caption: The save_close_caption of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._save_close_caption = save_close_caption

    @property
    def ip_address_access_control(self):
        """Gets the ip_address_access_control of this InlineResponse20041Recording.  # noqa: E501


        :return: The ip_address_access_control of this InlineResponse20041Recording.  # noqa: E501
        :rtype: GroupsgroupIdlockSettingsRecordingIpAddressAccessControl
        """
        return self._ip_address_access_control

    @ip_address_access_control.setter
    def ip_address_access_control(self, ip_address_access_control):
        """Sets the ip_address_access_control of this InlineResponse20041Recording.


        :param ip_address_access_control: The ip_address_access_control of this InlineResponse20041Recording.  # noqa: E501
        :type: GroupsgroupIdlockSettingsRecordingIpAddressAccessControl
        """

        self._ip_address_access_control = ip_address_access_control

    @property
    def local_recording(self):
        """Gets the local_recording of this InlineResponse20041Recording.  # noqa: E501

        Allow hosts and participants to record the meeting to a local file.  # noqa: E501

        :return: The local_recording of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._local_recording

    @local_recording.setter
    def local_recording(self, local_recording):
        """Sets the local_recording of this InlineResponse20041Recording.

        Allow hosts and participants to record the meeting to a local file.  # noqa: E501

        :param local_recording: The local_recording of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._local_recording = local_recording

    @property
    def prevent_host_access_recording(self):
        """Gets the prevent_host_access_recording of this InlineResponse20041Recording.  # noqa: E501

        If set to `true`, meeting hosts cannot view their meeting cloud recordings. Only the admins who have recording management privilege can access them.    # noqa: E501

        :return: The prevent_host_access_recording of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_host_access_recording

    @prevent_host_access_recording.setter
    def prevent_host_access_recording(self, prevent_host_access_recording):
        """Sets the prevent_host_access_recording of this InlineResponse20041Recording.

        If set to `true`, meeting hosts cannot view their meeting cloud recordings. Only the admins who have recording management privilege can access them.    # noqa: E501

        :param prevent_host_access_recording: The prevent_host_access_recording of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._prevent_host_access_recording = prevent_host_access_recording

    @property
    def record_audio_file(self):
        """Gets the record_audio_file of this InlineResponse20041Recording.  # noqa: E501

        Whether to record one audio file for all participants.  # noqa: E501

        :return: The record_audio_file of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._record_audio_file

    @record_audio_file.setter
    def record_audio_file(self, record_audio_file):
        """Sets the record_audio_file of this InlineResponse20041Recording.

        Whether to record one audio file for all participants.  # noqa: E501

        :param record_audio_file: The record_audio_file of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._record_audio_file = record_audio_file

    @property
    def record_gallery_view(self):
        """Gets the record_gallery_view of this InlineResponse20041Recording.  # noqa: E501

        When someone is sharing their screen, active speaker will show on the top right corner of the shared screen.  # noqa: E501

        :return: The record_gallery_view of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._record_gallery_view

    @record_gallery_view.setter
    def record_gallery_view(self, record_gallery_view):
        """Sets the record_gallery_view of this InlineResponse20041Recording.

        When someone is sharing their screen, active speaker will show on the top right corner of the shared screen.  # noqa: E501

        :param record_gallery_view: The record_gallery_view of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._record_gallery_view = record_gallery_view

    @property
    def record_speaker_view(self):
        """Gets the record_speaker_view of this InlineResponse20041Recording.  # noqa: E501

        Record active speaker with shared screen.  # noqa: E501

        :return: The record_speaker_view of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._record_speaker_view

    @record_speaker_view.setter
    def record_speaker_view(self, record_speaker_view):
        """Sets the record_speaker_view of this InlineResponse20041Recording.

        Record active speaker with shared screen.  # noqa: E501

        :param record_speaker_view: The record_speaker_view of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._record_speaker_view = record_speaker_view

    @property
    def recording_audio_transcript(self):
        """Gets the recording_audio_transcript of this InlineResponse20041Recording.  # noqa: E501

        Automatically transcribe the audio of a meeting or webinar for cloud recordings.  # noqa: E501

        :return: The recording_audio_transcript of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_audio_transcript

    @recording_audio_transcript.setter
    def recording_audio_transcript(self, recording_audio_transcript):
        """Sets the recording_audio_transcript of this InlineResponse20041Recording.

        Automatically transcribe the audio of a meeting or webinar for cloud recordings.  # noqa: E501

        :param recording_audio_transcript: The recording_audio_transcript of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._recording_audio_transcript = recording_audio_transcript

    @property
    def smart_recording(self):
        """Gets the smart_recording of this InlineResponse20041Recording.  # noqa: E501


        :return: The smart_recording of this InlineResponse20041Recording.  # noqa: E501
        :rtype: AccountsaccountIdsettingsRecordingSmartRecording
        """
        return self._smart_recording

    @smart_recording.setter
    def smart_recording(self, smart_recording):
        """Sets the smart_recording of this InlineResponse20041Recording.


        :param smart_recording: The smart_recording of this InlineResponse20041Recording.  # noqa: E501
        :type: AccountsaccountIdsettingsRecordingSmartRecording
        """

        self._smart_recording = smart_recording

    @property
    def save_chat_text(self):
        """Gets the save_chat_text of this InlineResponse20041Recording.  # noqa: E501

        Save chat messages from the meeting or webinar.  # noqa: E501

        :return: The save_chat_text of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._save_chat_text

    @save_chat_text.setter
    def save_chat_text(self, save_chat_text):
        """Sets the save_chat_text of this InlineResponse20041Recording.

        Save chat messages from the meeting or webinar.  # noqa: E501

        :param save_chat_text: The save_chat_text of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._save_chat_text = save_chat_text

    @property
    def show_timestamp(self):
        """Gets the show_timestamp of this InlineResponse20041Recording.  # noqa: E501

        Add a timestamp to the recording.  # noqa: E501

        :return: The show_timestamp of this InlineResponse20041Recording.  # noqa: E501
        :rtype: bool
        """
        return self._show_timestamp

    @show_timestamp.setter
    def show_timestamp(self, show_timestamp):
        """Sets the show_timestamp of this InlineResponse20041Recording.

        Add a timestamp to the recording.  # noqa: E501

        :param show_timestamp: The show_timestamp of this InlineResponse20041Recording.  # noqa: E501
        :type: bool
        """

        self._show_timestamp = show_timestamp

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
        if issubclass(InlineResponse20041Recording, dict):
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
        if not isinstance(other, InlineResponse20041Recording):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other