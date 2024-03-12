import argparse
import os
from datetime import datetime

import colorama
from colorama import Fore

colorama.init(autoreset=True)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='File name')
    parser.add_argument('-d', '--date', help='date for search: less than "../2024-02-05 00:00:00.000", '
                                             'more than "2024-02-05 00:00:00.000/..", '
                                             'from - to "2024-02-05 00:00:00.000/2024-02-05 00:00:00.000", '
                                             'exact "2024-02-05 00:00:00.000"')
    parser.add_argument('-t', '--text', help='a text to look for')
    parser.add_argument('-n', '--unwanted', help='filter logs exclude text')
    parser.add_argument('--full', help='return full log entry instead of default symbols Qty',
                        action='store_true')
    args = parser.parse_args()
    return args


def parse_valid_date(line: str) -> datetime | bool:
    try:
        valid_date = datetime.fromisoformat(line[:23])
        return valid_date
    except ValueError:
        return False


def open_file(file_path: str) -> str:
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


def parse_data_from_file_or_directory(args_file: str) -> dict:
    abs_path = os.path.abspath(args_file)
    data = {}
    if os.path.isfile(abs_path):
        for data_line in open_file(abs_path):
            if parse_valid_date(data_line):
                data[parse_valid_date(data_line[:23])] = data_line
            else:
                data[list(data.keys())[-1]] += f'{data_line}'
    elif os.path.isdir(abs_path):
        for file in os.listdir(abs_path):
            file_path = os.path.join(abs_path, file)
            for data_line in open_file(file_path):
                if parse_valid_date(data_line):
                    data[parse_valid_date(data_line[:23])] = data_line
                else:
                    data[list(data.keys())[-1]] += f'{data_line}'
    return data


def find_by_date(args_date: str | None, data: dict) -> dict | str:
    data_by_date = {}
    if args_date is not None:
        if args_date.startswith('../'):
            time = parse_valid_date(parse_arguments().date[3:])
            for key, value in data.items():
                if key <= time:
                    data_by_date[key] = value
        elif args_date.endswith('/..'):
            time = parse_valid_date(parse_arguments().date[:-3])
            for key, value in data.items():
                if key >= time:
                    data_by_date[key] = value
        elif '/' in args_date:
            start_time, end_time = parse_valid_date(args_date.split('/')[0]), parse_valid_date(args_date.split('/')[1])
            for key, value in data.items():
                if start_time <= key <= end_time:
                    data_by_date[key] = value
        else:
            time = parse_valid_date(parse_arguments().date)
            for key, value in data.items():
                if key == time:
                    data_by_date[key] = value
    else:
        data_by_date = data
    return data_by_date


def find_by_text(args_text: str | None, data: dict) -> dict | str:
    data_by_text = {}
    if args_text is not None:
        for key, value in data.items():
            if args_text in value:
                data_by_text[key] = value
        if len(data_by_text) == 0:
            data_by_text = data
    else:
        data_by_text = data
    return data_by_text


def exclude_unwanted(args_unwanted: str | None, data: dict) -> dict | str:
    data_exclude_unwanted = {}
    if args_unwanted is not None:
        for key, value in data.items():
            if args_unwanted not in value:
                data_exclude_unwanted[key] = value
        if len(data_exclude_unwanted) == 0:
            data_exclude_unwanted = data
    else:
        data_exclude_unwanted = data
    return data_exclude_unwanted


def create_result_dict(args_file, args_date=None, args_text=None, args_unwanted=None):
    data_from_file = parse_data_from_file_or_directory(args_file)
    data_by_date = find_by_date(args_date, data_from_file)
    data_by_text = find_by_text(args_text, data_by_date)
    result_dict = exclude_unwanted(args_unwanted, data_by_text)

    return result_dict


def print_result(args_full: bool | None, data: dict, args_text=None):
    if args_full is True:
        for key, value in data.items():
            print(value)
    else:
        for key, value in data.items():
            if args_text is not None:
                start_index = max(value.find(args_text) - 150, 0)
                end_index = min(value.find(args_text) + len(args_text) + 150, len(value))
                before_arg_string = value[start_index:value.find(args_text)]
                after_arg_string = value[value.find(args_text) + len(args_text):end_index]
                print(before_arg_string + Fore.YELLOW + args_text + Fore.RESET + after_arg_string)
            else:
                print(Fore.YELLOW + f'{key}' + Fore.RESET + ' ' + value[:300])


def total_counts(full_data: dict, result_data: dict) -> str:
    total_logs = len(full_data)
    total_result_logs = len(result_data)
    print_count = (f'{Fore.RED}Total logs count: {Fore.GREEN}{total_logs}\n'
                   f'{Fore.RED}Total results count: {Fore.GREEN}{total_result_logs}')
    return print_count


parsed_args = parse_arguments()
file_from_args, date_from_args, text_from_args, unwanted_from_args, full_flag_from_args = (
    parsed_args.file, parsed_args.date, parsed_args.text, parsed_args.unwanted, parsed_args.full
)
data_full = parse_data_from_file_or_directory(file_from_args)
res_data = create_result_dict(file_from_args, date_from_args, text_from_args, unwanted_from_args)

print_result(full_flag_from_args, res_data, text_from_args)
print(total_counts(data_full, res_data))
