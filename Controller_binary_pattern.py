#import Retriver_ontology_entity
#import ontology_importer
import Extractor_binary_relation_individual_extractor
''' 
def get_binary_patterns(ontology_path):
    ontology=ontology_importer.ontology_reader(ontology_path)
    binary_relations = Retriver_ontology_entity.entity_object_protery_List(ontology)
    return binary_relations
'''
def get_binary_patterns_data_from_doc(user_data,doc,doctype,pages, sheet):
    binary_relations = '''
    {
    "OntologyAxiom": [
        {
        "Binary_Relation": "Crop IsaffectedBy GrowingProblem"
        "DOMAIN": "Crop",
        "RANGE": "GrowingProblem",
        "OBJECT_PROPERTY": "IsaffectedBy"
        "Annotation": "Crop can be a rice considered in the doc. Growing Problme can be a pest or disease"
        }
    ]
    }
    '''
    #Testing binary relation pattern based individual extraction
    #parameters: binary_relation_individual_extractor: List/JSON ,docpath: file path ,doc_type: pdf or excel, pages: if pdf, sheet_name: if excel
    respones = Extractor_binary_relation_individual_extractor.get_individual_for_binary_relation(binary_relations,'./PDF/rice india part2.pdf','pdf',3,None)
    #respones = Extractor_binary_relation_individual_extractor.get_individual_for_binary_relation(binary_relations,'./POPs/homegarden_brinjal_v9.xlsx','excel',None,"Variety - small")
    return respones
get_binary_patterns_data_from_doc ('','','','','')