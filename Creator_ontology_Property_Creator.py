from owlready2 import*

def createObjProperty(ontology, property_name, domain_class, range_class):
    with ontology:
        prop = types.new_class(property_name, (ObjectProperty, FunctionalProperty))
        prop.domain    = [domain_class]
        prop.range     = [range_class]
    return ontology

def createStrDataProperty(ontology, property_name, domain_class):
    with ontology:
        prop = types.new_class(property_name, (DataProperty, FunctionalProperty))
        prop.domain    = [domain_class]
        prop.range     = [str]
    return ontology

def createFloatDataProperty(ontology, property_name, domain_class):
    with ontology:
        prop = types.new_class(property_name, (DataProperty, FunctionalProperty))
        prop.domain    = [domain_class]
        prop.range     = [float]
    return ontology

def createObjPropertyForIndividual (ontology,domainName,object_property_name, rangeName, individual1, individual2):
    
     # Get individual by name
    individual_domain = getattr(ontology, individual1)
    print (f"what this1: {individual_domain}")
    individual_range = getattr(ontology, individual2)
    print (f" what this1: {individual_range}")
    #if object property exist
    object_Property_Name = ontology.__getattr__(object_property_name)
    #object_Property_Name = getattr(ontology, object_property_name)
    print(f"domain{object_Property_Name.domain} and range {object_Property_Name.range}")
    #if the object property already in the ontology
    individual_domain.__setattr__(object_property_name, [individual_range])
    
    print (list (object_Property_Name.get_relations()))

    #if we need to add  object property newly, this code can be used
    '''
    with ontology:
        domainName = getattr(ontology, domainName)
        rangeName = getattr(ontology, rangeName)
        class object_Property_Name(domainName >> rangeName):
            pass
    
    individual_domain.object_Property_Name.append(individual_range)
    print (list (object_Property_Name.get_relations()))
    '''
    return ontology