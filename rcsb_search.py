from rcsbsearchapi.search import TextQuery, AttributeQuery
from rcsbsearchapi import rcsb_attributes as attrs
from rcsbsearchapi.const import STRUCTURE_ATTRIBUTE_SEARCH_SERVICE

q1 = TextQuery("Respiratory Complex I")
q2 = AttributeQuery("exptl.method", "exact_match", "electron microscopy",
                    STRUCTURE_ATTRIBUTE_SEARCH_SERVICE)
q3 = attrs.rcsb_accession_info.deposit_date > "2020-01-01"

query = q1 & q2 & q3

# for assemblyid in query("assembly"):
#     print(assemblyid)

print(query.count())
