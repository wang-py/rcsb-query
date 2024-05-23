from rcsbsearchapi.search import TextQuery, AttributeQuery
from rcsbsearchapi import rcsb_attributes as attrs
from rcsbsearchapi.const import STRUCTURE_ATTRIBUTE_SEARCH_SERVICE

q1 = TextQuery("Respiratory Complex I")
q2 = AttributeQuery("rcsb_polymer_entity.rcsb_macromolecular_names_combined.name",
                    "contains_phrase", "Complex I",
                    STRUCTURE_ATTRIBUTE_SEARCH_SERVICE)
q3 = AttributeQuery("rcsb_entry_info.deposited_solvent_atom_count",
                    "greater", 0,
                    STRUCTURE_ATTRIBUTE_SEARCH_SERVICE)
q4 = attrs.rcsb_accession_info.deposit_date > "2010-01-01"
query = q1 & q2 & q3 & q4

hits = [x for x in list(query(results_verbosity="minimal"))
        if x['score'] > 0.8]

print("total number of results: ", query.count())
print(f"scores above 0.8: {len(hits)}")
print("last 10 hits: ", hits[-10:])
