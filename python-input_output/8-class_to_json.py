def class_to_json(obj):
    """
    return description of dict with a structure data for
    the sérialisation JSO a object.
    
    argu:
        obj: instance of a classe.
        
    return:
        dict: représentatio obj.
    """
    return obj.__dict__

