# A tiny Spanish dictionary made by using the dict() command

Patterns = {
    "rs": "rs|Line on right side",
    "ls": "ls|Line on left side",
    "ts": "ts|Line on top",
    "bs": "bs|Line on bottom",
    "tt": "tt|Triangle on top",
    "bt": "bt|Triangle on bottom",
    "bri": "bri|Brick pattern",
    "sku": "sku|Skull pattern",
    "cre": "cre|Creeper pattern",
    "drs": "drs|Diag Line Top L",
    "dls": "dls|Diag Line Top R",
    "ms": "ms|Horiz line through mid",
    "cs": "cs|Vert line through mid",
    "bts": "bts|Bottom Saw",
    "tts": "tts|Top Saw",
    "bl": "bl|Bottom-Left Box",
    "br": "br|Bottom-Right Box",
    "tl": "tl|Top-Left Box",
    "tr": "tr|Top-Right Box",
    "flo": "flo|Flower pattern",
    "gra": "gra|Gradient",
    "hh": "hh|Top Half",
    "vh": "vh|Left half",
    "mr": "mr|Middle Rhombus",
    "mc": "mc|Middle Circle",
    "cbo": "cbo|Curly Border",
    "moj": "moj|Mojang logo",
    "sc": "sc|+ Cross",
    "cr": "cr|x Cross",
    "bo": "bo|Border",
    "ss": "ss|Vertical Stripes",
    } 

print(Patterns['rs'])                   # calling left side like this returns the other
                                        # but how do you call the right side to return the left?

for item in Patterns:                   # this prints the left only
    print(item)


