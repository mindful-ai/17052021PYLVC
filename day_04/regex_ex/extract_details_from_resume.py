import re
EOF = ''
# Read the file as a text

f = open( "resume.txt", "r" )
content = f.read()
f.close()
# Patterns

jobid = r"#\d{6}"
email = r"(\w+[._])*\w+@{1}\w*\.(com|org|in)"
phone = r"ccc"
linkedin = r"linkedin.com/(\w+/){1,3}(\w+[-._]?)+"
name = r"ccc"

# Apply the patterns and store what ever is extracted



m = re.search(jobid, content)
if m:
    print('JOBID     : ', m.group())

m = re.search(email, content)
if m:
    print('EMAIL     : ', m.group())

m = re.search(phone, content)
if m:
    print('PHONE     : ', m.group())

m = re.search(linkedin, content)
if m:
    print('LINKEDIN  : ', m.group())

m = re.search(name, content)
if m:
    print('NAME      : ', m.groupdict()['Name'])