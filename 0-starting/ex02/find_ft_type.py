def all_thing_is_obj(object: any) -> int:
    
    type_whitelist = [list, set, tuple, dict, str]
    object_type = type(object)

    if object_type is str:
        print(f"{object} is in the kitchen : {object_type}")
    elif object_type in type_whitelist:
        print(f"{object_type.__name__.capitalize()} : {object_type}")
    else:
        print("Type not found")

    return 42
