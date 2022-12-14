# SPDX-License-Identifier: CC0-1.0

import os

import xmlschema

def getAllXMLFiles(srcDir):
    # recursively gets all files in srcDir with .xml extension.
    paths = []
    for root, ds, fs in os.walk("src"):
        for f in fs:
            if f.endswith(".xml"):
                paths.append(os.path.join(root, f))
    return paths

def validateXMLFile(xmlFilename, spdxSchema):
    spdxSchema.validate(xmlFilename)

if __name__ == "__main__":
    spdxSchema = xmlschema.XMLSchema("ListedLicense.xsd")
    paths = getAllXMLFiles("src")
    for xf in paths:
        validateXMLFile(xf, spdxSchema)
