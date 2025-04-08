import ontology_importer
import Retriver_nary_pattern_retriver
import Extractor_n_ary_pattern_individual_extractor
 
def get_nary_patterns(ontology_path):
    ontology=ontology_importer.ontology_reader(ontology_path)
    n_ary_entity = Retriver_nary_pattern_retriver.detect_n_ary_relationships(ontology)
    return n_ary_entity

def get_nary_patterns_data_from_doc(n_ary_entity):
    n_ary_entity = '''
    {
    "NaryPropertyAxiom": {
        "ontology structure": [
            "Crop hasGrowingProblemEvent GrowingProblemEvent"
            "GrowingProblemEvent hasGrowingProblem GrowingProblem",
            "GrowingProblemEvent hasSymptom Symptom",
            "GrowingProblemEvent hasCausalAgent CausalAgent",
            "GrowingProblemEvent hasVailablePeriod Season",
            "GrowingProblemEvent hasControlMethod ControlMethod",
            "GrowingProblemEvent hasPreventionMethod PreventionMethod"
        ]
    }
    }
    '''
    respones = Extractor_n_ary_pattern_individual_extractor.get_individual_for_nary_relation(n_ary_entity,'./PDF/rice india part2.pdf','pdf',3,None)
    #respones = Extractor_n_ary_pattern_individual_extractor.get_individual_for_nary_relation(n_ary_entity,'./POPs/homegarden_brinjal_v9.xlsx','excel',None,"PoP - large")
    return respones

#Testing for KES
#get_nary_patterns_data_from_doc('')
