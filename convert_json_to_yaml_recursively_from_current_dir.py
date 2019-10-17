import json
import yaml
import os
import glob

base_dir = '.'
for file in glob.iglob("**/*", recursive=True):
	fp = os.path.normpath(file)
	if not os.path.basename(fp).endswith('.json'):
		continue
	try :
		s = yaml.dump(yaml.load(json.dumps(json.loads(open(fp).read())), Loader=yaml.FullLoader), default_flow_style=False)
		with open(os.path.join(os.path.dirname(fp), os.path.basename(fp)[:-5] + '.yaml'), 'w') as f:
			f.write(s)
		print('removing', fp)
		os.remove(fp)
	except Exception as e:
		print("skipping file " + file + " due to Exception : " + str(e))


