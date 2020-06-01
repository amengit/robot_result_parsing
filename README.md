# Get keyword usage statistics from output.xml via `rebot` command

It will write the output to temp tsv file, the temp file directory will be logged from the console output. then it can be imported to excel fro further analizing, it accepts 1 parameter: the file name, by default: keyword_statistics.tsv

it can be run as below if `CollectKws.py` in the module search path.
`python -m robot.rebot --prerebotmodifier CollectKws output.xml`
or you can run from directory where `CollectKws.py` located with providing file name
`python -m robot.rebot --prerebotmodifier CollectKws:CDC_keyword_statistics.tsv output.xml`
