from antithesis_sdk import antithesis_fallback_sdk 
import time

def must_be_even_number(number:int) -> None:
    '''
    Example workload activity function
    '''

    print("Performing the workload activity must_be_even_number")

    # Evaulate sometimes assertion since we are recording each iteration of the workload completed
    # It's possible ot also set evaulation (condition to false i.e. if we failed to get a number)
    sdk.sometimes(declare=False, id="Performed workload iteration",message="performed workload iteration",condition=True)

    if number % 2 == 0:
        # You can also skip this always assertion and only assert on the failure case below
        sdk.always(declare=False, id="Must be even number", message="We got an even number divisible by 2",condition=True, details={"number received": number})
    else:
        sdk.always(declare=False, id="Must be even number", message="We got an odd number not divisible by 2",condition=False, details={"number received": number}) 

if __name__ == '__main__':

    sdk = antithesis_fallback_sdk()

    # # At the start of the workload we indicate that setup is complete 
    # # and we are ready to work
    sdk.setup_complete()

    # # We first declare the SDK assertions we want to use in this workload
    # # The always property corresponds to an invariant we check that must never fail
    sdk.always(declare=True, id="Must be even number", message="We got an odd number not divisible by 2")

    # We declare another sometimes property that indicates we should have some type of activities happen (at least once)
    # during this test
    sdk.sometimes(declare=True, id="Performed workload iteration", message="performed workload iteration")

    # Run the workload indefinitely
    while True:
        # getting a one byte random interger (0 - 255)
        random_int = sdk.get_random_int(1)
        print(f"Gotten random interger {random_int}")

        # the workload we run
        must_be_even_number(random_int)

        # 0 to 15 seconds sleep between each workload activity
        sleep_interval = random_int % 5
        print(f"Sleeping for {sleep_interval}")
        time.sleep(sleep_interval)
