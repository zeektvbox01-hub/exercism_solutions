"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_tuple):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(wagon_tuple)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first, second, third, *rest = each_wagons_id
    return [third ,*missing_wagons, *rest, first, second]


def add_missing_stops(route, **stops_dict):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    final_route = route
    stops_list = []
    for stop in stops_dict.values():
        stops_list.append(stop)
    final_route["stops"] = stops_list
    return final_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return {**route,**more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    [[colour_1_a,colour_1_b,colour_1_c],[colour_2_a,colour_2_b,colour_2_c],[colour_3_a,colour_3_b,colour_3_c]] = wagons_rows
    return [[colour_1_a,colour_2_a,colour_3_a],[colour_1_b,colour_2_b,colour_3_b],[colour_1_c,colour_2_c,colour_3_c]]
