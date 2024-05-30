import argparse
import json
from foo_param.foo_param.foo_param import FooParameterization

def main():
    parser = argparse.ArgumentParser(description="Foo Physics Simulation")
    parser.add_argument('--radius', type=float, required=True, help="Radius of the sphere")
    args = parser.parse_args()

    parameterization = FooParameterization(args.radius)
    try:
        parameterization.validate()
    except ValueError as e:
        print(f"Validation Error: {e}")
        return

    volume = parameterization.calculate_volume()
    print(f"Calculated Volume: {volume}")



if __name__ == "__main__":
    main()