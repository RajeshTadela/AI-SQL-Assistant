from database.schema_reader import get_schema


def infer_relationships(config):

    schema = get_schema(config)

    relationships = []

    tables = list(schema.keys())

    for table1 in tables:

        cols1 = [c[0] for c in schema[table1]]

        for table2 in tables:

            if table1 == table2:
                continue

            cols2 = [c[0] for c in schema[table2]]

            for col1 in cols1:

                for col2 in cols2:

                    if col1.lower() == col2.lower():

                        relationships.append(
                            (
                                table1,
                                col1,
                                table2,
                                col2
                            )
                        )

    return relationships


if __name__ == "__main__":

    for relation in infer_relationships():

        print(relation)