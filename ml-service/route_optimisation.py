from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

import numpy as np


distance_matrix = np.load('./data/distance_matrix.npy')
def create_data_model():
    """Stores the data for the problem."""
    data = {
        'distance_matrix': distance_matrix,
        'num_vehicles': 3,  # Number of collection vehicles
        'depot': 0  # Starting point (depot)
    }
    return data

def solve_vrp():
    """Solve the VRP with OR-Tools."""
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set parameters for the search
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print_solution(manager, routing, solution, data)
    else:
        print('No solution found!')

def print_solution(manager, routing, solution, data):
    """Prints solution on console."""
    print('Objective: {}'.format(solution.ObjectiveValue()))
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        plan_output += ' {}\n'.format(manager.IndexToNode(index))
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        print(plan_output)

if __name__ == '__main__':
    solve_vrp()
