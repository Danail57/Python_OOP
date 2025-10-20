def list_roman_emperors(*args, **kwargs):
    success_emperors = {}
    failed_emperors = {}
    result = ''

    for emperor_name, success_status in args:
        if success_status:
            success_emperors[emperor_name] = kwargs[emperor_name]
        else:
            failed_emperors[emperor_name] = kwargs[emperor_name]

    sorted_success_emperors = sorted(success_emperors.items(), key=lambda  kvp: (-kvp[1], kvp[0]))
    sorted_failed_emperors = sorted(failed_emperors.items(), key=lambda  kvp: (kvp[1], kvp[0]))

    result = f"Total number of emperors: {len(args)}"

    if success_emperors:
        result += f"\nSuccessful emperors: {len(success_emperors)}"

        for emperor_name, years in sorted_success_emperors:
            result += f'\n****{emperor_name}: {years}'

    if sorted_failed_emperors:
        result += f"\nUnsuccessful emperors: {len(sorted_failed_emperors)}"
        for emperor_name, years in sorted_failed_emperors:
            result += f'\n****{emperor_name}: {years}'

    return result

# print(list_roman_emperors(("Augustus",True), ("Nero", False), Augustus=40,Nero=14,))
# print(list_roman_emperors(("Augustus",True), ("Trajan", True), ("Nero", False),("Caligula", False), ("Pertinax", False),("Vespasian", True), Augustus=40,Trajan=19, Nero=14, Caligula=4,Pertinax=4, Vespasian=19,))
