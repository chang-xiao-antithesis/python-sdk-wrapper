# Python Antithesis Fallback SDK Wrapper

**DISCLAIMER**

This is a simple Python wrapper for the [Antithesis fallback SDK](https://antithesis.com/docs/using_antithesis/sdk/fallback/overview.html) that allows you to access some of the functionalities of Antithesis. It is not official or supported by Antithesis in any way. It is meant as a stopgap measure before the release of the official Python SDK.

## How to use 

The `antithesis_sdk.py` contains a standalone class that can be imported into our Python application or workload like the following:

```
from antithesis_sdk import antithesis_fallback_sdk 
```

The class itself does not have any 3rd party dependencies

### Define Test Properties

There are the following types of test properties you can access. Please consult with Antithesis to better understand the test property types.

```
def always(declare:bool, id:str, message:str, condition:bool = False, details:dict = {})
def sometimes(declare:bool, id:str, message:str, condition:bool = False, details:dict = {})
def reachable(declare:bool, id:str, message:str, condition:bool = False, details:dict = {})
def unreachable(declare:bool, id:str, message:str, condition:bool = False, details:dict = {})
```

A quick explanation of the parameters

**declare -** Whether we are just declaring a test property (usually at the beginning of your program) or if set to false it means we are **evaluating** the test property.

**id -** A unique simple human-readable string to identify the test property, the declared value should be the same as the value of the evaluation. 

**message -** More descriptive information about the test property.

**condition -** Only needed if you set *declare* to *false*, which means you are evaulating the test property. Condition true means the test property passed and vice-versa.

**details -** Only needed if you set *declare* to *false*, A key/value dictionary to include additional information at the evaluation of the test property.

### Lifecycle Messages

```
def setup_complete(details:dict = {})
```

This indicates to Antithesis that your system is ready for testing (e.g. fault injection). For example, it is useful to invoke this at the start of the workload.

### Randomness

```
def get_random_int(bytes = 1)
```

This returns a random integer from Antithesis of a certain byte size. For example, bytes = 1 means you will get an integer between 0 and 255.

## Testing this locally

You can run the `test.py` script like the following:

```
ANTITHESIS_OUTPUT_DIR=./ python3 ./test.py
```

This test will simulate an indefinite workload that continues to populate an `sdk.jsonl` document. In **production Antithesis testing environment you do not have to define this environment variable**



