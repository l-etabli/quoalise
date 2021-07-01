## TODO Embed metadata in SenML

- Date: 2019-04-23
- Id: <a name="use-senml">use-senml</a>
- Status: proposed
- Deciders: Gautier Husson, Cyril Lugan, Cédric Gelineau

## Identify devices with URNs

- Date: 2019-05-06
- Id: <a name="identify-devices-with-urns">identify-devices-with-urns</a>
- Status: proposed
- Deciders: Gautier Husson, Cyril Lugan, Cédric Gelineau

### Context

examples in Uniform Resource Names for Device Identifiers
https://datatracker.ietf.org/doc/rfc9039/

```
The optional underscore-separated components at the end of the DEV
   URN depict individual aspects of a device.  The specific strings and
   their semantics are up to the designers of the device, but could be
   used to refer to specific interfaces or functions within the device.
```

    urn:dev:ow:264437f5000000ed_humidity    # The humidity
                                            # part of a multi-sensor
                                            # device

    urn:dev:ow:264437f5000000ed_temperature # The temperature
                                            # part of a multi-sensor
                                            # device

SenML uses a colon for the same usage

```
urn:dev:ow:10e2073a01080063:voltage
```

### Decision

Use 'dev' urns as in RFC 9039, even without having a proper organisation id for now.

```
urn:dev:prm:30001610071843_consumption/active_power/raw
```

## Timestamp periods at their begining

- Date: 2020-12
- Id: <a name="stamp-time-periods-start">stamp-time-periods-start</a>
- Status: proposed
- Deciders: Cédric Gelineau

### Context

SenML associates a specific time with a specific value. This time can be ambiguous when the value have been computed over a period of time, like a power average.

SENML does not specify how time periods and aggregations are represented.

### Candidates

- Stamp at the period begning
  + used de facto in the Enedis API and Viriya
- Stamp at the period end
  + would make more sense, since it is the time at which the value can be computed

### Decision

Arbitrarily chosed to timestamp time periods at the begining :

```xml
<!-- 245 is the aggregated value during 60s, between  1600041600 and 1600041660.
<senml t="1600041600" v="245" />
<senml t="1600041660" v="250" />
```

## Use ISO format to represent time periods

- Date: 2020-12
- Id: <a name="use-iso-time-periods">use-iso-time-periods</a>
- Status: proposed
- Deciders: Cyril Lugan

### Context

Time periods might be needed

- when asking for data
- to represent the period used for a measurement mean
- to represent a measurement sampling period 

### Candidates

1. ISO 8601

  - Easier to read, way harder to parse
  - Standardized
  - Already used in Enedis APIs
  - Does not handle fraction of a second well (like 3 Hz)
  - Samples
    + `PT0.05S`: 50 miliseconds
    + `PT10M`: 10 minutes
    + `P2D`: 2 days
    + `P3Y6M4DT12H30M5S`: three years, six months, four days, twelve hours, thirty minutes, and five seconds

2. Seconds

  - Harder to read, easier to parse
  - SI unit
  - Already used in SENML
  - Does not handle fraction of a second well (like 3 Hz)
  - Samples
    + `0.05`: 0.05 miliseconds
    + `600`: 10 minutes
    + `172800`: 2 days

### Decision

Use ISO, which seems more expressive. Might change if parsing is annoying, or when needing to represent fractions of a second.

## Represent sensor measurements with SenML

- Date: 2019-04-23
- Id: <a name="use-senml">use-senml</a>
- Status: proposed
- Deciders: Gautier Husson, Gregory Elleouet

Use SenML to format raw data

https://tools.ietf.org/html/rfc8428

See [Rapport d’évaluation des formalismes de données](https://github.com/consometers/sen1-poc-docs/blob/master/Rapport_choix_formalisme.pdf) (fr).