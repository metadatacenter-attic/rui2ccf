import json
from rui2ccf.ontology import SPOntology


def run(args):
    """
    """
    o = SPOntology.new()
    for f in args.input_file:
        records = json.load(open(f))
        o = o.mutate(records)

    o.serialize(args.output)
