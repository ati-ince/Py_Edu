1. Conversion:
"2020-02-01" -> convert -> datetime(2020,1,1,) #for understand data with using language
2. Validation:
"2020-01-01" -> data is wrong #but not always easy to detect....
3. Enrichment:
"206.52.21.11" that IP means -> Carpinteria, California, U.S.
4. Missing:
IP="" -> #no data so improvisation needs :)

------------
#After doing all these task that data going to store into single DB (data lake). It is easier to work with. Some example Google's BigQuery, Spark, etc.
