def set(age):
    if age < 0:
        raise Exception()
    print(f"Age set to {age}")

try:
    set(-5)

except Exception as e:
    print(e)