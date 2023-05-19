# taken from https://youtu.be/tKYefJqtvCA?t=500
import json
d={
    'course_name':'Python',
    'fees':15000
}
print(type(d))
print(d)
f=json.dumps(d) ## json.dump() jo hai hamesha given a Python data type usko json object/data type mein convert karega.
# in short matlab json.dump() is used to dump a non json data type to json
print (type(f))
print (f)
print (d.keys())