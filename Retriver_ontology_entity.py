from owlready2 import*
#T-box Classes
def entity_class_List(onto):
    #Retrive classes from the ontology
    print("Classes:")
    all_classes = list(onto.classes())
    #Print all classes in the ontology
    for owl_class in all_classes:
        print(owl_class)
        print(owl_class.iri)

#T-box SubClasses
def entity_subclass_list(onto):
    # Retrieve classes from the ontology
    print("Classes and Subclasses:")
    all_classes = list(onto.classes())
    sub_classes_list = {}
    # Iterate through each class
    for owl_class in all_classes:
        print(f"Class: {owl_class.name}")
        print(f"  IRI: {owl_class.iri}")
        
        # Retrieve and print subclasses
        subclasses = list(owl_class.subclasses())
        if subclasses:
            print("  Subclasses:")
            for subclass in subclasses:
                print(f"    - {subclass.name}")
        else:
            print("  Subclasses: None")
        print("-" * 40)  # Separator for readability
        sub_classes_list [owl_class.name] = subclasses
    return sub_classes_list

#T-box OP
def entity_object_protery_List(onto):
    # List all object properties
    print("Object Properties:")
    biary_relationships = []
    for obj_prop in onto.object_properties():
    # if isinstance(obj_prop, ObjectProperty):
        print(obj_prop.iri)
         # Check if domain is not empty before accessing it
        if isinstance(obj_prop.domain, list) and len(obj_prop.domain) > 0:
            domain_name = obj_prop.domain[0].name
        else:
            domain_name = "None"  # Or any default value you'd like to assign
        
        # Check if range is not empty before accessing it
        if isinstance(obj_prop.range, list) and len(obj_prop.range) > 0:
            range_name = obj_prop.range[0].name
        else:
            range_name = "None"  # Or any default value you'd like to assign
        print(f"- : {obj_prop.name} and {domain_name} and {range_name}")
        biary_relationships.append({"object_property": obj_prop.name, "domain":domain_name, "range": range_name})
    return biary_relationships

#T-box Data property
def entity_data_property_List(onto):
    # List all data properties
    print("\nData Properties:")
    for data_prop in onto.data_properties():
        #if isinstance(data_prop, DataProperty):
        print(data_prop.iri)

#T-box Data property for Classes
def data_property_list_for_classes (onto,owlclasses):
    class_data_properties = {}

    # Retrieve all classes from the ontology
    all_classes = list(onto.classes())
    #all_classes = owlclasses
    
    for owl_class in all_classes:
        # Initialize a dictionary for the current class
        class_info = {"IRI": owl_class.iri, "DataProperties": []}
        
        # Retrieve data properties associated with the class
        for data_prop in onto.data_properties():
            if owl_class in data_prop.domain:
                data_property_info = {
                    "name": data_prop.name,
                    "range": [r for r in data_prop.range] if data_prop.range else None
                }
                class_info["DataProperties"].append(data_property_info)
        
        # Add the class info to the result dictionary
        class_data_properties[owl_class.name] = class_info
    return class_data_properties

# A- box
def individual_attributes (onto):
    individuals_data = {}
    # Retrieve all individuals and their relationships and axioms
    for ind in onto.individuals():
        individual_info = {"Relationships": {}, "Class": []}

        # Get relationships
        for prop in ind.get_properties():
            values = getattr(ind, prop.name)
            if values:
                individual_info["Relationships"][prop.name] = [str(value) for value in values]

        # Get axioms (class types)
        individual_info["Class"] = [str(class_type) for class_type in ind.is_a]

        # Add to the dictionary with the individual's name as the key
        individuals_data[ind.name] = individual_info
    return individuals_data

#A-box
def listOfIndividualsforObjectProperty (object_Property_Name):
    print (type (object_Property_Name.get_relations()))
    generated_list = list(object_Property_Name.get_relations())
    print(generated_list)
