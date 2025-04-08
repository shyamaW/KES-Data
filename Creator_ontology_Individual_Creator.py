from owlready2 import*

def createIndividualList(ontology, class_name, new_individual_names):
    with ontology:
         class_to_add = getattr(ontology, class_name)

    # Create individuals dynamically
    for name in new_individual_names:
        new_individual = class_to_add(name=name)
    return ontology

def createIndividual(ontology, class_name, individual_name):
    with ontology:
        class_to_add = getattr(ontology, class_name)
        new_individual = class_to_add(name=individual_name)
    return ontology