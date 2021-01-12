class NationRepository:

    def __init__(self):
        self.connection_info = { 'host': 'localhost', 'db': 'prj1', 'user': 'root', 'password': 'Pa$$w0rd', 'charset': 'utf8' }
    
    def select_nation_by_name(self, name_key):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select distinct(nation) from air_quality where nation like %s"
        cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["nation"]

        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result


    def select_station_by_nation(self, name_key):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select distinct nation, stn_nm from air_quality where nation like %s"
        cursor.execute(sql, ("%" + name_key + "%",))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["nation", "stn_nm"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

    def show_data_by_station(self, stn):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select nation, obs_dt, stn_nm, no2, o3, co2, so2, pm10, pm25 from air_quality where stn_nm like %s"
        cursor.execute(sql, (stn,))

        rows = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["nation", "obs_dt", "stn_nm", "no2", "o3", "co2", "so2", "pm10", "pm25"]
        
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

