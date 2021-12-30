import psycopg2


def getConnection():
    conn = psycopg2.connect("dbname=testbackend user=kevin")
    
    return conn

def getSettlementsByCp(cp):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            select s.name,
                   s.codepostal,
                   s.zone,
                   s.id_asenta_munici,
                   ty.name,
                   pos.office
            from settlements s 
            inner join typesettlements ty on s.id_typesett = ty.idsettl
            inner join postaladmins pos on s.id_postal = pos.idpostal
            where s.codepostal = %s;
        """
        cur.execute(query, (cp,))
        result = cur.fetchall()
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        return "Error on the server"

    finally:
        conn.close()

def getSettlementsByName(name):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            select s.name,
                   s.codepostal,
                   s.zone,
                   s.id_asenta_munici,
                   ty.name,
                   pos.office
            from settlements s 
            inner join typesettlements ty on s.id_typesett = ty.idsettl
            inner join postaladmins pos on s.id_postal = pos.idpostal
            where s.name = %s;
        """
        cur.execute(query, (name,))
        result = cur.fetchall()
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        return "Error on the server"

    finally:
        conn.close()

def getMunicipalitiesByName(name):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            select name,
	               id_state
            from municipalities
            where name = %s;
        """
        cur.execute(query, (name,))
        result = cur.fetchall()
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        return "Error on the server"

    finally:
        conn.close()

def getStateByName(name):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            select idstate,
	               name
            from states
            where name = %s;
        """
        cur.execute(query, (name,))
        result = cur.fetchall()
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        return "Error on the server"

    finally:
        conn.close()


def getCity(name):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            select *
            from cities
            where name = %s;
        """
        cur.execute(query, (name,))
        result = cur.fetchall()
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        return "Error on the server"

    finally:
        conn.close()


def insertState(no_state, state):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            insert into states(idstate, name) 
            values(%s, %s);
        """
        cur.execute(query, (no_state, state))
        conn.commit()
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        return False

    finally:
        conn.close()

def insertMunicipality(idmunici, name, state):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query1 = """
            select idstate 
            from states 
            where name = %s
        """
        cur.execute(query1, (state,))
        state_found = cur.fetchone()

        query2 = """
            insert into municipalities(idmunici, name, id_state) 
            values(%s, %s, %s);
        """
        cur.execute(query2, (idmunici, name, state_found[0]))
        conn.commit()
        cur.close()
        return state_found[0]

    except (Exception, psycopg2.DatabaseError) as error:
        return error

    finally:
        conn.close()

def insertSettlement(name, cp, zone, id_ase_muni, typesettl, munici, city, officepos):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            call insertSettlement(%s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        cur.execute(query, (name, cp, zone, id_ase_muni, typesettl, munici, city, officepos))
        conn.commit()
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close()

def insertCity(idcity, name):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            insert into cities(idcity, name) 
            values(%s, %s);
        """
        
        cur.execute(query, (idcity, name))
        conn.commit()
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close()

def insertPostalAdmin(idpostal):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            insert into postaladmins(idpostal, office) 
            values(%s, %s);
        """
        
        cur.execute(query, (idpostal, idpostal))
        conn.commit()
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close()

def getUser(username):
    conn = getConnection()
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE username=%s"
    cur.execute(query, (username,))
    row = cur.fetchone()
    conn.close()
    return row

def getUserId(id):
    conn = getConnection()
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id=%s"
    cur.execute(query, (id,))
    row = cur.fetchone()
    conn.close()
    return row

def insertUser(username, password):
    conn = getConnection()
    cursor = conn.cursor()

    query = "INSERT INTO users(username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))

    conn.commit()
    conn.close()

def getPostalAdmin(name):
    try:
        conn = getConnection()
        cur = conn.cursor()
        query = """
            select *
            from postaladmins
            where name = %s;
        """
        cur.execute(query, (name,))
        result = cur.fetchall()
        cur.close()
        return result

    except (Exception, psycopg2.DatabaseError) as error:
        return "Error on the server"

    finally:
        conn.close()