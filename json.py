import json

def convertToJson():
    pd = {'first':'Bob',
          'last':'Ross',
          'age':'15',
          'hobby': None,
          'abc':'123'
          }
    pd_json = json.dumps(pd)
    print(pd_json)

    load_json = (json.loads(pd_json))
    print(load_json.values())

    target = 'Ross'
    for key,val in load_json.items():
        if val == target:
            print(key)

    with open('person.txt','w') as json_file:
        json.dump(load_json, json_file)

def main():
    '''
    json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    #pjson = (json.loads(json_data))

    loaded_json = (json.loads(json_data))
    for x in loaded_json: 
        print("%s: %d" % (x, loaded_json[x]))
    
    # print(pjson['a'])


    #Pretty Printing JSON string back
    print(json.dumps(person_dict, indent = 4, sort_keys=True))
    '''
    convertToJson()
if __name__ == "__main__":
    main() 