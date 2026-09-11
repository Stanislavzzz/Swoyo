import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("--lang", default="ru", help="Язык приветствия")
args = parser.parse_args()


if args.lang == "ru":
    print(f'Привет. Твоё имя {args.name}')
elif args.lang == "en":
    print(f'Hello. Твоё имя {args.name}')
else:
    print(f'Неизвестное имя {args.lang}')
