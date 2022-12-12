import pandas as pd
from pandas import DataFrame
import sys


def decorator_timer(some_function):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        end = time()-t1
        return result, end
    return wrapper


def expandDf(data: DataFrame) -> DataFrame:
    data[["elf1_zone_inf", "elf1_zone_sup"]] = data.elf1.str.split('-', expand=True)
    data[["elf2_zone_inf", "elf2_zone_sup"]] = data.elf2.str.split('-', expand=True)

    data[["elf1_zone_inf", "elf1_zone_sup"]] = \
        data[["elf1_zone_inf", "elf1_zone_sup"]].astype("int64")
    data[["elf2_zone_inf", "elf2_zone_sup"]] = \
        data[["elf2_zone_inf", "elf2_zone_sup"]].astype("int64")

    return data


@decorator_timer
def filterDf(data: DataFrame) -> DataFrame:
    filteredDf: DataFrame = data[((data.elf1_zone_inf >= data.elf2_zone_inf) &
                                  (data.elf1_zone_sup <= data.elf2_zone_sup)) |
                                 ((data.elf2_zone_inf >= data.elf1_zone_inf) &
                                  (data.elf2_zone_sup <= data.elf1_zone_sup))]

    return filteredDf


@decorator_timer
def filterDfWithQuery(data: DataFrame) -> DataFrame:
    elf1ZoneInElf2Zone: str = "((elf1_zone_inf >= elf2_zone_inf) and \
                                (elf1_zone_sup <= elf2_zone_sup))"
    elf2ZoneInElf1Zone: str = "((elf2_zone_inf >= elf1_zone_inf) and \
                                (elf2_zone_sup <= elf1_zone_sup))"

    filteredDf = data.query(elf1ZoneInElf2Zone + 'or' + elf2ZoneInElf1Zone)

    return filteredDf


def part1(inputDf: DataFrame) -> int:
    expandedDf = expandDf(inputDf)
    filteredDf, exec_time = filterDf(expandedDf)
    print(f"not query mode : {exec_time}")
    filteredDfWithQuery, exec_time = filterDfWithQuery(expandedDf)
    print(f"query mode : {exec_time}")

    result = len(filteredDf)

    return result


def part2(inputDf: DataFrame):
    result = None

    return result


if __name__ == "__main__":
    inputDf: DataFrame = pd.read_csv("input", sep=',', header=None, names=["elf1", "elf2"])

    match sys.argv[1]:
        case '1': print(part1(inputDf))
        case '2': print(part2(inputDf))
        case other: print("Type 1 or 2")
