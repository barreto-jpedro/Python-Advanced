from json import dump

from troposphere import ec2
from troposphere import Template

template = Template()
instancia = ec2.Instance(
    "firstTestServer", ImageId="ami-00399ec92321828f5", InstanceType="t2.micro"
)

template.add_resource(resource=instancia)

with open("Module 8.yml", "w") as file:
    dump(template.to_yaml(), file)
