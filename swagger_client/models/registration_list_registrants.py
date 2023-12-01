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

class RegistrationListRegistrants(object):
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
        'id': 'str',
        'address': 'str',
        'city': 'str',
        'comments': 'str',
        'country': 'str',
        'custom_questions': 'list[MeetingsmeetingIdrecordingsregistrantsCustomQuestions]',
        'email': 'str',
        'first_name': 'str',
        'industry': 'str',
        'job_title': 'str',
        'last_name': 'str',
        'no_of_employees': 'str',
        'org': 'str',
        'phone': 'str',
        'purchasing_time_frame': 'str',
        'role_in_purchase_process': 'str',
        'state': 'str',
        'status': 'str',
        'zip': 'str',
        'create_time': 'datetime',
        'join_url': 'str',
        'participant_pin_code': 'int'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'city': 'city',
        'comments': 'comments',
        'country': 'country',
        'custom_questions': 'custom_questions',
        'email': 'email',
        'first_name': 'first_name',
        'industry': 'industry',
        'job_title': 'job_title',
        'last_name': 'last_name',
        'no_of_employees': 'no_of_employees',
        'org': 'org',
        'phone': 'phone',
        'purchasing_time_frame': 'purchasing_time_frame',
        'role_in_purchase_process': 'role_in_purchase_process',
        'state': 'state',
        'status': 'status',
        'zip': 'zip',
        'create_time': 'create_time',
        'join_url': 'join_url',
        'participant_pin_code': 'participant_pin_code'
    }

    def __init__(self, id=None, address=None, city=None, comments=None, country=None, custom_questions=None, email=None, first_name=None, industry=None, job_title=None, last_name=None, no_of_employees=None, org=None, phone=None, purchasing_time_frame=None, role_in_purchase_process=None, state=None, status=None, zip=None, create_time=None, join_url=None, participant_pin_code=None):  # noqa: E501
        """RegistrationListRegistrants - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._address = None
        self._city = None
        self._comments = None
        self._country = None
        self._custom_questions = None
        self._email = None
        self._first_name = None
        self._industry = None
        self._job_title = None
        self._last_name = None
        self._no_of_employees = None
        self._org = None
        self._phone = None
        self._purchasing_time_frame = None
        self._role_in_purchase_process = None
        self._state = None
        self._status = None
        self._zip = None
        self._create_time = None
        self._join_url = None
        self._participant_pin_code = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if comments is not None:
            self.comments = comments
        if country is not None:
            self.country = country
        if custom_questions is not None:
            self.custom_questions = custom_questions
        self.email = email
        self.first_name = first_name
        if industry is not None:
            self.industry = industry
        if job_title is not None:
            self.job_title = job_title
        if last_name is not None:
            self.last_name = last_name
        if no_of_employees is not None:
            self.no_of_employees = no_of_employees
        if org is not None:
            self.org = org
        if phone is not None:
            self.phone = phone
        if purchasing_time_frame is not None:
            self.purchasing_time_frame = purchasing_time_frame
        if role_in_purchase_process is not None:
            self.role_in_purchase_process = role_in_purchase_process
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if zip is not None:
            self.zip = zip
        if create_time is not None:
            self.create_time = create_time
        if join_url is not None:
            self.join_url = join_url
        if participant_pin_code is not None:
            self.participant_pin_code = participant_pin_code

    @property
    def id(self):
        """Gets the id of this RegistrationListRegistrants.  # noqa: E501

        Registrant ID.  # noqa: E501

        :return: The id of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RegistrationListRegistrants.

        Registrant ID.  # noqa: E501

        :param id: The id of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this RegistrationListRegistrants.  # noqa: E501

        The registrant's address.  # noqa: E501

        :return: The address of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RegistrationListRegistrants.

        The registrant's address.  # noqa: E501

        :param address: The address of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this RegistrationListRegistrants.  # noqa: E501

        The registrant's city.  # noqa: E501

        :return: The city of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this RegistrationListRegistrants.

        The registrant's city.  # noqa: E501

        :param city: The city of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def comments(self):
        """Gets the comments of this RegistrationListRegistrants.  # noqa: E501

        The registrant's questions and comments.  # noqa: E501

        :return: The comments of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RegistrationListRegistrants.

        The registrant's questions and comments.  # noqa: E501

        :param comments: The comments of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def country(self):
        """Gets the country of this RegistrationListRegistrants.  # noqa: E501

        The registrant's two-letter [country code](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).  # noqa: E501

        :return: The country of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this RegistrationListRegistrants.

        The registrant's two-letter [country code](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).  # noqa: E501

        :param country: The country of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def custom_questions(self):
        """Gets the custom_questions of this RegistrationListRegistrants.  # noqa: E501

        Information about custom questions.  # noqa: E501

        :return: The custom_questions of this RegistrationListRegistrants.  # noqa: E501
        :rtype: list[MeetingsmeetingIdrecordingsregistrantsCustomQuestions]
        """
        return self._custom_questions

    @custom_questions.setter
    def custom_questions(self, custom_questions):
        """Sets the custom_questions of this RegistrationListRegistrants.

        Information about custom questions.  # noqa: E501

        :param custom_questions: The custom_questions of this RegistrationListRegistrants.  # noqa: E501
        :type: list[MeetingsmeetingIdrecordingsregistrantsCustomQuestions]
        """

        self._custom_questions = custom_questions

    @property
    def email(self):
        """Gets the email of this RegistrationListRegistrants.  # noqa: E501

        The registrant's email address. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for return value details.  # noqa: E501

        :return: The email of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RegistrationListRegistrants.

        The registrant's email address. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for return value details.  # noqa: E501

        :param email: The email of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this RegistrationListRegistrants.  # noqa: E501

        The registrant's first name.  # noqa: E501

        :return: The first_name of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this RegistrationListRegistrants.

        The registrant's first name.  # noqa: E501

        :param first_name: The first_name of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def industry(self):
        """Gets the industry of this RegistrationListRegistrants.  # noqa: E501

        The registrant's industry.  # noqa: E501

        :return: The industry of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this RegistrationListRegistrants.

        The registrant's industry.  # noqa: E501

        :param industry: The industry of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._industry = industry

    @property
    def job_title(self):
        """Gets the job_title of this RegistrationListRegistrants.  # noqa: E501

        The registrant's job title.  # noqa: E501

        :return: The job_title of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this RegistrationListRegistrants.

        The registrant's job title.  # noqa: E501

        :param job_title: The job_title of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def last_name(self):
        """Gets the last_name of this RegistrationListRegistrants.  # noqa: E501

        The registrant's last name.  # noqa: E501

        :return: The last_name of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this RegistrationListRegistrants.

        The registrant's last name.  # noqa: E501

        :param last_name: The last_name of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def no_of_employees(self):
        """Gets the no_of_employees of this RegistrationListRegistrants.  # noqa: E501

        The registrant's number of employees.  * `1-20`  * `21-50`  * `51-100`  * `101-250`  * `251-500`  * `501-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`  # noqa: E501

        :return: The no_of_employees of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._no_of_employees

    @no_of_employees.setter
    def no_of_employees(self, no_of_employees):
        """Sets the no_of_employees of this RegistrationListRegistrants.

        The registrant's number of employees.  * `1-20`  * `21-50`  * `51-100`  * `101-250`  * `251-500`  * `501-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`  # noqa: E501

        :param no_of_employees: The no_of_employees of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "1-20", "21-50", "51-100", "101-250", "251-500", "501-1,000", "1,001-5,000", "5,001-10,000", "More than 10,000"]  # noqa: E501
        if no_of_employees not in allowed_values:
            raise ValueError(
                "Invalid value for `no_of_employees` ({0}), must be one of {1}"  # noqa: E501
                .format(no_of_employees, allowed_values)
            )

        self._no_of_employees = no_of_employees

    @property
    def org(self):
        """Gets the org of this RegistrationListRegistrants.  # noqa: E501

        The registrant's organization.  # noqa: E501

        :return: The org of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this RegistrationListRegistrants.

        The registrant's organization.  # noqa: E501

        :param org: The org of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def phone(self):
        """Gets the phone of this RegistrationListRegistrants.  # noqa: E501

        The registrant's phone number.  # noqa: E501

        :return: The phone of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this RegistrationListRegistrants.

        The registrant's phone number.  # noqa: E501

        :param phone: The phone of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def purchasing_time_frame(self):
        """Gets the purchasing_time_frame of this RegistrationListRegistrants.  # noqa: E501

        The registrant's purchasing time frame.  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`  # noqa: E501

        :return: The purchasing_time_frame of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_time_frame

    @purchasing_time_frame.setter
    def purchasing_time_frame(self, purchasing_time_frame):
        """Sets the purchasing_time_frame of this RegistrationListRegistrants.

        The registrant's purchasing time frame.  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`  # noqa: E501

        :param purchasing_time_frame: The purchasing_time_frame of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "Within a month", "1-3 months", "4-6 months", "More than 6 months", "No timeframe"]  # noqa: E501
        if purchasing_time_frame not in allowed_values:
            raise ValueError(
                "Invalid value for `purchasing_time_frame` ({0}), must be one of {1}"  # noqa: E501
                .format(purchasing_time_frame, allowed_values)
            )

        self._purchasing_time_frame = purchasing_time_frame

    @property
    def role_in_purchase_process(self):
        """Gets the role_in_purchase_process of this RegistrationListRegistrants.  # noqa: E501

        The registrant's role in the purchase process.  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`  # noqa: E501

        :return: The role_in_purchase_process of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._role_in_purchase_process

    @role_in_purchase_process.setter
    def role_in_purchase_process(self, role_in_purchase_process):
        """Sets the role_in_purchase_process of this RegistrationListRegistrants.

        The registrant's role in the purchase process.  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`  # noqa: E501

        :param role_in_purchase_process: The role_in_purchase_process of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "Decision Maker", "Evaluator/Recommender", "Influencer", "Not involved"]  # noqa: E501
        if role_in_purchase_process not in allowed_values:
            raise ValueError(
                "Invalid value for `role_in_purchase_process` ({0}), must be one of {1}"  # noqa: E501
                .format(role_in_purchase_process, allowed_values)
            )

        self._role_in_purchase_process = role_in_purchase_process

    @property
    def state(self):
        """Gets the state of this RegistrationListRegistrants.  # noqa: E501

        The registrant's state or province.  # noqa: E501

        :return: The state of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RegistrationListRegistrants.

        The registrant's state or province.  # noqa: E501

        :param state: The state of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this RegistrationListRegistrants.  # noqa: E501

        The status of the registrant's registration.      `approved`: User has been successfully approved for the webinar.     `pending`:  The registration is still pending.     `denied`: User has been denied from joining the webinar.  # noqa: E501

        :return: The status of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RegistrationListRegistrants.

        The status of the registrant's registration.      `approved`: User has been successfully approved for the webinar.     `pending`:  The registration is still pending.     `denied`: User has been denied from joining the webinar.  # noqa: E501

        :param status: The status of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """
        allowed_values = ["approved", "denied", "pending"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def zip(self):
        """Gets the zip of this RegistrationListRegistrants.  # noqa: E501

        The registrant's ZIP or postal code.  # noqa: E501

        :return: The zip of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this RegistrationListRegistrants.

        The registrant's ZIP or postal code.  # noqa: E501

        :param zip: The zip of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def create_time(self):
        """Gets the create_time of this RegistrationListRegistrants.  # noqa: E501

        The time at which the registrant registered.  # noqa: E501

        :return: The create_time of this RegistrationListRegistrants.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RegistrationListRegistrants.

        The time at which the registrant registered.  # noqa: E501

        :param create_time: The create_time of this RegistrationListRegistrants.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def join_url(self):
        """Gets the join_url of this RegistrationListRegistrants.  # noqa: E501

        The URL using which an approved registrant can join the meeting or webinar.  # noqa: E501

        :return: The join_url of this RegistrationListRegistrants.  # noqa: E501
        :rtype: str
        """
        return self._join_url

    @join_url.setter
    def join_url(self, join_url):
        """Sets the join_url of this RegistrationListRegistrants.

        The URL using which an approved registrant can join the meeting or webinar.  # noqa: E501

        :param join_url: The join_url of this RegistrationListRegistrants.  # noqa: E501
        :type: str
        """

        self._join_url = join_url

    @property
    def participant_pin_code(self):
        """Gets the participant_pin_code of this RegistrationListRegistrants.  # noqa: E501

        The participant PIN code is used to authenticate audio participants before they join the meeting.  # noqa: E501

        :return: The participant_pin_code of this RegistrationListRegistrants.  # noqa: E501
        :rtype: int
        """
        return self._participant_pin_code

    @participant_pin_code.setter
    def participant_pin_code(self, participant_pin_code):
        """Sets the participant_pin_code of this RegistrationListRegistrants.

        The participant PIN code is used to authenticate audio participants before they join the meeting.  # noqa: E501

        :param participant_pin_code: The participant_pin_code of this RegistrationListRegistrants.  # noqa: E501
        :type: int
        """

        self._participant_pin_code = participant_pin_code

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
        if issubclass(RegistrationListRegistrants, dict):
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
        if not isinstance(other, RegistrationListRegistrants):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
