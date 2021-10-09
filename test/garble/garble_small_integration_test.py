import util.garble.garble_util as gu
import util.file.file_util as fu
from types import SimpleNamespace


def test_small():
    print("\n\nStarting test...")
    do_test("hospital_001")
    do_test("hospital_002")
    do_test("hospital_003")
    print("\n\nDone.")


def do_test(name):
    print("-----------------------------------")
    print("Doing test for: " + name)
    source_file = fu.get_file_name("test-data/data-owner/small/"+name+"/"+name+".csv")
    secret_file = fu.get_file_name("test-data/data-owner/small/"+name+"/secret-file.txt")
    output_dir = fu.get_file_name("test-data/data-owner/small/"+name+"/out")
    schema_dir = fu.get_file_name("test-data/data-owner/small/schema")
    output_zip = name+".zip"
    gu.do_garble(source_file, secret_file, output_dir, schema_dir, output_zip)



