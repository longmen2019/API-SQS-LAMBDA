#!/usr/bin/env python3

import aws_cdk as cdk

from python_project15.python_project15_stack import PythonProject15Stack


app = cdk.App()
PythonProject15Stack(app, "PythonProject15Stack")

app.synth()
