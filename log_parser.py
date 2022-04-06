import re

print('Warnings:')
with open('data/rsvp_agent_log.dat', 'r') as log_file:
    for line in log_file:
        match = re.search('WARNING', line)
        if match != None:
            print(re.sub(r'WARNING:\S+:', '--', line))

