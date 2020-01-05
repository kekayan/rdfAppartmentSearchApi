from flask import Flask
import sparqlapi as api
app = Flask(__name__)

@app.route('/appartment/<string:name>')
def byName(name):
    return api.searchByAddress(name)

@app.route('/bedroom/<int:rooms>')
def byExactBedRoomCount(rooms):
    return api.bySameBedroom(rooms)

@app.route('/bedroom/<int:rooms>/more')
def byBedRoomCount(rooms):
    return api.byBedroom(rooms)

@app.route('/location/<string:location>')
def byLocation(location):
    return api.byLocation(location)

@app.route('/address/<string:address>')
def byAddress(address):
    return api.searchByAddress(address)

if __name__ == '__main__':
    app.run()