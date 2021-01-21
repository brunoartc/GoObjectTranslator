import sys
import re


def translateType(tpeo:str):
    tpe = tpeo.replace("List<", "").replace("?", "")
    is_list = "[]" if tpeo.find("List") != -1 else ""
    if (tpe == "int" or tpe == "int64"):
        return is_list + "int"
    elif (tpe == "decimal" or tpe == "float64"):
        return is_list + "float64"
    elif (tpe == "string"):
        return is_list + "string"
    elif (tpe == "bool"):
        return is_list + "bool"
    elif (tpe == "DateTime"):
        return is_list + "time.Time"
    elif (tpe[0].isupper()):
        return is_list + tpe
    else:
        return is_list + "interface{}"

patternFindNameClass = r'(public class )([A-Za-z]+)'

patternFindName = r'(public *)((List<)*(string|DateTime|int|bool|decimal|[A-Z]+[A-z]*)(\?*))(( |>)*)([A-z]+)'

with open(sys.argv[1], 'r') as file:
    data = file.read().replace('\n', '')

print("type " + re.search(patternFindNameClass, data).groups()[1] + " struct {")
print("".join(["\t" + x[-1] + " " + translateType(x[1]) + "\n" for x in re.findall(patternFindName, data)]))
print("}")
input()


