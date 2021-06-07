# -*- encoding: utf-8 -*-
import boto3
kinesis = boto3.client("kinesis")

#データ送信
kinesis.put_records(
    Records = [
        {
            "Data" : b"String",
            "PartitionKey" : "String"
        }
    ],
    StreamName = "Kinesis Data Stream Name"
)
