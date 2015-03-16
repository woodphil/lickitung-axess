from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired
from models import Acode

class AcodeForm(Form):
    acode = TextField('Acode', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.query = None


    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        query = Acode.query.filter_by(id=self.acode.data).first()

        if query is None:
            self.acode.errors.append('Unknown acode')
            return False

        return True
