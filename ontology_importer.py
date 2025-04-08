from owlready2 import get_ontology

def ontology_reader(path):
    # Specify the path to your ontology file (e.g., `.owl` or `.rdf` file)
    ontology_path = path

    # Load the ontology
    onto = get_ontology(ontology_path).load()

    return onto
