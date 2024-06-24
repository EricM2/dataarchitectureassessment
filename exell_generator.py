import pandas as pd

# Define the data for the Excel sheet separated by data architecture aspects
data = [
    ("Data Modeling and Design", "", "", ""),
    ("", "How well-defined are your data models (conceptual, logical, physical)?", 
     "1: No defined data models.\n2: Basic models with many gaps.\n3: Moderately defined models with some gaps.\n4: Well-defined models with minor gaps.\n5: Comprehensive and fully defined models.",
     "1: Initiate a data modeling project to create basic models.\n2: Conduct workshops to identify and fill gaps in existing models.\n3: Review and refine models to address remaining gaps.\n4: Regularly update models to ensure they remain comprehensive."),
    
    ("", "Are data models standardized across the organization?", 
     "1: No standardization.\n2: Minimal standardization efforts.\n3: Some standardization in certain areas.\n4: Mostly standardized with few exceptions.\n5: Fully standardized across the organization.",
     "1: Develop and implement data modeling standards.\n2: Promote standardization through training and guidelines.\n3: Standardize data models in key areas.\n4: Ensure all data models follow standard guidelines."),
    
    ("", "How do you handle data redundancy and normalization?", 
     "1: No strategies for handling redundancy or normalization.\n2: Basic strategies with significant redundancy.\n3: Moderate strategies with occasional redundancy.\n4: Good strategies with minimal redundancy.\n5: Excellent strategies with no redundancy.",
     "1: Develop strategies for data normalization.\n2: Implement basic normalization techniques.\n3: Regularly review data for redundancy.\n4: Optimize data models to minimize redundancy."),
    
    ("", "Are relationships between different data entities clearly defined?", 
     "1: Relationships are not defined.\n2: Few relationships are defined.\n3: Some relationships are defined.\n4: Most relationships are defined.\n5: All relationships are clearly defined.",
     "1: Identify and document key relationships.\n2: Define relationships in data models.\n3: Review and refine relationships.\n4: Ensure all relationships are well-documented and clear."),
    
    ("Data Storage and Operations", "", "", ""),
    ("", "What types of databases are in use (relational, NoSQL, data lakes)?", 
     "1: Single type of database with no flexibility.\n2: Limited use of multiple database types.\n3: Moderate use of multiple database types.\n4: Extensive use of multiple database types.\n5: Comprehensive use of the appropriate database types for various use cases.",
     "1: Assess the need for different database types.\n2: Implement limited use of additional database types.\n3: Expand the use of multiple database types.\n4: Optimize the use of different database types."),
    
    ("", "How is data storage optimized for performance and cost?", 
     "1: No optimization strategies.\n2: Minimal optimization strategies.\n3: Some optimization strategies.\n4: Well-defined optimization strategies.\n5: Comprehensive and fully implemented optimization strategies.",
     "1: Conduct a cost-performance analysis.\n2: Implement basic optimization strategies.\n3: Regularly review and improve optimization strategies.\n4: Fully optimize data storage."),
    
    ("", "What are your data archiving and retention policies?", 
     "1: No archiving or retention policies.\n2: Basic policies with many gaps.\n3: Moderate policies with some gaps.\n4: Well-defined policies with minor gaps.\n5: Comprehensive and fully implemented policies.",
     "1: Develop archiving and retention policies.\n2: Implement basic policies.\n3: Regularly review and improve policies.\n4: Fully implement archiving and retention policies."),
    
    ("", "How is data partitioned and indexed?", 
     "1: No partitioning or indexing.\n2: Basic partitioning and indexing with significant gaps.\n3: Moderate partitioning and indexing.\n4: Well-defined partitioning and indexing.\n5: Comprehensive and fully optimized partitioning and indexing.",
     "1: Develop partitioning and indexing strategies.\n2: Implement basic partitioning and indexing.\n3: Regularly review and optimize partitioning and indexing.\n4: Fully optimize partitioning and indexing."),
    
    ("", "Are storage solutions scalable to meet future data growth?", 
     "1: Not scalable.\n2: Limited scalability.\n3: Moderately scalable.\n4: Highly scalable with some limitations.\n5: Fully scalable to meet future data growth.",
     "1: Assess scalability requirements.\n2: Implement basic scalability solutions.\n3: Regularly review and improve scalability.\n4: Fully optimize scalability solutions."),
    
    ("Data Integration and Interoperability", "", "", ""),
    ("", "What ETL tools and processes are in place for data integration?", 
     "1: No ETL tools or processes.\n2: Basic ETL tools with significant gaps.\n3: Moderate ETL tools and processes.\n4: Well-defined ETL tools and processes.\n5: Comprehensive and fully implemented ETL tools and processes.",
     "1: Identify and implement ETL tools.\n2: Develop basic ETL processes.\n3: Regularly review and improve ETL processes.\n4: Fully implement ETL tools and processes."),
    
    ("", "How do you handle data from disparate sources?", 
     "1: No strategy for handling disparate data sources.\n2: Basic strategies with significant gaps.\n3: Moderate strategies with some gaps.\n4: Well-defined strategies with minor gaps.\n5: Comprehensive and fully implemented strategies.",
     "1: Develop strategies for handling disparate data sources.\n2: Implement basic strategies.\n3: Regularly review and improve strategies.\n4: Fully implement strategies."),
    
    ("", "Are there automated workflows for data extraction, transformation, and loading?", 
     "1: No automated workflows.\n2: Minimal automated workflows.\n3: Some automated workflows.\n4: Extensive automated workflows with minor gaps.\n5: Fully automated workflows.",
     "1: Develop automated workflows.\n2: Implement basic automation.\n3: Regularly review and improve workflows.\n4: Fully automate ETL processes."),
    
    ("", "How do you handle real-time data integration?", 
     "1: No real-time data integration.\n2: Basic real-time integration with significant gaps.\n3: Moderate real-time integration.\n4: Well-defined real-time integration.\n5: Comprehensive and fully implemented real-time integration.",
     "1: Develop real-time integration strategies.\n2: Implement basic real-time integration.\n3: Regularly review and improve real-time integration.\n4: Fully implement real-time integration strategies."),
    
    ("Data Governance and Security", "", "", ""),
    ("", "What data governance framework is in place?", 
     "1: No governance framework.\n2: Basic governance framework with significant gaps.\n3: Moderate governance framework.\n4: Well-defined governance framework.\n5: Comprehensive and fully implemented governance framework.",
     "1: Develop a data governance framework.\n2: Implement basic governance.\n3: Regularly review and improve governance framework.\n4: Fully implement governance framework."),
    
    ("", "Are there clearly defined roles and responsibilities for data stewardship?", 
     "1: No defined roles or responsibilities.\n2: Minimal defined roles and responsibilities.\n3: Some defined roles and responsibilities.\n4: Well-defined roles and responsibilities with minor gaps.\n5: Comprehensive and fully implemented roles and responsibilities.",
     "1: Define roles and responsibilities.\n2: Implement basic roles and responsibilities.\n3: Regularly review and improve roles and responsibilities.\n4: Fully implement roles and responsibilities."),
    
    ("", "How do you ensure data compliance with relevant regulations (e.g., GDPR, CCPA)?", 
     "1: No compliance measures.\n2: Basic compliance measures with significant gaps.\n3: Moderate compliance measures.\n4: Well-defined compliance measures with minor gaps.\n5: Comprehensive and fully implemented compliance measures.",
     "1: Develop compliance measures.\n2: Implement basic compliance.\n3: Regularly review and improve compliance.\n4: Fully implement compliance measures."),
    
    ("", "What policies are in place for data access and usage?", 
     "1: No policies.\n2: Basic policies with significant gaps.\n3: Moderate policies.\n4: Well-defined policies with minor gaps.\n5: Comprehensive and fully implemented policies.",
     "1: Develop data access and usage policies.\n2: Implement basic policies.\n3: Regularly review and improve policies.\n4: Fully implement policies."),
    
    ("Data Quality and Performance", "", "", ""),
    ("", "How is data quality maintained during integration?", 
     "1: No data quality measures.\n2: Basic data quality measures with significant gaps.\n3: Moderate data quality measures.\n4: Well-defined data quality measures with minor gaps.\n5: Comprehensive and fully implemented data quality measures.",
     "1: Develop data quality measures.\n2: Implement basic measures.\n3: Regularly review and improve measures.\n4: Fully implement data quality measures."),
    
    ("", "How do you handle data lineage?", 
     "1: No data lineage tracking.\n2: Minimal data lineage tracking.\n3: Some data lineage tracking.\n4: Well-defined data lineage tracking.\n5: Comprehensive and fully implemented data lineage tracking.",
     "1: Develop data lineage tracking strategies.\n2: Implement basic tracking.\n3: Regularly review and improve tracking.\n4: Fully implement data lineage tracking."),
    
    ("", "What data profiling and cleansing methods are used?", 
     "1: No profiling or cleansing methods.\n2: Basic methods with significant gaps.\n3: Moderate methods.\n4: Well-defined methods with minor gaps.\n5: Comprehensive and fully implemented methods.",
     "1: Develop profiling and cleansing methods.\n2: Implement basic methods.\n3: Regularly review and improve methods.\n4: Fully implement profiling and cleansing methods."),
    
    ("", "How do you measure and improve data quality over time?", 
     "1: No measurement or improvement strategies.\n2: Basic strategies with significant gaps.\n3: Moderate strategies.\n4: Well-defined strategies with minor gaps.\n5: Comprehensive and fully implemented strategies.",
     "1: Develop measurement and improvement strategies.\n2: Implement basic strategies.\n3: Regularly review and improve strategies.\n4: Fully implement measurement and improvement strategies."),
    
    ("Data Analytics and Reporting", "", "", ""),
    ("", "What types of analytics tools are in use (descriptive, predictive, prescriptive)?", 
     "1: No analytics tools.\n2: Basic analytics tools with significant gaps.\n3: Moderate analytics tools.\n4: Well-defined analytics tools with minor gaps.\n5: Comprehensive and fully implemented analytics tools.",
     "1: Identify and implement analytics tools.\n2: Develop basic analytics strategies.\n3: Regularly review and improve analytics tools.\n4: Fully implement analytics tools."),
    
    ("", "How is data visualized and reported?", 
     "1: No data visualization or reporting.\n2: Basic visualization and reporting with significant gaps.\n3: Moderate visualization and reporting.\n4: Well-defined visualization and reporting.\n5: Comprehensive and fully implemented visualization and reporting.",
     "1: Develop visualization and reporting strategies.\n2: Implement basic visualization and reporting.\n3: Regularly review and improve visualization and reporting.\n4: Fully implement visualization and reporting strategies."),
    
    ("", "What self-service BI tools are available to users?", 
     "1: No self-service BI tools.\n2: Basic tools with significant gaps.\n3: Moderate tools.\n4: Well-defined tools with minor gaps.\n5: Comprehensive and fully implemented tools.",
     "1: Identify and implement self-service BI tools.\n2: Develop basic self-service BI strategies.\n3: Regularly review and improve BI tools.\n4: Fully implement self-service BI tools."),
    
    ("", "How do you ensure data is accurate and timely for analytics?", 
     "1: No strategies for accuracy and timeliness.\n2: Basic strategies with significant gaps.\n3: Moderate strategies.\n4: Well-defined strategies with minor gaps.\n5: Comprehensive and fully implemented strategies.",
     "1: Develop strategies for accuracy and timeliness.\n2: Implement basic strategies.\n3: Regularly review and improve strategies.\n4: Fully implement strategies for accuracy and timeliness.")
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["Aspect", "Question", "Maturity Levels", "Improvement Steps"])

# Save the DataFrame to an Excel file
df.to_excel("Data_Architecture_Questionnaire.xlsx", index=False)
