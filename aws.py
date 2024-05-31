
After createting the S3 bucket, we need add below bucket policy for coe deployment in S3 bucket
{
    "Version": "2012-10-17",
    "Id": "Policy1717138099633",
    "Statement": [
        {
            "Sid": "Stmt1717138087935",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::my-bucket-2024-05-31-new/*"
        }
    ]
}
Below Access are required for the Glue CICD pipeline creation

codepipeline IAM role

AWScodepipeline_fullaccess
AWSCodebuildadminaccess
cloudformationfullaccess
IAMfullaccess
s3fullaccess

Note:- Once we create the role, we need to change the trusted policy from "ec2" to "codepipeline"

Cloudformation IAM role

IAMfullaccess
S3fullaccess
AWSGlueServicerole
AWScloudformationfullaccess


