# ETL of Spotify charts in AWS


# Architecture Overview:
This documentation describes the data transformation and processing pipeline for the Spotify streams dataset. The dataset contains information about the streaming activity of various tracks on Spotify across different regions and charts. The goal of this pipeline is to extract, transform, and load the data into a structured schema that supports efficient querying and analysis for various business needs.
The cloud choosen for this business case was AWS (Amazon Web Services) for its scalability, managed services, and global reach. The architecture includes data ingestion, transformation, and storage.

### Proposed Architecture:
AWS Services such as CLI, IAM, S3, Lambda, Glue, and RedShift were selected for this business case. In summary, the ideia of the pipeline is to ensure scalability and 100% automation. To make this feasible, the architecture logic was building following the logical sequence steps:
1. Connect local folder with the cloud through AWS CLI
2. Pipeline is triggered once the file arrives in cloud
2. Source Data: The raw data is stored in CSV files in an Amazon S3 bucket.
3. AWS Glue: AWS Glue is used to perform ETL (Extract, Transform, Load) 
4. Amazon Redshift: Amazon Redshift is the target data warehouse where the transformed data is loaded. 
5. A star schema is designed to optimize storage and maintain consistency.
* Note: The pipeline was built to handle larges ammounts of data with services such as S3, Glue and Redshift enabling scalability

The following diagram shows the high-level architecture of the pipeline:
![image](https://github.com/paulohader/spotify-etl/assets/122403781/626a18c5-bb12-4b6b-9a8a-2538dd3e7cc2)


## How does the pipepiline works?
### Data Ingestion:
- Amazon S3 was selected as a Data Lake as the landing zone for raw data dumps (allowing storage of large volumes of data in a scalable and cost-effective way)
- Scheduled regular data dumps from Sfotipy local folder to the S3 bucket.
- Automated ingestion using AWS Lambda.

### Overview of the Data Transformation and Processing:
* There are interactions between three services (S3, Glue, Redshift), so an IAM role was created granting the full permisions for each service
AWS Glue Studio was selected for ETL (Extract, Transform, Load) processing:
1. Glue jobs were created to extract the raw data in S3 and transform CSV data into structured schema for the proposed case
2. Glue ETL job was set with visual (Extract from S3, transform and load into Redshift) to handle schema evolution and data validation (image)
3. The Glue job connects directly to the target Amazon Redshift Data Warehouse, finally loading the respective tables
4. The schedule option in AWS Glue Studio allows you to schedule your pipeline as per need
5. The star schema was built to optimise storage and maintain consistency
* Note: In each step described, was possible to set the parameters needed (i.e, s3 path, transformation type, db connections)
* Note 2: AWS Glue transforms data with Spark, Pyspark support and its DynamicFrame, handling the large ammount of data
![aws-etl-flow](https://github.com/paulohader/spotify-etl/assets/122403781/6c62e676-6ae9-4f1e-a096-dfe9a2599539)


### Step by step to crete and perform each service

#### Create an Amazon Redshift Cluster:
An Amazon Redshift cluster was created by accessing the Amazon Redshift console.
##### Cluster Configuration: 
The cluster settings, including node type, number of nodes, database name, and other parameters, were configured during cluster creation. The cluster was then provisioned.

#### Create a Redshift Database and Table:
Connection to Amazon Redshift: A connection to the Amazon Redshift cluster was established using a SQL client tool.
Database and Table Creation: A database was created within the Redshift cluster, and a table was set up to receive the transformed data.
Schema Definition: The schema, including defining columns and their data types, was established based on the structure of the transformed data.
![image](https://github.com/paulohader/spotify-etl/assets/122403781/d32ebc54-fd13-414e-94d7-70f77615de62)

#### Data Ingestion:
#### Data Lake Selection: 
Amazon S3 was chosen as the Data Lake, providing a scalable and cost-effective storage solution for large volumes of raw data dumps.

#### Automated Data Ingestion:
Regular data dumps from the local Spotify folder to the designated S3 bucket were scheduled and automated using the AWS CLI.
AWS Lambda handled the automated data ingestion, ensuring data was continuously moved to the Data Lake.

#### Data Transformation and Processing:
The data transformation and processing involved interactions between Amazon S3, AWS Glue, and Amazon Redshift. An IAM role with full permissions for each service was established to facilitate this process.
####  ETL Processing with AWS Glue Studio:
AWS Glue Studio was chosen for Extract, Transform, Load (ETL) processing due to its flexibility and scalability.
Data Extraction and Transformation:
Glue jobs were created to extract raw data stored in Amazon S3 and transform CSV data into a structured schema tailored for the specific use case.

#### Visual ETL Job Creation:
A Glue ETL job was configured visually to handle the complete ETL process, including data extraction from S3, transformation, and loading into Amazon Redshift. This approach managed schema evolution and data validation.
Direct Connection to Amazon Redshift:
The Glue job established a direct connection to the target Amazon Redshift Data Warehouse, ensuring data was efficiently loaded into the respective tables.
![aws-etl-job](https://github.com/paulohader/spotify-etl/assets/122403781/14d0a64a-3932-4bd8-afed-b9789cefc626)

#### Pipeline Scheduling:
AWS Glue Studio's scheduling feature was configured to automate the pipeline according to specific needs (weekly, every 2 days). This was set to run the pipeline at regular intervals, such as daily or hourly, aligning with business requirements.

#### Star Schema Optimization:
A star schema was implemented to optimize storage and maintain data consistency, enhancing data warehousing efficiency.
Parameterization:
Throughout each step, parameters such as S3 paths, transformation types, and database connections were configured to align with the unique pipeline requirements.


#### AWS Glue's Data Transformation:
AWS Glue employed Spark, Pyspark support, and its DynamicFrame to efficiently handle the large amount of data, optmising performance of the data transformation process.
#### CloudWatch Monitoring:
The pipeline setup has included CloudWatch monitoring, which allows for real-time monitoring and alerts on various metrics and events related to the pipeline's operation. CloudWatch Alarms can be configured to notify users of any issues or anomalies during pipeline execution.

## Final Comments

### Scalability Considerations:
Amazon S3 enables virtually unlimited storage capacity to handle large datasets.
Redshift scales horizontally by adding nodes to the cluster as needed
Now it is possible to connect AWS Glue with Bitbucket, Gitlab and Github repositories to keep track of version control and made changes to the code

### Benefits of This Approach:
Scalability: The architecture can handle growing data volumes without manual intervention.
Automation: Scheduled jobs ensure 100% automation of data ingestion and transformation.
It is possible to pay only for the resources used during processing.




