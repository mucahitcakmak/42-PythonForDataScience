def NULL_not_found(object: any) -> int:
    
    flag = 0
    object_type = type(object)
    
    if object is None:
        print(f"Nothing: {object} {object_type}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {object_type}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {object_type}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {object_type}")
    elif isinstance(object, str) and len(object) == 0:
        print(f"Empty: {object_type}")
    else:
        print("Type not Found")
        flag = 1

    return flag