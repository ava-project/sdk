import valideer

schema = {
    "+id": "number",
    "+name": "string"
}

test = {
    "name": "toto"
}


validator = valideer.parse(schema)

validator.validate(test)
