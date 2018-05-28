from influxdb import client as influxdb


class db(object):
    def __init__(self):
        self.db = influxdb.InfluxDBClient("172.17.0.12", 18081, "admin", "gongxifacai", "tick")

    def get_db(self):
        return self.db

if __name__ == '__main__':
    print db().db
    exit(0)
    # db = influxdb.InfluxDBClient("127.0.0.1", 18081, "", "", "tick")
    # sql = "select * from i9888 where time >= '2018-05-23T00:00:00Z' limit 1"
    # result = db.query(sql)
    # print result
    # sql = "select count(volume) from i9888 group by time(1d) tz('Asia/Shanghai')"
    # result = db.query(sql)
    # print result

    sql = "select count(volume) from i9888 where time > '2018-05-24T11:00:00Z' order by time desc limit 1"
    result = influx().query(sql)

    print len(result)