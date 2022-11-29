# This file is part of the EESSI build-and-deploy bot,
# see https://github.com/EESSI/eessi-bot-software-layer
#
# The bot helps with requests to add software installations to the
# EESSI software layer, see https://github.com/EESSI/software-layer
#
# author: Bob Droege (@bedroge)
# author: Thomas Roeblitz (@trz42)
#
# license: GPLv2
#
import argparse


def parse_common_args(args=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", "--debug",
        help="print debug information",
        action="store_true",
    )

    parsed_args, unknown = parser.parse_known_args(args=args)

    return parsed_args, unknown


def event_handler_parse(args=None):
    parsed_args, unknown_args = parse_common_args(args=args)
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-b", "--build",
        help="accept software build requests",
        action="store_true",
    )
    parser.add_argument(
        "-t", "--test",
        help="accept software test requests",
        action="store_true",
    )

    parser.add_argument(
        "-f", "--file",
        help="use event data from a JSON file",
    )

    parser.add_argument(
        "-c", "--cron",
        help="run in cron mode instead of web app mode",
        action="store_true",
    )

    parser.add_argument(
        "-p", "--port", default=3000,
        help="listen on a specific port for events (default 3000)",
    )

    return parser.parse_args(args=unknown_args, namespace=parsed_args)


def job_manager_parse(args=None):
    parsed_args, unknown_args = parse_common_args(args=args)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--max-manager-iterations", default=-1,
        help="loop behaviour: i<0 - indefinite, i==0 - don't run, i>0: run i iterations (default -1)",
    )

    parser.add_argument(
        "-j", "--jobs",
        help="limits the processing to a specific job id or list of comma-separated list of job ids",
    )

    return parser.parse_args(args=unknown_args, namespace=parsed_args)
