import subprocess

import schedule

import config


def vpn_off():
    subprocess.call(['sh', './vpn.sh'])


if __name__ == '__main__':
    schedule.every().day.at(config.time_for_schedule).do(vpn_off)
    while True:
        schedule.run_pending()
