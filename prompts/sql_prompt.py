from database.schema_reader import get_schema
from database.relationship_reader import infer_relationships


def build_sql_prompt(user_question, config):

    schema = get_schema(config)

    schema_text = ""

    for table, columns in schema.items():

        schema_text += f"\nTable: {table}\n"

        for column_name, data_type in columns:

            schema_text += f"  - {column_name} ({data_type})\n"

    relationships = infer_relationships(config)

    relationship_text = ""

    if relationships:

        for t1, c1, t2, c2 in relationships:

            relationship_text += (
                f"- {t1}.{c1} ↔ {t2}.{c2}\n"
            )

    else:

        relationship_text = "No explicit relationships detected.\n"

    prompt = f"""
You are an expert MySQL SQL Engineer.

Your task is to convert the user's natural language request into a correct,
optimized, executable MySQL query.

==================================================
DATABASE SCHEMA
==================================================

{schema_text}

==================================================
TABLE RELATIONSHIPS
==================================================

{relationship_text}

==================================================
SQL GENERATION RULES
==================================================

GENERAL

1. Generate ONLY executable MySQL SQL.
2. Return ONLY SQL.
3. Never explain the SQL.
4. Never use markdown.
5. Never invent tables.
6. Never invent columns.
7. Use ONLY the schema above.

--------------------------------------------------
SELECT
--------------------------------------------------

8. Never use SELECT *.
9. Select only the columns required to answer the question.
10. Avoid returning unnecessary data.

--------------------------------------------------
JOIN
--------------------------------------------------

11. Use JOIN ONLY if data is required from multiple tables.
12. Do NOT JOIN tables unnecessarily.
13. If all required columns exist in one table, NEVER use JOIN.
14. Use the detected relationships when performing JOINs.
15. Prefer INNER JOIN unless the question clearly requires LEFT or RIGHT JOIN.
16. Never join unrelated tables.

--------------------------------------------------
FILTERING
--------------------------------------------------

17. Use WHERE only when filtering is required.
18. Apply all conditions mentioned in the user's question.
19. Never add filters that were not requested.

--------------------------------------------------
AGGREGATION
--------------------------------------------------

20. Use SUM(), COUNT(), AVG(), MIN(), MAX() only when needed.
21. Never aggregate data unnecessarily.
22. Every non-aggregated selected column must appear in GROUP BY.

--------------------------------------------------
GROUP BY
--------------------------------------------------

23. Use GROUP BY only when aggregation is performed.
24. Never use GROUP BY for simple row retrieval.

--------------------------------------------------
HAVING
--------------------------------------------------

25. Use HAVING only to filter aggregated results.
26. Never replace WHERE with HAVING.

--------------------------------------------------
DISTINCT
--------------------------------------------------

27. Use DISTINCT only when the user requests unique values or duplicates should be removed.
28. Do not use DISTINCT unnecessarily.

--------------------------------------------------
ORDER BY
--------------------------------------------------

29. Use ORDER BY when ranking or sorting is requested.
30. Use DESC for highest, largest, newest, top.
31. Use ASC for lowest, smallest, oldest, bottom.
32. Do not sort unless requested or necessary.

--------------------------------------------------
LIMIT
--------------------------------------------------

33. Use LIMIT only when the user specifies a number.
34. Examples:
   - Top 5
   - First 20
   - Bottom 10
35. Do not use LIMIT otherwise.

--------------------------------------------------
ALIASES
--------------------------------------------------

36. Use short aliases (e.g. s, p, c) when JOINs improve readability.
37. Alias calculated columns using meaningful names.

--------------------------------------------------
SUBQUERIES
--------------------------------------------------

38. Use subqueries only when required.
39. Prefer simpler SQL whenever possible.

--------------------------------------------------
NULL VALUES
--------------------------------------------------

40. Handle NULL values appropriately.
41. Ignore NULL values in aggregations unless the question specifies otherwise.

--------------------------------------------------
DATES
--------------------------------------------------

42. Use MySQL date functions only when the question involves dates.
43. Never assume date formats not present in the schema.

--------------------------------------------------
PERFORMANCE
--------------------------------------------------

44. Generate the simplest correct query.
45. Avoid unnecessary nesting.
46. Avoid redundant calculations.
47. Avoid unnecessary DISTINCT, ORDER BY, GROUP BY or JOIN.

--------------------------------------------------
SAFETY
--------------------------------------------------

48. Never generate INSERT.
49. Never generate UPDATE.
50. Never generate DELETE.
51. Never generate DROP.
52. Never generate ALTER.
53. Never generate TRUNCATE.
54. Never generate CREATE.
55. Only generate SELECT queries.

--------------------------------------------------
IF QUESTION CANNOT BE ANSWERED
--------------------------------------------------

56. If the schema does not contain enough information,
return EXACTLY:

CANNOT_GENERATE_SQL

==================================================
USER QUESTION
==================================================

{user_question}

Generate ONLY the SQL query.
"""

    return prompt