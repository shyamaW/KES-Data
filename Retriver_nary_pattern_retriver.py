from owlready2 import*

def detect_n_ary_relationships(ontology):
    ''' 
    n_ary_relationships = []
    all_classes = list(ontology.classes())
    
    for entity in all_classes:
        connected_classes = set()
        # Access entity properties or relations based on library syntax
        for prop in entity.is_a:  # Common way to access properties in ontology libraries
            if hasattr(prop, "range"):  # Check if prop has a range (target classes)
                target_classes = prop.range  # Retrieve target classes for this property
                connected_classes.update(target_classes)
        
        # Check if connected classes exceed binary relation threshold
        if len(connected_classes) >= 3:
            n_ary_relationships.append({
                "central_entity": entity,
                "connected_classes": list(connected_classes)
            })
'''
        # Retrieve all classes in the ontology
    all_classes = list(ontology.classes())

    # Initialize a dictionary to store object properties for each class
    class_object_properties = {}

    # Iterate through each class to extract its object properties
    for owl_class in all_classes:
        object_properties = []

        # Iterate through all object properties in the ontology
        for prop in ontology.object_properties():
            # Check if the class is in the domain of the property
            if owl_class in prop.domain:
                object_properties.append(prop)
        # Store the results in the dictionary
        class_object_properties[owl_class.name] = object_properties
    
    n_ary_relationships = []
    n_ary_pattern_entity = {}
    # Output the classes and their associated object properties
    for cls, props in class_object_properties.items():
        # Check if connected classes exceed binary relation threshold
        if len(props) >= 3:
            print(f"Class: {cls}")
            print("  Object Properties:")
            n_ary_relationships = []
            for obj_prop in props:
                print(f"- : {obj_prop.name} and {obj_prop.range}")
                #range_name = obj_prop.range[0].name if isinstance(obj_prop.range, list) else obj_prop.range.name
                        # Check if range is not empty before accessing it
                if isinstance(obj_prop.range, list) and len(obj_prop.range) > 0:
                    range_name = obj_prop.range[0].name
                else:
                    range_name = "None"  # Or any default value you'd like to assign
               
                    # Check and print characteristics
                if prop.is_functional_for:
                    print("  - Functional")
                #n_ary_relationships.append(obj_prop.name)
                n_ary_relationships.append({"property": obj_prop.name, "range": range_name})
            n_ary_pattern_entity[cls] = n_ary_relationships
    return n_ary_pattern_entity
