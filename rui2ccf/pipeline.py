import os
import requests
from requests_file import FileAdapter
from rui2ccf.ontology import SPOntology


def run(args):
    """
    """
    session = requests.Session()
    session.mount('file://', FileAdapter())

    output_path, output_basename = os.path.split(args.output)

    o = SPOntology.new(output_basename)
    for url in args.input_url:
        response = session.get(url)
        records = response.json()
        o = o.mutate(records)

    o.serialize(args.output)
