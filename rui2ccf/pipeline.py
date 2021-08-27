import os
import json
from rui2ccf.ontology import SPOntology


def run(args):
    """
    """
    output_path, output_basename = os.path.split(args.output)

    o = SPOntology.new(output_basename)
    for fileName in args.input_file:
        if not (fileName.endswith(".json") or fileName.endswith(".jsonld")):
            raise IOError("Required JSON format")
        records = json.load(open(fileName))
        o = o.mutate(records)

    o.serialize(args.output)
