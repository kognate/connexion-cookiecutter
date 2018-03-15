from unittest import TestCase
import json
import yaml
from swagger_spec_validator import validate_spec_url
import pathlib
from tempfile import NamedTemporaryFile

class TestSwagger(TestCase):

    def setUp(self):
        swagger = pathlib.Path('swagger.yml')
        self.swagger_json_file = NamedTemporaryFile()
        with swagger.open() as s:
            d = json.dumps(yaml.load(s.read()))
            self.swagger_json_file.write(d.encode('utf-8'))
            self.swagger_json_file.seek(0)
            
    def test_swagger_valid(self):
        res = False
        try:
            validate_spec_url("file://{}".format(self.swagger_json_file.name))
            res = True
        except:
            pass
        
        assert res, "This swagger file is not valid"
     
