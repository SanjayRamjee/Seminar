from flask import Flask, jsonify, abort, make_response, request
import sqlite3

app = Flask(__name__)
#Senator query 2    1/5
@app.route('/congress/senator/party/<party>', methods=['GET'])
def get_senators_by_party(party):
  conn = sqlite3.connect('congress.db')
  query = '''
    select state, fname, lname, 
           (strftime("%d",birthday) || '-' || strftime("%m",birthday) || '-' ||
            strftime("%Y",birthday)) birthday, url, twitter, facebook, youtube
    from SENATOR
    where party = ''' + "'" + party + "'" + '''
    order by state
  '''
  cursor = conn.cursor()
  cursor.execute(query)
  records = cursor.fetchall()
  if len(records) == 0:
    abort(404)
  senators = []
  for record in records:
    senators.append({'state':record[0],'fname':record[1],'lname':record[2],'birthday':record[3],
                     'url':record[4],'twitter':record[5],'facebook':record[6],'youtube':record[7]})
  result = {'senators':senators}
  cursor.close()
  conn.close()
  return jsonify(result)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
#Senator query 1     2/5
@app.route('/congress/senator/<state_code>', methods=['GET'])
def get_senator_state_code(state_code):
    query = '''
select fname, lname, party, 
       (strftime("%d",birthday) || '-' || strftime("%m",birthday) || '-' || strftime("%Y",birthday)) birthday, 
       url, twitter, facebook, youtube
from SENATOR
where state = ''' + "'" + state_code + "'" + '''
order by lname, fname
'''
    conn = sqlite3.connect('congress.db')
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    if len(records) == 0:
        abort(404)
    senators = []
    for record in records:
        senators.append({'state':record[0],'fname':record[1],'lname':record[2],'birthday':record[3],
                        'url':record[4],'twitter':record[5],'facebook':record[6],'youtube':record[7]})
    result = {'senators':senators}
    cursor.close()
    conn.close()
    return jsonify(result)
#Legislator query     3/5
@app.route('/congress/legislator/<state_code>', methods=['GET'])
def get_legislator(state_code):
    conn = sqlite3.connect('congress.db')
    query = '''
    select fname, lname, party, 
        (strftime("%d",birthday) || '-' || strftime("%m",birthday) || '-' || strftime("%Y",birthday)) birthday, 
        url, twitter, facebook, youtube
    from SENATOR
    where state = ''' + "'" + state_code + "'" + '''
    order by lname, fname
    '''
    querytwo = '''
    select fname, lname, party, 
        (strftime("%d",birthday) || '-' || strftime("%m",birthday) || '-' || strftime("%Y",birthday)) birthday, 
        url, twitter, facebook, youtube, district
    from HREP
    where state = ''' + "'" + state_code + "'" + '''
    order by district 
    '''
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.execute(querytwo)
    records = cursor.fetchall()
    if len(records) == 0:
        abort(404)
    senators = []
    for record in records:
        senators.append({'state':record[0],'fname':record[1],'lname':record[2],'birthday':record[3],
                        'url':record[4],'twitter':record[5],'facebook':record[6],'youtube':record[7]})
    result = {'senators':senators}
    cursor.close()
    conn.close()
    return jsonify(result)
#Hrep query 1         4/5
@app.route('/congress/hrep/<state_code>', methods=['GET'])
def hrep_one(state_code):

    query = '''select fname, lname, party, 
        (strftime("%d",birthday) || '-' || strftime("%m",birthday) || '-' || strftime("%Y",birthday)) birthday, url, twitter, facebook, youtube, district
    from HREP
    where state = ''' + "'" + state_code + "'" + '''
    order by district'''
    conn = sqlite3.connect('congress.db')
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    if len(records) == 0:
        abort(404)
    senators = []
    for record in records:
        senators.append({'state':record[0],'fname':record[1],'lname':record[2],'birthday':record[3],
                        'url':record[4],'twitter':record[5],'facebook':record[6],'youtube':record[7]})
    result = {'senators':senators}
    cursor.close()
    conn.close()
    return jsonify(result)
#Hrep query 2           5/5
@app.route('/congress/hrep/party/<party>', methods=['GET'])
def hrep_two(party):
    query = '''
    select state, fname, lname, 
       (strftime("%d",birthday) || '-' || strftime("%m",birthday) || '-' || strftime("%Y",birthday)) birthday, 
       url, twitter, facebook, youtube, district from HREP where party = ''' + "'" + party + "'" + '''
       order by state
     '''
    conn = sqlite3.connect('congress.db')
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    if len(records) == 0:
        abort(404)
    senators = []
    for record in records:
        senators.append({'state':record[0],'fname':record[1],'lname':record[2],'birthday':record[3],
                        'url':record[4],'twitter':record[5],'facebook':record[6],'youtube':record[7]})
    result = {'senators':senators}
    cursor.close()
    conn.close()
    return jsonify(result)
if __name__ == '__main__':
    app.run(host='localhost',port='4000',debug=True)

