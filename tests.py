from wtforms import Form, fields
from wtforms_test import FormTestCase


class ExampleForm(Form):
    textarea = fields.TextAreaField()
    text = fields.TextField()
    integer = fields.IntegerField()
    datetime = fields.DateTimeField()


class TestFormTestCase(FormTestCase):
    form_class = ExampleForm

    def test_assert_type(self):
        self.assert_type('text', fields.TextField)
        self.assert_type('textarea', fields.TextAreaField)
        self.assert_type('integer', fields.IntegerField)