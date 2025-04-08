import Extractor_subclass_individual_extractor
import ontology_importer
import Retriver_ontology_entity
import json

def get_subclass_from_onto(ontology_path):
    ontology = ontology_importer.ontology_reader(ontology_path)
    subclasses = Retriver_ontology_entity.entity_subclass_list(ontology)
    return subclasses

def get_classes_properties(ontology_path, classList):
    ontology = ontology_importer.ontology_reader(ontology_path)
    subclasses = Retriver_ontology_entity.data_property_list_for_classes(ontology, classList)
    return subclasses
    
def get_subclass_pattern_from_doc (user_data,doc,doctype,pages):    
# Define the ontology structure with classes, subclasses, and data properties
    data = {
        "classes": {
            "Crop": {
                "subclasses": {
                    "variety":{
                        "data_properties": [
                            "average_yield",
                            "average_yield_unit", 
                            "features", 
                            "average plant height",
                            "average plant height units",
                            "maturity period",
                            "maturity period units"
                        ]
                    }
                }
            }
        }
    }

    # Convert the dictionary to a JSON string
    json_classes = json.dumps(data, indent=4)

    #Testing SubClasses pattern based individual extraction
    #parameters: subclasses: List/JSON ,docpath: file path ,doc_type: pdf or excel, pages: if pdf, sheet_name: if excel
    respones = Extractor_subclass_individual_extractor.get_subclass_individual(json_classes,'./PDF/rice india part1.pdf','pdf',3,None)
    #respones = subclass_individual_extractor.get_subclass_individual(json_classes,'./POPs/homegarden_brinjal_v9.xlsx','excel',None,"Variety - small")
    return respones