import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://sptbucket/input-spt/charts.csv"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Change Schema Artists
ChangeSchemaArtists_node1696864838568 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[("artist", "string", "artist", "string")],
    transformation_ctx="ChangeSchemaArtists_node1696864838568",
)

# Script generated for node Change Schema Charts
ChangeSchemaCharts_node1696866084336 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[("chart", "string", "chart", "string")],
    transformation_ctx="ChangeSchemaCharts_node1696866084336",
)

# Script generated for node Change Schema - Regions
ChangeSchemaRegions_node1696871389465 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[("region", "string", "region", "string")],
    transformation_ctx="ChangeSchemaRegions_node1696871389465",
)

# Script generated for node Change Schema - Main
ChangeSchemaMain_node1696871597915 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("title", "string", "title", "string"),
        ("rank", "string", "rank", "int"),
        ("date", "string", "date", "date"),
        ("artist", "string", "artist", "string"),
        ("url", "string", "url", "string"),
        ("region", "string", "region", "string"),
        ("chart", "string", "chart", "string"),
        ("trend", "string", "trend", "string"),
        ("streams", "string", "streams", "int"),
    ],
    transformation_ctx="ChangeSchemaMain_node1696871597915",
)

# Script generated for node Drop Duplicates Artists
DropDuplicatesArtists_node1696866852953 = DynamicFrame.fromDF(
    ChangeSchemaArtists_node1696864838568.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicatesArtists_node1696866852953",
)

# Script generated for node Drop Duplicates Charts
DropDuplicatesCharts_node1696866795346 = DynamicFrame.fromDF(
    ChangeSchemaCharts_node1696866084336.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicatesCharts_node1696866795346",
)

# Script generated for node Drop Duplicates - Regions
DropDuplicatesRegions_node1696871522482 = DynamicFrame.fromDF(
    ChangeSchemaRegions_node1696871389465.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicatesRegions_node1696871522482",
)

# Script generated for node Amazon Redshift - Main
AmazonRedshiftMain_node1696871571914 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchemaMain_node1696871597915,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-939567218419-eu-north-1/temporary/",
        "useConnectionProperties": "true",
        "dbtable": "public.main",
        "connectionName": "RedshiftServerless",
        "preactions": "CREATE TABLE IF NOT EXISTS public.main (title VARCHAR, rank INTEGER, date DATE, artist VARCHAR, url VARCHAR, region VARCHAR, chart VARCHAR, trend VARCHAR, streams INTEGER);",
    },
    transformation_ctx="AmazonRedshiftMain_node1696871571914",
)

# Script generated for node Redshift - Artistis Table
RedshiftArtistisTable_node1696866149297 = glueContext.write_dynamic_frame.from_options(
    frame=DropDuplicatesArtists_node1696866852953,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-939567218419-eu-north-1/temporary/",
        "useConnectionProperties": "true",
        "dbtable": "public.artists",
        "connectionName": "RedshiftServerless",
        "preactions": "CREATE TABLE IF NOT EXISTS public.artists (artist VARCHAR);",
    },
    transformation_ctx="RedshiftArtistisTable_node1696866149297",
)


