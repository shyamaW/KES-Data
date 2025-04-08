from owlready2 import *

# Load your ontology (replace 'your_ontology.owl' with the path to your ontology file)
ontology = get_ontology("your_ontology.owl").load()

# Iterate over each object property in the ontology
for prop in ontology.object_properties():
    print(f"Property: {prop.name}")
    
    # Check and print characteristics
    if prop.is_functional_for:
        print("  - Functional")
    if prop.is_inverse_functional_for:
        print("  - Inverse Functional")
    if prop.is_symmetric_for:
        print("  - Symmetric")
    if prop.is_transitive_for:
        print("  - Transitive")
    if prop.is_reflexive_for:
        print("  - Reflexive")
    if prop.is_irreflexive_for:
        print("  - Irreflexive")
    if prop.is_asymmetric_for:
        print("  - Asymmetric")

    # Print domain and range for reference
    print(f"  - Domain: {[cls.name for cls in prop.domain]}")
    print(f"  - Range: {[cls.name for cls in prop.range]}")
    print()
