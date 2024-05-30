  MyJob:
    Type: AWS::Glue::Job
    Properties:
      Command:
        Name: glueetl
        ScriptLocation: "s3://<your-S3-script-uri>"
      DefaultArguments:                               --> Under this parameters we can pass requred things like (Python library path, Dependent JARs path and ref files path)
        "--job-bookmark-option": "job-bookmark-enable"
      ExecutionProperty:
        MaxConcurrentRuns: 2
      MaxRetries: 0
      Name: cf-job1
      Role: !Ref MyJobRole

******************************************************************************************************
Sample Glue job cloudformation templete for (DefaultArguments)
*******************************************************************************************************
MyJob:
    Type: AWS::Glue::Job
    Properties:
      Name: cf-job1
      Command:
        Name: test-etl1
        ScriptLocation: "s3://project_bucket/releases/latest/mixpanel_job.py"
        PythonVersion: "3"
      Description: "Testing setup config"
      ExecutionProperty:
        MaxConcurrentRuns: 2
      MaxRetries: 2
      GlueVersion: "3.0"
      WorkerType: "G.1X"
      NumberOfWorkers: 2
      Timeout: 2880
      DefaultArguments:
        "--class": "GlueApp"
        "--enable-continuous-cloudwatch-log": "true"
        "--enable-job-insights": "true"
        "--enable-metrics": "true"
        "--enable-spark-ui": "true"
        "--extra-jars": "s3://project_bucket/releases/latest/jars/delta-core_2.12-1.0.1.jar"
        "--extra-py-files": "s3://project_bucket/releases/latest/lib.zip"
        "--job-bookmark-option": "job-bookmark-disable"
        "--job-language": "python"
        "--spark-event-logs-path": "s3://project_bucket/logs/"
      Role: !Ref MyJobRole
                                       
