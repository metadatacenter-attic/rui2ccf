import json
from rui2ccf.ontology import SOntology


def run(args):
    """
    """
    records = json.load(open(args.input_file))
    o = SOntology.new()
    o = o.mutate(records)
    o.serialize(args.output)
