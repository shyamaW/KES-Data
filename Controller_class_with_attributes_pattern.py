import Retriver_ontology_entity
import ontology_importer
import Extractor_individual_property_value_extractor

def get_individuals_attributes_patterns(ontology_path):
    ontology=ontology_importer.ontology_reader(ontology_path)
    #should get attrubutes for general classes
    class_with_attributes = Retriver_ontology_entity.individual_attributes(ontology)
    return class_with_attributes

def get_individual_data_from_doc (class_with_attributes,docpath,doc_type, pages, sheet_name):

    individual_attributes_data = Extractor_individual_property_value_extractor.get_class_property_value(class_with_attributes,docpath,doc_type, pages, sheet_name)
    return individual_attributes_data

#testing for KES
classList = {
     "classes": {
            "SoilType": {
                "data_properties": [
                    "hasmaxphvalue",
                    "hasminphvalue"
                ]
            },
            "Crop": {
                "data_properties": [
                    "scientific_name"
                ]
            }
           
        }
}
#Testing for KES
get_individual_data_from_doc (classList,'./PDF/rice india part1.pdf','pdf',3,None)