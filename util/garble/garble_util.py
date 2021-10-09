import garble
from types import SimpleNamespace
from pathlib import Path


def do_garble(source_file, secret_file, output_dir, schema_dir, output_zip):
    print("source_file: " + source_file)
    print("secret_file: " + secret_file)
    print("output_dir: " + output_dir)
    print("schema_dir: " + schema_dir)
    print("output_zip: " + output_zip)
    args = {
        "sourcefile": source_file,
        "secretfile": secret_file,
        "schemadir": schema_dir,
        "outputdir":  output_dir,
        "outputzip": output_zip
    }
    args = SimpleNamespace(**args)
    clks = garble.garble_pii(args)
    garble.create_clk_zip(clks, args)


# def do_garble_household(source_file, secret_file, output_dir, schemafile, output_zip, mappingfile):
#     args = {
#         "sourcefile": source_file,
#         "secretfile": secret_file,
#         "schemafile": schemafile,
#         "outputdir":  output_dir,
#         "outputzip": output_zip,
#         "mappingfile": mappingfile,
#         "testrun": "t"
#     }
#     print("")
#     print("-------------------")
#     print("ARGS:")
#     print(str(args))
#     print("-------------------")
#     print("")
#     args = SimpleNamespace(**args)
#     clks = gh.garble_households(args)
#     gh.create_clk_zip(clks, args)


