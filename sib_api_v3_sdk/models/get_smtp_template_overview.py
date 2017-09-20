# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetSmtpTemplateOverview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'id': 'int',
        'name': 'str',
        'subject': 'str',
        'is_active': 'bool',
        'test_sent': 'bool',
        'sender': 'GetSmtpTemplateOverviewSender',
        'reply_to': 'str',
        'to_field': 'str',
        'tag': 'str',
        'html_content': 'str',
        'created_at': 'str',
        'modified_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subject': 'subject',
        'is_active': 'isActive',
        'test_sent': 'testSent',
        'sender': 'sender',
        'reply_to': 'replyTo',
        'to_field': 'toField',
        'tag': 'tag',
        'html_content': 'htmlContent',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, id=None, name=None, subject=None, is_active=None, test_sent=None, sender=None, reply_to=None, to_field=None, tag=None, html_content=None, created_at=None, modified_at=None):
        """
        GetSmtpTemplateOverview - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._subject = None
        self._is_active = None
        self._test_sent = None
        self._sender = None
        self._reply_to = None
        self._to_field = None
        self._tag = None
        self._html_content = None
        self._created_at = None
        self._modified_at = None

        self.id = id
        self.name = name
        self.subject = subject
        self.is_active = is_active
        self.test_sent = test_sent
        if sender is not None:
          self.sender = sender
        self.reply_to = reply_to
        self.to_field = to_field
        self.tag = tag
        self.html_content = html_content
        self.created_at = created_at
        self.modified_at = modified_at

    @property
    def id(self):
        """
        Gets the id of this GetSmtpTemplateOverview.
        ID of the template

        :return: The id of this GetSmtpTemplateOverview.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetSmtpTemplateOverview.
        ID of the template

        :param id: The id of this GetSmtpTemplateOverview.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GetSmtpTemplateOverview.
        Name of the template

        :return: The name of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetSmtpTemplateOverview.
        Name of the template

        :param name: The name of this GetSmtpTemplateOverview.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def subject(self):
        """
        Gets the subject of this GetSmtpTemplateOverview.
        Subject of the template

        :return: The subject of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this GetSmtpTemplateOverview.
        Subject of the template

        :param subject: The subject of this GetSmtpTemplateOverview.
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")

        self._subject = subject

    @property
    def is_active(self):
        """
        Gets the is_active of this GetSmtpTemplateOverview.
        Status of template (true=active, false=inactive)

        :return: The is_active of this GetSmtpTemplateOverview.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this GetSmtpTemplateOverview.
        Status of template (true=active, false=inactive)

        :param is_active: The is_active of this GetSmtpTemplateOverview.
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")

        self._is_active = is_active

    @property
    def test_sent(self):
        """
        Gets the test_sent of this GetSmtpTemplateOverview.
        Status of test sending for the template (true=test email has been sent, false=test email has not been sent)

        :return: The test_sent of this GetSmtpTemplateOverview.
        :rtype: bool
        """
        return self._test_sent

    @test_sent.setter
    def test_sent(self, test_sent):
        """
        Sets the test_sent of this GetSmtpTemplateOverview.
        Status of test sending for the template (true=test email has been sent, false=test email has not been sent)

        :param test_sent: The test_sent of this GetSmtpTemplateOverview.
        :type: bool
        """
        if test_sent is None:
            raise ValueError("Invalid value for `test_sent`, must not be `None`")

        self._test_sent = test_sent

    @property
    def sender(self):
        """
        Gets the sender of this GetSmtpTemplateOverview.

        :return: The sender of this GetSmtpTemplateOverview.
        :rtype: GetSmtpTemplateOverviewSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this GetSmtpTemplateOverview.

        :param sender: The sender of this GetSmtpTemplateOverview.
        :type: GetSmtpTemplateOverviewSender
        """

        self._sender = sender

    @property
    def reply_to(self):
        """
        Gets the reply_to of this GetSmtpTemplateOverview.
        Email defined as the \"Reply to\" for the template

        :return: The reply_to of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this GetSmtpTemplateOverview.
        Email defined as the \"Reply to\" for the template

        :param reply_to: The reply_to of this GetSmtpTemplateOverview.
        :type: str
        """
        if reply_to is None:
            raise ValueError("Invalid value for `reply_to`, must not be `None`")

        self._reply_to = reply_to

    @property
    def to_field(self):
        """
        Gets the to_field of this GetSmtpTemplateOverview.
        Customisation of the \"to\" field for the template

        :return: The to_field of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._to_field

    @to_field.setter
    def to_field(self, to_field):
        """
        Sets the to_field of this GetSmtpTemplateOverview.
        Customisation of the \"to\" field for the template

        :param to_field: The to_field of this GetSmtpTemplateOverview.
        :type: str
        """
        if to_field is None:
            raise ValueError("Invalid value for `to_field`, must not be `None`")

        self._to_field = to_field

    @property
    def tag(self):
        """
        Gets the tag of this GetSmtpTemplateOverview.
        Tag of the template

        :return: The tag of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this GetSmtpTemplateOverview.
        Tag of the template

        :param tag: The tag of this GetSmtpTemplateOverview.
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")

        self._tag = tag

    @property
    def html_content(self):
        """
        Gets the html_content of this GetSmtpTemplateOverview.
        HTML content of the template

        :return: The html_content of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._html_content

    @html_content.setter
    def html_content(self, html_content):
        """
        Sets the html_content of this GetSmtpTemplateOverview.
        HTML content of the template

        :param html_content: The html_content of this GetSmtpTemplateOverview.
        :type: str
        """
        if html_content is None:
            raise ValueError("Invalid value for `html_content`, must not be `None`")

        self._html_content = html_content

    @property
    def created_at(self):
        """
        Gets the created_at of this GetSmtpTemplateOverview.
        Creation date of the template (YYYY-MM-DD HH:mm:ss)

        :return: The created_at of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this GetSmtpTemplateOverview.
        Creation date of the template (YYYY-MM-DD HH:mm:ss)

        :param created_at: The created_at of this GetSmtpTemplateOverview.
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")
        if created_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$', created_at):
            raise ValueError("Invalid value for `created_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$/`")

        self._created_at = created_at

    @property
    def modified_at(self):
        """
        Gets the modified_at of this GetSmtpTemplateOverview.
        Last modification date of the template (YYYY-MM-DD HH:mm:ss)

        :return: The modified_at of this GetSmtpTemplateOverview.
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this GetSmtpTemplateOverview.
        Last modification date of the template (YYYY-MM-DD HH:mm:ss)

        :param modified_at: The modified_at of this GetSmtpTemplateOverview.
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")
        if modified_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$', modified_at):
            raise ValueError("Invalid value for `modified_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$/`")

        self._modified_at = modified_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetSmtpTemplateOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other