
After createting the S3 bucket, we need add below bucket policy for coe deployment in S3 bucket

                                                               {
  "Id": "Policy1716964562825",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1716964561156",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::mybucket-20240529-new/*",
      "Principal": "*"
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


