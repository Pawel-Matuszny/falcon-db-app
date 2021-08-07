import falcon
from sqlalchemy import select

from engine import *

from model import *
import json

from views import *

app = falcon.App()
app.req_options.auto_parse_form_urlencoded=True

get_list = GetList()
get_object_info = GetObjectInfo()
delete_object = DeleteObject()
update_object = UpdateObject()
health_check = HealthCheck()

app.add_route('/index', get_list)
app.add_route('/get/{var_id:int}', get_object_info)
app.add_route('/delete/{var_id:int}', delete_object)
app.add_route('/update/{var_id:int}', update_object)
app.add_route("/status",  health_check)
