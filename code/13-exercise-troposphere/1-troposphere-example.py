# https://github.com/cloudtools/troposphere

from troposphere import Base64, FindInMap, GetAtt
from troposphere import Parameter, Output, Ref, Template
import troposphere.ec2 as ec2

template = Template()

keyname_param = template.add_parameter(Parameter(
    "KeyName",
    Type="String",
    Description="Name of an existing EC2 KeyPair to enable SSH",
    Default="pduleba-eu-west-1-key-pair",
))

template.add_mapping('RegionMap', {
    "eu-west-1": {"AMI": "ami-01720b5f421cf0179"},
    "eu-west-2": {"AMI": "ami-0e80a462ede03e653"},
    "eu-west-3": {"AMI": "ami-000bdaf1845abe910"},
    "eu-north-1": {"AMI": "ami-01d2b64cb4bdfe5db"},
    "eu-south-1": {"AMI": "ami-04a490111f1f73f3a"},
    "eu-central-1": {"AMI": "ami-03c3a7e4263fd998c"}
})

ec2_instance = template.add_resource(ec2.Instance(
    "Ec2Instance",
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t1.micro",
    KeyName=Ref(keyname_param),
    SecurityGroups=["default"],
    UserData=Base64("80")
))

template.add_output([
    Output(
        "InstanceId",
        Description="InstanceId of the newly created EC2 instance",
        Value=Ref(ec2_instance),
    ),
    Output(
        "AZ",
        Description="Availability Zone of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "AvailabilityZone"),
    ),
    Output(
        "PublicIP",
        Description="Public IP address of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PublicIp"),
    ),
    Output(
        "PrivateIP",
        Description="Private IP address of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PrivateIp"),
    ),
    Output(
        "PublicDNS",
        Description="Public DNSName of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PublicDnsName"),
    ),
    Output(
        "PrivateDNS",
        Description="Private DNSName of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PrivateDnsName"),
    ),
])

print("--------------------------\n----- JSON TEMPLATE ------\n--------------------------")
print(template.to_json())
print("--------------------------\n----- YAML TEMPLATE ------\n--------------------------")
print(template.to_yaml())
