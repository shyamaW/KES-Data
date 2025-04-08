#import Extractor_individual_property_value_extractor
#import Controller_binary_pattern
#import Controller_n_ary_pattern
import Controller_subClass_pattern
import json


#read a given ontology
#path="./OntoRepo/CropKB_tbox_original.rdf"
#binary_rel = Controller_binary_pattern.get_binary_patterns(path)
#Controller_binary_pattern.get_binary_patterns_data_from_doc(None,'./PDF/rice india part1.pdf','pdf',3,None)
#print (binary_rel)

#nary_patterns = Controller_n_ary_pattern.get_nary_patterns(path)
#print (nary_patterns)
#Controller_n_ary_pattern.get_nary_patterns_data_from_doc(None)

# mediator of openai extractor and the ontology
#subClasses = Controller_subClass_pattern.get_subclass_pattern_from_doc(None,None, None, None)
#subClasses = Controller_subClass_pattern.get_subclass_pattern_from_doc(None,None, None, None)
#print (subClasses)
#subclassList = Controller_subClass_pattern.get_subclass_from_onto(path)
""" 
for subclassess in subclassList:
    
    class_data_properties = Controller_subClass_pattern.get_classes_properties (path, subclassess)
# Convert the dictionary to a JSON string
    json_output = json.dumps(class_data_properties, indent=4)
    print (json_output)
"""
"""
#read a given ontology
path="./OntoRepo/CropKB_tbox_original.rdf"
#get_nary_patterns()

#respones = n_ary_pattern_individual_extractor.get_individual_for_nary_relation(n_ary_entity,'./PDF/RICE.pdf','pdf',2,None)
respones = n_ary_pattern_individual_extractor.get_individual_for_nary_relation(n_ary_entity,'./POPs/homegarden_brinjal_v9.xlsx','excel',None,"PoP - large")

""" 
"""
# calling to openai lib for extract individuals - pdf file can be passed
#outputContent = OntoIndividualExtractor.textToOntologyIndividual()
#parsed_data = json.loads(outputContent)
# Accessing information
#JSONtoOntologyPasser.createEntitiesFromJSON (outputContent)
"""

""" 
individuals= '''
{
    "Individuals": [
        {
            "name": "PR 131",
            "class": "rice crop",
            "dataProperties": [
                "plant_height",
                "maturity_days"
            ]
        },
        {
            "name": "PR 129",
            "class": "rice crop",
            "dataProperties": [
                "average_yeild",
                "version"
            ]
        }
    ]
}
'''


#Testing SubClasses pattern based individual extraction
#parameters: subclasses: List/JSON ,docpath: file path ,doc_type: pdf or excel, pages: if pdf, sheet_name: if excel
respones = Extractor_individual_property_value_extractor.get_class_property_value(individuals,'./PDF/rice india.pdf','pdf',2,None)
#respones = subclass_individual_extractor.get_subclass_individual(json_classes,'./POPs/homegarden_brinjal_v9.xlsx','excel',None,"Variety - small")
print (respones)
"""