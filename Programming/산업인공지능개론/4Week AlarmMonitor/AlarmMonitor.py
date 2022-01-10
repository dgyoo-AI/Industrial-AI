from durable.lang import *

with ruleset('AlarmMonitor'):
    # this rule will trigger for events with status
    @when_all((m.status=='<POST>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=ABORT>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=CLEAR>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=IGNORE>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=RETRY>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=WAIT>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=DISABLE>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=ENABLE>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<R=STOP>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all((m.status == '<CLEAR>') & (+m.alid))
    def event(c):
        print('AlarmMonitor-> Status {0} {1} {2}'.format(c.m.status, c.m.module, c.m.alid))

    @when_all(+m.alid and m.status == '<POST>')
    def fact(c):
        print('AlarmMonitor-> Alarm Added {0}'.format(c.m.alid))

    # this rule will be triggered when the fact is retracted
    @when_all(none(+m.alid))
    def empty(c):
        print('AlarmMonitor-> No Alarm! Alarm Clear')

# define variable
pLotDataFile = open("D:/CBNU/AlarmMonitor/alarm.log", "r")

for line in pLotDataFile.readlines():
    line = line.strip()
    # print(len(line))
    if len(line) > 0:
        words = line.split("\t")
        # print(len(words))

        AlarmInfo = words[2].split('  ')
        # print(AlarmInfo)
        AlarmItem = []
        for item in AlarmInfo:
            if item != '':
                AlarmItem.append(item)
                # print(AlarmItem)

        # will throw MessageObservedError because the fact has already been asserted
        try:
            if words[1] == "<POST>":
                assert_fact('AlarmMonitor', {
                    'status': words[1],
                    'module': AlarmItem[0].strip('['),
                    'alid': AlarmItem[1],
                    'alname': AlarmItem[2]
                })

        except BaseException as e:
            print('AlarmMonitor expected {0}'.format(e.message))

        if words[1] == "<CLEAR>":
            retract_fact('AlarmMonitor', {
                'status': words[1],
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })

            retract_fact('AlarmMonitor', {
                'status': '<R=ABORT>',
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })

            retract_fact('AlarmMonitor', {
                'status': '<R=CLEAR>',
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })

            retract_fact('AlarmMonitor', {
                'status': '<R=DISABLE>',
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })

            retract_fact('AlarmMonitor', {
                'status': '<R=ENABLE>',
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })

            retract_fact('AlarmMonitor', {
                'status': '<R=STOP>',
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })

            retract_fact('AlarmMonitor', {
                'status': '<R=WAIT>',
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })

            retract_fact('AlarmMonitor', {
                'status': '<POST>',
                'module': AlarmItem[0].strip('['),
                'alid': AlarmItem[1],
                'alname': AlarmItem[2]
            })