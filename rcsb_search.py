from rcsbsearchapi.search import TextQuery, AttributeQuery
from rcsbsearchapi import rcsb_attributes as attrs
from rcsbsearchapi.const import STRUCTURE_ATTRIBUTE_SEARCH_SERVICE

q1 = TextQuery("Respiratory Complex I")
q2 = AttributeQuery("rcsb_polymer_instance_annotation.annotation_lineage.name",
                    "contains_words", "NADH oxidoreductase",
                    STRUCTURE_ATTRIBUTE_SEARCH_SERVICE)
q3 = attrs.rcsb_accession_info.deposit_date > "2010-01-01"

query = q1 & q2 & q3

hits = [x for x in list(query(results_verbosity="minimal"))
        if x['score'] > 0.8]

print("total number of results: ", query.count())
print(f"scores above 0.8: {len(hits)}")
print("last 10 hits: ", hits[-10:])
