from owlready2 import*

def createClasses (ontology, class_name):
    with ontology:
        NewClass = types.new_class(class_name, (Thing,),)
        print (NewClass.iri)
    return ontology
    #ontology.save("./OntoRepo/phd3.owl","rdfxml")

def createClassesWithIndiduals (ontology, class_name, individual):
    with ontology:
        NewClass = types.new_class(class_name, (Thing,),)
        NewClass (individual)
        print (NewClass.iri)
    return ontology
    #ontology.save("./OntoRepo/phd3.owl","rdfxml")
   

def createSubClasses (ontology, class_name, superClassName):
    with ontology:
        NewClass = types.new_class(class_name, (ontology[superClassName],))   
        print (NewClass.iri)
        print("Saving ontology")
    return ontology
    #ontology.save("./OntoRepo/phd3.owl","rdfxml")
