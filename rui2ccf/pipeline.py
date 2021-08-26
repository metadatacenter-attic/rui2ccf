import os
import json
from rui2ccf.ontology import SPOntology


def run(args):
    """
    """
    if not args.input_file.endswith(".json"):
        raise IOError("Required JSON format")

    path, basename = os.path.split(args.output)

    o = SPOntology.new(basename)
    for f in args.input_file:
        records = json.load(open(f))
        o = o.mutate(records)

    o.serialize(args.output)
