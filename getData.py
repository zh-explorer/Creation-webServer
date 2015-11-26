from getSqlData import *
from encodeJson import *
def getData(latitude, longitude):
    SqlData = getSqlData(latitude, longitude)
    jsonData = encodeJson(SqlData)
    return jsonData
