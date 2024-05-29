def class_to_json(obj):
    """
    return description of dict with a structure data for
    the sérialisation JSO a object.
    
    Arguments:
        obj: instance of a classe.
        
    Returr:
        dict: représentatio obj.
    """
    return obj.__dict__

