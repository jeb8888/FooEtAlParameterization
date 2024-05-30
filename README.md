# Foo et al. Parameterization

> Uses Foo et al. parameterization to take the radius of a sphere and return its volume

## Setup

```
git clone foo_param
cd foo_param
sudo pip3 install -e .
```


## Unit Testing

```
python3 foo_param/tests/test_parameterization.py
```

## Contributing

If you have suggestions for how Foo et al. Parameterization could be improved, or want to report a bug, open an issue! We'd love all and any contributions.

For more, check out the [Contributing Guide](CONTRIBUTING.md).

## Python API

```
from foo_param.parameterization import FooParameterization

param = FooParameterization(5)
param.validate()
volume = param.calculate_volume()
print(f"Volume: {volume}")
```

## License

This project is licensed under the MIT License.