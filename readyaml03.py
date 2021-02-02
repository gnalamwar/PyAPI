#!/usr/bin/python3

import yaml

def main():
    ## Open a blob of YAML data
    with open("myYAML.yml", "r") as yf:
        pyyammy = yaml.load(yf)

    # display our new Python data
    print(pyyammy)


if __name__ == "__main__":
    main()
