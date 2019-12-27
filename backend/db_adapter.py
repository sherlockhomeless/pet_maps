import psycopg2


database_name = "khama"
user_name = "khama"
pw = "khama"


def get_postgis_connection():
    return psycopg2.connect(database=database_name, user=user_name, host='localhost', password='khama')


def get_cursor():
    return get_postgis_connection().cursor()


def get_all_suburbs():
    cur = get_cursor()
    cur.execute("""
    SELECT tags
    FROM planet_osm_polygon
    """)
    res = cur.fetchall()
    list_suburbs = []
    for elem in res:
        elem = elem[0]
        # if tag-attribute is empty
        if len(elem) == 0:
            continue
        if 'suburb' in elem:
            try:
                sub_name = elem.split('suburb"=>"')[1].split('"')[0]
                if sub_name not in list_suburbs:
                    list_suburbs.append(sub_name)
            except IndexError:
                continue
    print(list_suburbs)


def test_connection():
    cur = get_cursor()
    cur.execute("""
    SELECT amenity
    FROM planet_osm_polygon
    WHERE amenity IS NOT NULL;
    """)
    print("should be 'biergarten':", cur.fetchone())
    return True

