import MySQLdb

def getSqlData(getLatitude, getLongitude):
    db = MySQLdb.connect("localhost", "pyUser", "meiyoumima", "MainDB")

    cursor = db.cursor()

    sql = "SELECT PM, latitude, longitude FROM Data;"

    cursor.execute(sql)
    results = cursor.fetchall()

    PM = 0
    latitude = 0
    longitude = 0
    i = 0

    for row in results:
        PM += row[0]
        latitude += row[1]
        longitude += row[2]
        i += 1

    PM /= i
    latitude /= i
    longitude /= i

    db.close()

    data = {"PM":PM,"latitude":getLatitude,"longitude":getLongitude}
    
    return data
