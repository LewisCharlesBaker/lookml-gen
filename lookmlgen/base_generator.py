"""
    File name: base_generator.py
    Author: joeschmid
    Date created: 4/8/17
"""
import abc
import six

DEFAULT_WARNING_HEADER_COMMENT = \
    """# STOP! This file was generated by an automated process.
# Any edits you make will be lost the next time it is
# re-generated.\n"""


class GeneratorFormatOptions(object):
    """Specify formatting options to be used during LookML generation

    :param indent_spaces: Number of spaces to indent
    :param newline_between_items: Add a newline between items
    :param omit_default_field_type: Leave out 'type: string'
    :param warning_header_comment: Text to use as a comment as the top
                                   of the file warning the user that the
                                   file will get overwritten
    :param omit_time_frames_if_not_set: If no time frame is specified for
                                        a dimension_group field, omit the
                                        time_frames parameter. If timeframes
                                        is not included every timeframe
                                        option will be added to the dimension group.
    :type indent_spaces: int
    :type newline_between_items: bool
    :type omit_default_field_type: bool
    :type warning_header_comment: string
    :type omit_time_frames_if_not_set: bool

    """
    def __init__(self, indent_spaces=2, newline_between_items=True,
                 omit_default_field_type=True, view_fields_alphabetical=True,
                 warning_header_comment=DEFAULT_WARNING_HEADER_COMMENT,
                 omit_time_frames_if_not_set=False):
        self.indent_spaces = indent_spaces
        self.newline_between_items = newline_between_items
        self.omit_default_field_type = omit_default_field_type
        self.warning_header_comment = warning_header_comment
        self.view_fields_alphabetical = view_fields_alphabetical
        self.omit_time_frames_if_not_set = omit_time_frames_if_not_set


@six.add_metaclass(abc.ABCMeta)
class BaseGenerator:
    """ Abstract base class for any subclass that generates LookML

    :param file: File handle of a file open for writing or a
                 StringIO object
    :param format_options: Formatting options to use during generation
    :type file: File handle or StringIO object
    :type format_options:
        :class:`~lookmlgen.base_generator.GeneratorFormatOptions`

    """
    def __init__(self, file=None, format_options=GeneratorFormatOptions()):
        self.file = file
        self.format_options = format_options

    @abc.abstractmethod
    def generate_lookml(self, file=None, format_options=None):
        """ Implement this method in subclasses to generate LookML

        :param file: File handle of a file open for writing or a
                     StringIO object
        :param format_options: Formatting options to use during generation
        :type file: File handle or StringIO object
        :type format_options:
            :class:`~lookmlgen.base_generator.GeneratorFormatOptions`

        """
        raise NotImplementedError(
            'You must implement the generate_lookml() method')

    @classmethod
    def __subclasshook__(cls, C):
        if cls is BaseGenerator:
            if any("generate_lookml" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
