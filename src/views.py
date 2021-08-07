import falcon
from sqlalchemy import select

import sys

from engine import *

from model import *
import json

class GetList:
    def on_get(self, request, response):
        result = Session.query(App_base).order_by(App_base.ID).all()
        response.status = falcon.HTTP_200 
        response.content_type = falcon.MEDIA_TEXT
        response.text = (str(result))
        
class GetObjectInfo:
    def on_get(self, request, response,var_id):
        result = Session.query(App_base).get(var_id)
        response.status = falcon.HTTP_200 
        response.content_type = falcon.MEDIA_TEXT
        if str(result)=="None":
            response.text = '{"record_status":"not_exist"}'
            response.status = falcon.HTTP_204
        else:
            response.text = (str(result))

class DeleteObject:
    def on_get(self, request, response,var_id):
        record = Session.query(App_base).get(var_id)
        response.content_type = falcon.MEDIA_TEXT
        if str(record)=="None":
            response.status = falcon.HTTP_204 
            response.text = '{"record_status":"not_exist"}'
        else:
            record.is_deleted = True
            response.status = falcon.HTTP_202 
            Session.commit()
            response.text = '{"record_status":"deleted"}'

class UpdateObject:
    def on_get(self, request, response,var_id):
        record = Session.query(App_base).get(var_id)
        if record.is_deleted == False:
            response.status = falcon.HTTP_200
            response.content_type = 'text/html'
            response.body = "<form method='POST' action='/update/"+str(var_id)+"' enctype='application/x-www-form-urlencoded'>\
                                <textarea name='text_form'>"+str(record.text)+"</textarea> <br>\
                                <label for='finished'>Is finished:</label>\
                                <select name='finished' id='finished'>\
                                    <option value='finished'>finished</option>\
                                    <option value='not'>not</option>\
                                </select><br>\
                                <input type='submit' value='Update record'>\
                            </form>"
        else:
            response.status = falcon.HTTP_202
            response.content_type = 'text/html'
            response.body = '{"record_status":"deleted"}'

    def on_post(self, request, response, var_id):
        record = Session.query(App_base).get(var_id)
        if record.is_deleted == False :
            text_field = request.get_param("text_form")
            is_finished_field = request.get_param("finished")
            record.text = str(text_field)
            record.status = str(is_finished_field)
            Session.commit()
            response.status = falcon.HTTP_202 
            response.content_type = falcon.MEDIA_TEXT
            response.text = '{"record_status":"updated"}'
        else:
            response.status = falcon.HTTP_204
            response.content_type = 'text/html'
            response.body = '{"record_status":"deleted"}'


class HealthCheck:
    def on_get(self, request, response):
        is_database_working = True
        output = '{"db_status":"ok"}'

        try:
            conn = engine.connect()
            conn.close()
        except Exception as e:
            output = str(e)
            is_database_working = False
            output = '{"db_status":"unavailable"}'

        if is_database_working:
            response.status = falcon.HTTP_200
        else:
            response.status = falcon.HTTP_500

        response.content_type = falcon.MEDIA_TEXT
        response.text = (output)